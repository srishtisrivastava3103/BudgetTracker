from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns=[
            #url(r'$', views.HomeView,name='home'),
            #url(r'^user/new/$',views.CreateProfile.as_view(),name='create_profile'),
            path('',views.HomeView,name="Home"),
            path('login',views.LoginView,name="Login"),
            path('signup',views.SignupView,name='SignUp'),
            path('user_expense',views.User_Expense_View,name="UserExpenses"),
            path('new_post', views.NewPost, name='NewPost'),
            path('All Posts', views.PostList.as_view(), name='AllPosts'),
            path('posts/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
            path('cashflow', views.CashflowView, name="cashflow_management"),

]