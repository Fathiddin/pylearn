from django.contrib import admin
from .models import UploadFile, Posts
# Register your models here.


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    prepopulated_fields = {"slug_id": ("title",)}

admin.site.register(UploadFile)