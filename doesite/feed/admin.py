from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Profile)
admin.site.register(Post)

class ProfileInLine(admin.StackedInline):
    model = Profile