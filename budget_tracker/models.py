from django.db import models
#from django.contrib.auth.models
import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, unique=True,)
    email = models.EmailField(null=False, unique=True)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    budget = models.DecimalField(max_digits=6, decimal_places=2)
    password = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.username



class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    percentage = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    date=models.DateField()


class Bill(Expense):
    Electricity = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    Water = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    Rent = models.DecimalField(blank=False, max_digits=20, decimal_places=2)


class Food(Expense):
    Junk = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    Grocery = models.DecimalField(default=0, max_digits=20, decimal_places=2)


class Entertainment(Expense):
    Movies = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    Shopping = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    Special_Occasions = models.DecimalField(blank=False, max_digits=20, decimal_places=2)


class Travel(Expense):
    Local = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    Work = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    Trips = models.DecimalField(blank=False, max_digits=20, decimal_places=2)


class Misc(Expense):
    Medical = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    Unlabelled = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
