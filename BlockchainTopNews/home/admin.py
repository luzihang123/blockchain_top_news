from django.contrib import admin

# Register your models here.


from home.models import Category, Tag, Article

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
