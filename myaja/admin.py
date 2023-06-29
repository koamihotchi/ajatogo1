from django.contrib import admin
from .models import Articles,Newsletter

# Register your models here.
admin.site.register(Articles)
admin.site.register(Newsletter)