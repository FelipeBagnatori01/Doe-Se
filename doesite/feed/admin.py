from django.contrib import admin
from django.contrib.auth.models import Group, User
# Register your models here.
from .models import *

admin.site.unregister(Group)
admin.site.register(Post)

class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInLine]
    
admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Profile)

