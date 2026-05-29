from django.contrib import admin
from manage_posts.models import Category, Article, Rating



# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Rating)