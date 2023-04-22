from django.shortcuts import render, redirect
from django.views import View

from myapp.Classes.supervisor import Supervisor
from myapp.Classes.users import User, UserUtility
from myapp.models import User, Course, Section, CourseToUser


# Create your views here.


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(
            User_LogName=username, User_LogPass=password)
        if user:
            return redirect('index')
        else:
            return redirect('login')


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class AccountBase(View):
    def get(self, request):
        users = UserUtility.get_all_users()
        print(users)
        return render(request, 'accountbase.html', {"users": users})

    def searchUser(self):
        pass

    def filterUser(self):
        pass

    def deleteUser(self):
        pass


# want to return the same view but for a specific course


# class InstructorToCourse(View):
#
#     def get(self, request):
#         return render(request, 'createaccount.html')
#
#     def assignInstructors(self):
#         pass
#
#     def getInstructor(self):
#         pass
#
#     def removeInstructor(self):
#         pass


class CreateAccount(View):
    def get(self, request):
        return render(request, 'createaccount.html')

    def post(self, request):
        Supervisor.create_account(request.POST.get('firstname'), request.POST.get('lastname'),
                                  request.POST.get('email'), request.POST.get('username'), request.POST.get('password'),
                                  request.POST.get('address'), request.POST.get('city'),
                                  request.POST.get('number'), request.POST.get('position'))
        return render(request, 'accountbase.html')


class EditAccount(View):
    def get(self, request):
        return render(request, 'editaccount.html')
