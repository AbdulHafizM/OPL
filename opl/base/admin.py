from django.contrib import admin
from .models import Calendar
from .models import Blog, Admission
# Register your models here.

admin.site.register(Calendar)
admin.site.register(Blog)
admin.site.register(Admission)
