from django.contrib import admin
from courses.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(User)