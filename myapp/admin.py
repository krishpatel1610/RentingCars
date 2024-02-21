from django.contrib import admin
from .models import usertable, contactus, vehicle_table, feedback, booking_table
# Register your models here.
class showusertable(admin.ModelAdmin):
    list_display = ['emailid','phoneno','password','name','licence_no','address','role','status','id']

admin.site.register(usertable,showusertable)

class showvehicle_table(admin.ModelAdmin):
      list_display = ['vehicle_name','vehicle_color','venicle_type','vehicle_number','vehicle_photo','vehicle_description','rent_per_day']

admin.site.register(vehicle_table,showvehicle_table)

class showbook(admin.ModelAdmin):
     list_display = ['vehicle_id','login_id','from_duration','from_to','amount','reciept','booking_date','paystatus']

admin.site.register(booking_table,showbook)


class showcontact(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'contact_date']

admin.site.register(contactus,showcontact)

class showfeedback(admin.ModelAdmin):
    list_display = ['l_id', 'name', 'ratings', 'comments']

admin.site.register(feedback,showfeedback)