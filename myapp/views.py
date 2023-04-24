from django.shortcuts import render, redirect
from django.views import View

from myapp.Classes.supervisor import Supervisor
from myapp.Classes.users import Users, UserUtility
from myapp.models import User, Course, Section, CourseToUser
from . import views


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
        # get value of method from within request.POST
        method = request.POST.get('method')

        # filterUser functionality
        if method == 'filterUser':
            search_type = request.POST.get('position')
            users = Users.filterUser(search_type)
            #  the isinstance function checks if the result variable contains an instance of the TypeError class
            if isinstance(users, TypeError):
                return render(request, 'accountbase.html', {"message": "You didn't select a User Type"})
            return render(request, 'accountbase.html', {"users": users})

        # searchUser functionality
        elif method == "searchUser":
            search_name = request.POST.get('search')
            user = Users.searchUser(search_name)
            #  the isinstance function checks if the result variable contains an instance of the TypeError class
            if isinstance(user, TypeError):
                return render(request, 'accountbase.html', {"message": "No user with that last name"})
            return render(request, 'accountbase.html', {"users": user})

        # deleteUser functionality
        elif method == "deleteUser":
            username = request.POST.get('username')
            Supervisor.deleteUser(username)
            user = UserUtility.get_all_users()
            return render(request, 'accountbase.html', {"users": user})

        # create account functionality
        else:
            result = Supervisor.create_account(request.POST.get('firstname'), request.POST.get('lastname'),
                                               request.POST.get('email'), request.POST.get('username'),
                                               request.POST.get('password'),
                                               request.POST.get('address'), request.POST.get('city'),
                                               request.POST.get('number'), request.POST.get('position'))

            #  the isinstance function checks if the result variable contains an instance of the TypeError class
            if isinstance(result, TypeError):
                return render(request, 'createaccount.html',
                              {"message": "You forgot to fill in one of the fields - please fill out form again"})
            users = UserUtility.get_all_users()
            return render(request, 'accountbase.html', {"users": users})


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
        courses = Course.objects.all()
        return render(request, 'course_base.html', {"courses": courses})

    def post(self, request):
        courses = Course.objects.all()
        result = Supervisor.create_course(request.POST.get('course_code'), request.POST.get('course_name'),
                                          request.POST.get('course_desc'), request.POST.get('course_inst'))
        if isinstance(result, TypeError):
            users = UserUtility.get_all_users()
            return render(request, 'createcourse.html', {"users": users, "message": result})
        return render(request, 'course_base.html', {"courses": courses})


class CreateCourse(View):
    TEMPLATE = "createcourse.html"

    def get(self, request):
        users = UserUtility.get_all_users()
        return render(request, 'createcourse.html', {"users": users})

    def post(self, request):
        return render(request, 'createcourse.html', {"success": "course created"})


class EditCourse(View):

    def get(self, request, *args, **kwargs):
        c_code = kwargs['Course_Code']
        course = Course.objects.get(Course_Code=c_code)
        users = UserUtility.get_all_users()
        return render(request, 'courseedit.html', {'course': course, "users": users})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        course_code = kwargs['Course_Code']
        actCourse = Course.objects.get(Course_Code=course_code)
        print(course_code)
        print(actCourse)
        made_instructor = request.POST.get('Course_Instructor')
        if made_instructor == actCourse.Course_Instructor:
            return render(request, 'courseedit.html', {"error": "this instructor is already assigned to the course"})

        elif actCourse.Course_Instructor is not "":
            print(Course.objects.get(Course_Code=course_code).Course_Instructor)
            Supervisor.removeInstructorFromClass(request.POST.get('Course_Instructor'), course_code)
            return redirect('courseedit', Course_Code=course_code)
        else:
            Supervisor.addInstructor(request.POST.get('Course_Instructor'), course_code)
            courses = Course.objects.all()

            return redirect('/course_base', {course_code})
