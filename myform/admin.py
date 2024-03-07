from django.contrib import admin

# Register your models here.
from .models import MyForm, UserSchema

admin.site.register(MyForm)
admin.site.register(UserSchema)