from django.contrib import admin
from home.models import Contact
from .models import *

# Register your models here.

admin.site.register(Contact),
admin.site.register(Patient),
admin.site.register(Book),
admin.site.register(Doctor),
admin.site.register(Room),


