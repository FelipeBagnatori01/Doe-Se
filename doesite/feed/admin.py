from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Institute)
admin.site.register(Post)
admin.site.register(Follows)