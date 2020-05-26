from django import forms
from budget_tracker.models import User, account, Expense, Food, Bill, Entertainment, Travel, Misc


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'budget', 'password')
        widgets = {
            'password': forms.PasswordInput()}


class AccountForm(forms.ModelForm):
    class Meta:
        model = account
        fields = ('accno', 'bank', 'balance')

class DateInput(forms.DateInput):
    input_type = 'date'

class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('amount','date')
        # widgets = {
        #     'date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%d'),
        widgets = {"date":DateInput()}



class ExpenseForm(ExpenseModelForm):
    choices=[("Misc: Unlabelled","Misc: Unlabelled"),("Misc: Medical","Misc: Medical"),("Food: Junk","Food: Junk"),
             ("Food: Grocery","Food: Grocery"),("Bill: Electricity","Bill: Electricity"),("Bill: Rent","Bill: Rent"),
             ("Bill: Water","Bill: Water"),("Entertainment: Movies","Entertainment: Movies"),
             ("Entertainment: Shopping","Entertainment: Shopping"),
             ("Entertainment: Special_Occasions","Entertainment: Special Occasions"),
             ("Travel: Local","Travel: Local"),("Travel: Work","Travel: Work"),("Travel: Trips","Travel: Trips"),]
    Category = forms.ChoiceField(choices=choices)


    class Meta(ExpenseModelForm.Meta):
        fields = ExpenseModelForm.Meta.fields + ('Category',)
        widgets = {"date": DateInput()}


