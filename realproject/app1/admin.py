from django.contrib import admin
from .models import login
# Register your models here.


# Register your models here.
from .models import Donation 
from . import models

class DonationAdmin(admin.ModelAdmin):
    list_display=['id' ,'Name' , 'Description' , 'Targetprice' ]
admin.site.register(models.Donation,DonationAdmin)
admin.site.register(login)