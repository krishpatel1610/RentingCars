from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

class usertable(models.Model):
    emailid = models.CharField(max_length=40)
    phoneno = models.CharField(max_length=13)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    licence_no = models.CharField(max_length=50)
    address = models.TextField()
    role = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.emailid

class vehicle_table(models.Model):
    vehicle_name = models.CharField(max_length=40)
    vehicle_color = models.CharField(max_length=40)
    vehicle_number = models.CharField(max_length=40)
    venicle_type = models.CharField(max_length=40)
    vehicle_photo = models.ImageField(upload_to='photos')
    vehicle_description = models.TextField()
    rent_per_day = models.CharField(max_length=40)

    def vehicle_image(self):
        return mark_safe('<img src="fi" width="100" />'.format(self.vehicle_photo.url))

    vehicle_image.allow_tags= True

    def __str__(self):
        return self.vehicle_name

class booking_table(models .Model):
    vehicle_id = models.ForeignKey(vehicle_table,on_delete=models.CASCADE)
    login_id = models.ForeignKey(usertable,on_delete=models.CASCADE)
    from_duration = models. DateField()
    from_to = models.DateField()
    amount = models.CharField(max_length=35)
    reciept=models.ImageField(upload_to="reciepts",null=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    paystatus = models.IntegerField()

class feedback(models.Model):
    l_id = models.ForeignKey(usertable,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    ratings = models.CharField(max_length=25)
    comments = models.CharField(max_length=50)

    def __str__(self):
        return self.ratings

class contactus(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.CharField(max_length=30)
    contact_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name