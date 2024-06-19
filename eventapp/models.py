from django.db import models

# Create your models here.
class Customer(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = "customer"

class Administration(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "administration"

class Eventmanager(models.Model):
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


    class Meta:
        db_table = "eventmanager"


class Addevent(models.Model):
    email=models.EmailField(max_length=100,default=0)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    venue = models.CharField(max_length=100)
    venueaddress = models.CharField(max_length=100)
    datatime=models.CharField(max_length=100,default=0)
    contactnumber = models.BigIntegerField()
    entryfee = models.BigIntegerField()

    class Meta:
        db_table = "addevent"


class Bookevent(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    addevent = models.ForeignKey(Addevent, on_delete=models.CASCADE)
    cost = models.BigIntegerField()
    Date_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = "bookings"


class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    addevent = models.ForeignKey(Addevent, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.BigIntegerField()
    title = models.CharField(max_length=100)
    review = models.CharField(max_length=100)
    class Meta:
        db_table = "review"