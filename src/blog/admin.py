from django.contrib import admin
from .models import Article, Comment

# Register your models here.

#여기도 startapp애 따라서 생성을 해야함.
@admin.register(Article, Comment)
class BlogAdmin(admin.ModelAdmin):
    pass
