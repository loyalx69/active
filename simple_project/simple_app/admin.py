from django.contrib import admin
from simple_app.models import Mypost, Category, Author

# Register your models here.
admin.site.register(Mypost)
admin.site.register(Author)
admin.site.register(Category)