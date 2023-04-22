from django.contrib import admin
from myapp.models import User, Course, Section, CourseToUser

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(CourseToUser)
