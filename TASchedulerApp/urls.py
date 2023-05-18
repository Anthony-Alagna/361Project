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
from django.contrib.auth.views import LoginView, LogoutView
from myapp.views import (
    AccountBase,
    Home,
    CreateAccount,
    EditAccount,
    ViewPersonalInformation,
    ForgotPasswordView,
    ForgotPassword,
    viewSection,
    createSection,
    CourseBase,
    CreateCourse,
    EditCourse,
    ViewAccount,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", Home.as_view(), name="home"),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("forgotpassword/", ForgotPasswordView.as_view(), name="forgotpassword"),
    path("home/accountbase/", AccountBase.as_view(), name="accountbase"),
    path(
        "home/accountbase/createaccount/", CreateAccount.as_view(), name="createaccount"
    ),
    path("home/accountbase/editaccount/<int:id>",
         EditAccount.as_view(), name="editaccount"),
    path("home/course_base/", CourseBase.as_view(), name="course_base"),
    path("home/course_base/createcourse",
         CreateCourse.as_view(), name="createcourse"),
    path(
        "home/personal_information/<int:id>",
        ViewPersonalInformation.as_view(),
        name="personal_information",
    ),
    # have embed course id into url so that it can be retrieved to my method
    path(
        "home/course_base/courseedit/<str:Course_Code>",
        EditCourse.as_view(),
        name="courseedit",
    ),
    path("home/accountbase/viewaccount/<int:id>", ViewAccount.as_view(),
         name="viewaccount"),
    path(
        "home/course_base/coursesection.html<str:Course_Code>",
        viewSection.as_view(),
        name="coursesection",
    ),
    path("home/course_base/createsection.html",
         createSection.as_view(), name="createsection")
]
