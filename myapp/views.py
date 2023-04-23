from django.shortcuts import render, redirect
from django.views import View

from myapp.Classes.supervisor import Supervisor
from myapp.Classes.users import Users, UserUtility
from myapp.models import User, Course, Section, CourseToUser
from myapp.Classes.courses import CourseUtility

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
        return render(request, 'accountbase.html', {"users": users})

    def post(self, request):

        print(request.POST)
        # get value of method from within request.POST
        method = request.POST.get('method')

        # filterUser functionality
        if method == 'filterUser':
            user = request.POST.get('position')
            users = Users.filterUser(user)
            return render(request, 'accountbase.html', {"users": users})

        # searchUser functionality
        elif method == "searchUser":
            search_name = request.POST.get('search')
            print("searchname", search_name)
            user = Users.searchUser(search_name)
            return render(request, 'accountbase.html', {"users": user})

        elif method == "deleteUser":
            username = request.POST.get('username')
            Supervisor.deleteUser(username)
            user = UserUtility.get_all_users()
            return render(request, 'accountbase.html', {"users": user})

        # create account functionality
        else:
            result = Supervisor.create_account(request.POST.get('firstname'), request.POST.get('lastname'),
                                  request.POST.get('email'), request.POST.get('username'), request.POST.get('password'),
                                  request.POST.get('address'), request.POST.get('city'),
                                  request.POST.get('number'), request.POST.get('position'))

        #  the isinstance function checks if the result variable contains an instance of the TypeError class
            if isinstance(result, TypeError):
                return redirect('createaccount')

            users = UserUtility.get_all_users()
            return render(request, 'accountbase.html', {"users": users})



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
        return render(request, 'createaccount.html')


class EditAccount(View):
    def get(self, request):
        return render(request, 'editaccount.html')


class CourseBase(View):
    def get(self, request):
        courses = CourseUtility.get_course_list()
        return render(request, 'course_base.html', {"courses": courses})

    def post(self, request):
        CourseUtility.create_course(request.POST.get('course_name'), request.POST.get('course_code'),
                                    request.POST.get('course_desc'))
        courses = CourseUtility.get_course_list()
        return render(request, 'course_base.html', {"courses": courses})


class CreateCourse(View):
    TEMPLATE = "createcourse.html"

    def get(self, request):
        return render(request, 'createcourse.html')

    def post(self, request):
        return render(request, 'createcourse.html', {"success": "course created"})
