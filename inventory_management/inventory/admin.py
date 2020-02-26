from django.contrib import admin

from .models import *

# Register your models here.
admin.site.site_header = "IMS Admin"
admin.site.site_title = "IMS Admin"
admin.site.index_title = "Welcome to IMS Admin Dashboard"

admin.site.register(Item)
