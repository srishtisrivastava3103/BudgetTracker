from django.shortcuts import render, get_object_or_404, redirect
from budget_tracker.models import User, Expense,Food, Bill,Travel,Entertainment,Misc
import matplotlib.pyplot as plt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db import connection
import os
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from budget_tracker.forms import SignUpForm, ExpenseForm
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.
# class HomeView(TemplateView):
#   template_name = 'home.html'
g_username = ""
g_password = ""


def HomeView(request):
    return (render(request, 'budget_tracker/home.html'))


'''class CreateProfile(CreateView,LoginRequiredMixin):
    login_url='/login/'
    redirect_field_name='budget_tracker/userprofile.html'
    form_class=LoginForm
    model=account'''


def SignupView(request):
    if request.method == "POST":
        form1 = SignUpForm(request.POST)

        if form1.is_valid():
            form1.save()

            return render(request, 'budget_tracker/login.html', {'form1': form1})
    else:
        form1 = SignUpForm
        return render(request, 'budget_tracker/signup.html', {'form1': form1})
    return HttpResponseRedirect(reverse('Login'))


from django.contrib.auth import authenticate, login

'''def LoginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect('/budget_tracker/login')


    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect('/budget_tracker/signup')'''


def LoginView(request):
    global g_username
    global g_password
    if request.method == 'POST':
        username = request.POST.get('username')
        # username=username.lower()
        password = request.POST.get('password')
        # user = authenticate(username=username, password=password)
        for i in User.objects.all():
            if (i.username == username):
                if i.password == password:
                    g_username = username
                    g_password = password
                    return HttpResponseRedirect(reverse('UserExpenses'))

            # if user.is_active:
            # login(request,user)
            # else:
            #   return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'budget_tracker/login.html', {})


def User_Expense_View(request):
    global g_username
    expense_list=[]
    amt=0
    amt_list=[]
    for i in Food.objects.all():
        if str(i.user)==str(g_username):
            amt+=i.amount
            if i.Junk>0:
                expense_list+=[["Food: Junk", str(i.Junk), str(i.date)]]
            else:
                expense_list+=[["Food: Grocery", str(i.Grocery), str(i.date)]]
    amt_list+=[amt]
    amt=0

    for i in Bill.objects.all():
        if str(i.user) == str(g_username):
            amt += i.amount
            if i.Water > 0:
                expense_list += [["Bill: Water", str(i.amount), str(i.date)]]
            if i.Electricity > 0:
                expense_list += [["Bill: Electricity", str(i.amount), str(i.date)]]
            if i.Rent > 0:
                expense_list += [["Bill: Rent", str(i.amount), str(i.date)]]
    amt_list += [amt]
    amt = 0

    for i in Travel.objects.all():
        if str(i.user) == str(g_username):
            amt += i.amount
            if i.Work > 0:
                expense_list += [["Travel: Work", str(i.amount), str(i.date)]]
            if i.Local > 0:
                expense_list += [["Travel: Local", str(i.amount), str(i.date)]]
            if i.Trips > 0:
                expense_list += [["Travel: Trips", str(i.amount), str(i.date)]]
    amt_list += [amt]
    amt = 0

    for i in Entertainment.objects.all():
        if str(i.user) == str(g_username):
            amt += i.amount
            if i.Movies > 0:
                expense_list += [["Entertainment: Movies", str(i.amount), str(i.date)]]
            if i.Shopping > 0:
                expense_list += [["Entertainment: Shopping", str(i.amount), str(i.date)]]
            if i.Special_Occasions > 0:
                expense_list += [["Entertainment: Special Occasions", str(i.amount), str(i.date)]]

    amt_list += [amt]
    amt = 0
    for i in Misc.objects.all():
        if str(i.user) == str(g_username):
            amt += i.amount
            if i.Medical > 0:
                expense_list += [["Misc: Medical", str(i.amount), str(i.date)]]
            if i.Unlabelled > 0:
                expense_list += [["Misc: Unlabelled", str(i.amount), str(i.date)]]
    expense_list=sorted(expense_list, key=lambda x: x[2], reverse=True)

    amt_list += [amt]
    amt = 0

    plt.cla()
    labels = ['Food','Bills','Travel','Entertainment','Misc']
    # colors
    colors = ['#f5f240','#ba68c8', '#64b5f6', '#00e676', '#f06292']

    # # explsion
    explode = (0.05, 0.05, 0.05, 0.05,0.05)

    plt.pie(amt_list, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode=explode)
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.90, fc='#f5f0f3')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.tight_layout()
    # Equal aspect ratio ensures that pie is drawn as a circle

    plt.savefig("budget_tracker/static/Plot.png",transparent=True)

    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            Category = form.cleaned_data['Category'].split(":")[0]
            Sub=form.cleaned_data['Category'].split( ":")[1]
            Sub=Sub[1:]
            amt=0
            amt_list=[]
            date=form.cleaned_data['date']
            amount = int(form.cleaned_data['amount'])
            for i in User.objects.all():
                if i.username == g_username:
                    obj = Expense(user=i, amount=amount, percentage=0,date=date)
                    obj.save()
                    if Category=="Food":
                        if Sub=="Junk":
                            ob = Food(expense_id=obj.expense_id,amount=amount,user=i,date=obj.date, Junk=amount, Grocery=0, percentage=0)
                        if Sub=="Grocery":
                            ob = Food(expense_id=obj.expense_id,amount=amount,user=i,date=obj.date, Junk=0,Grocery=amount, percentage=0)
                    if Category == "Bill":
                        if Sub == "Water":
                            ob = Bill(expense_id=obj.expense_id, amount=amount,date=obj.date, user=i, Water=amount, Electricity=0,Rent=0,
                                      percentage=0)
                        if Sub == "Electricity":
                            ob = Bill(expense_id=obj.expense_id, amount=amount,date=obj.date, user=i, Water=0, Electricity=amount,Rent=0,
                                      percentage=0)
                        if Sub == "Rent":
                            ob = Bill(expense_id=obj.expense_id, amount=amount,date=obj.date, user=i, Water=0, Electricity=0,Rent=amount,
                                      percentage=0)
                    if Category=="Entertainment":
                        if Sub=="Movies":
                            ob=Entertainment(expense_id=obj.expense_id, amount=amount,date=obj.date, user=i, Movies=amount,Shopping=0,Special_Occasions=0)
                        if Sub == "Shopping":
                            ob = Entertainment(expense_id=obj.expense_id, amount=amount,date=obj.date, user=i, Movies=0,
                                               Shopping=amount, Special_Occasions=0)
                        if Sub == "Special Occasion":
                            ob = Entertainment(expense_id=obj.expense_id, amount=amount,date=obj.date, user=i, Movies=0,
                                               Shopping=0, Special_Occasions=amount)
                    if Category == "Travel":
                        if Sub == "Local":
                            ob = Travel(expense_id=obj.expense_id, amount=amount,date=obj.date, user=i, Local=amount,
                                               Work=0, Trips=0)
                        if Sub == "Work":
                            ob = Travel(expense_id=obj.expense_id, amount=amount,date=obj.date, user=i, Local=0,
                                               Work=amount, Trips=0)
                        if Sub == "Trips":
                            ob = Travel(expense_id=obj.expense_id, amount=amount,date=obj.date, user=i, Local=0,
                                               Work=0, Trips=amount)
                    if Category == "Misc":
                        if Sub == "Medical":
                            ob = Misc(expense_id=obj.expense_id, amount=amount,date=obj.date, user=i, Medical=amount, Unlabelled=0)
                        if Sub == "Unlabelled":
                            ob = Misc(expense_id=obj.expense_id, amount=amount, date=obj.date,user=i, Medical=0, Unlabelled=amount)

                    ob.save()
                    print(expense_list)

            return HttpResponseRedirect(reverse('UserExpenses'))
        else:

            print("Adding expense failed")
            return HttpResponseRedirect(reverse('UserExpenses'))
    else:
        form = ExpenseForm
        return render(request, 'budget_tracker/user_expense_page.html', {'form': form, 'username': g_username,'expense_list':expense_list})
