"""TASchedulerApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import AccountBase, Login, Home, CreateAccount, EditAccount, CourseBase, CreateCourse, EditCourse, EditPersonalInformation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home.as_view(), name='home'),
    path('', Login.as_view(), name='login'),
    path('home/accountbase/', AccountBase.as_view(), name='accountbase'),
    path('home/accountbase/createaccount/',
         CreateAccount.as_view(), name='createaccount'),
    path('home/accountbase/editaccount/', EditAccount.as_view(), name='editaccount'),
    path('home/course_base/', CourseBase.as_view(), name='course_base'),
    path('home/course_base/createcourse', CreateCourse.as_view(), name='createcourse'),
    path('home/personal_information', EditPersonalInformation.as_view(),
         name='personal_information'),
    # have embed course id into url so that it can be retrieved to my method
    path('course_base/courseedit/<str:Course_Code>',
         EditCourse.as_view(), name='courseedit')
]
