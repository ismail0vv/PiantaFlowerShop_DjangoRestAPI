from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Flower)
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Review)
admin.site.register(Color)
