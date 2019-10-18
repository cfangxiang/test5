from django.contrib import admin
from .models import *
class BookInfoadmin(admin.ModelAdmin):
    list_display=['id','btitle','bpub_date']
admin.site.register(BookInfo,BookInfoadmin)
admin.site.register(Test1)