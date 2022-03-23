from django.contrib import admin
from .models import hydjobs,banglorejobs,chennaijobs,punejobs
# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display = ['Date','Company','Title','Eligibility','Address','Email','Phonenumber']

class banglorejobsAdmin(admin.ModelAdmin):
    list_display = ['Date','Company','Title','Eligibility','Address','Email','Phonenumber']

class chennaijobsAdmin(admin.ModelAdmin):
    list_display = ['Date','Company','Title','Eligibility','Address','Email','Phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display = ['Date','Company','Title','Eligibility','Address','Email','Phonenumber']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(banglorejobs,banglorejobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
