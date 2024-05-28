from django.contrib import admin
from .models import *


@admin.register(Post)
class Post(admin.ModelAdmin):
    pass
