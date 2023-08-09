from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
# admin.site.register(Profile)
admin.site.register(Address)
class ContactadminView(admin.ModelAdmin):
    list_display = ['Name','Email','Phone','Subject','Message']
admin.site.register(Contact, ContactadminView)
