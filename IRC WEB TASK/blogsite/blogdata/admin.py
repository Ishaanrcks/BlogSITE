from django.contrib import admin
from blogdata.models import Blog_data
# Register your models here.
class blogdata_adm(admin.ModelAdmin):
    list_display=('Blog_Id','User_Name','Blog_Name','Blog','Blog_Image')
admin.site.register(Blog_data,blogdata_adm)
