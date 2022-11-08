from django.contrib import admin
from .models import Application_Form,CreateForm,FormValidation

# Register your models here.
class create(admin.ModelAdmin):
    list_display = ('Name',"Email",'Phone','Password')
admin.site.register(Application_Form)
admin.site.register(CreateForm,create)
admin.site.register(FormValidation,create)