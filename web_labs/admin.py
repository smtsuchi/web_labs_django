from django.contrib import admin

from .models import Account, Course, Section, Lesson, User_Lesson
# Register your models here.
admin.site.register(Account)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(User_Lesson)