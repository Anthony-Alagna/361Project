from django.shortcuts import render, redirect
from django.views import View

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
        return render(request, 'accountbase.html')

    def searchUser(self):
        pass

    def filterUser(self):
        pass

    def deleteUser(self):
        pass



class InstructorToCourse(View):

    def get(self, request):
        return render(request, 'createaccount.html')

    def assignInstructors(self):
        pass

    def getInstructor(self):
        pass

    def removeInstructor(self):
        pass


class CreateAccount(View):
    def get(self, request):
        return render(request, 'createaccount.html')


class EditAccount(View):
    def get(self, request):
        return render(request, 'editaccount.html')


class CourseBase(View):
    def get(self, request):
        return render(request, 'course_base.html')


class CreateCourse(View):
    def get(self, request):
        return render(request, 'createcourse.html')

    def post(self, request):
        name = request.POST.get('name')
        code = request.POST.get('code')
        course = Course.objects.filter(
            Course_Name=name, Course_Code=code)
