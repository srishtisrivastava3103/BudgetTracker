from django.db import models
#from django.contrib.auth.model
from django.utils import timezone

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

# class Post(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
#     title = models.CharField(max_length=60, unique=True)
#     content = models.CharField(max_length=2000)
#     datetime = models.DateTimeField(default=timezone.now())

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"slug": str(self.slug)})

class Assets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    asset = models.CharField(max_length=100, unique=True)
class Liability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    liability = models.CharField(max_length=100, unique=True)





