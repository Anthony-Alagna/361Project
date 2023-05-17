import datetime

from django.shortcuts import render, redirect
from django.views import View
from myapp.Classes.supervisor import Supervisor
from myapp.Classes.users import Users, UserUtility
from myapp.models import User, Course, Section, CourseToUser


# Create your views here.


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.get(email=username, User_LogPass=password)
        if user:
            # used to store the username in the session, so that it can be used later
            request.session["username"] = username
            user.isLoggedIn = True
            user.save()
            return redirect("home")
        else:
            # return status code 302
            return redirect("login")


class ForgotPassword(View):
    def get(self, request):
        return render(request, "forgotpassword.html")

    def post(self, request):
        username = request.POST.get("username")
        user = User.objects.filter(email=username)
        if user:
            # send email to user
            return render(request, "forgotpassword.html", {"message": "Password reset email sent"})
        if username is None:
            return render(request, "forgotpassword.html", {"message": "Please enter a username"})
        else:
            return render(request, "forgotpassword.html",
                          {"message": "User does not exist, please enter a valid username"})


class Home(View):
    def get(self, request, **kwargs):
        users = UserUtility.get_all_users()
        return render(request, "home.html", {"users": users})


class AccountBase(View):
    def get(self, request):
        current_user = User.objects.get(isLoggedIn=True)
        users = UserUtility.get_all_users()
        return render(request, "accountbase.html", {"users": users, "current_user": current_user})

    def post(self, request):
        # get value of method from within request.POST
        method = request.POST.get("method")

        # filterUser functionality
        if method == "filterUser":
            users = Users.filterUser(request.POST.get("position"))
            #  the isinstance function checks if the result variable contains an instance of the TypeError class
            if isinstance(users, ValueError):
                return render(
                    request,
                    "accountbase.html",
                    {"message": "You didn't select a User Type"},
                )
            return render(request, "accountbase.html", {"users": users})

        # searchUser functionality
        elif method == "searchUser":
            user = Users.searchUser(request.POST.get("search"))
            if isinstance(user, ValueError):
                return render(request, "accountbase.html", {"message": user})
            return render(request, "accountbase.html", {"users": user})

        # deleteUser functionality
        elif method == "deleteUser":
            username = request.POST.get("username")
            Supervisor.deleteUser(username)
            user = UserUtility.get_all_users()
            return render(request, "accountbase.html", {"users": user})


class CreateAccount(View):
    def get(self, request):
        return render(request, "createaccount.html")

    def post(self, request):
        result = Supervisor.create_account(
            request.POST.get("firstname"),
            request.POST.get("lastname"),
            request.POST.get("email"),
            request.POST.get("password"),
            request.POST.get("address"),
            request.POST.get("city"),
            request.POST.get("number"),
            request.POST.get("position"),
        )
        if isinstance(result, ValueError):
            return render(request, "createaccount.html", {"message": result})
        users = UserUtility.get_all_users()
        current_user = User.objects.get(isLoggedIn=True)
        return render(request, "accountbase.html", {"users": users, "current_user": current_user})


class EditAccount(View):
    def get(self, request, *args, **kwargs):
        id_search = kwargs["id"]
        user = User.objects.get(id=id_search)
        users = UserUtility.get_all_users()
        return render(request, "editaccount.html", {"user": user, "all_users": users})

    def post(self, request, **kwargs):
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        city = request.POST.get("city")
        phone = request.POST.get("phone_number")
        position = request.POST.get("position")
        id_search = kwargs["id"]
        userAccount = User.objects.get(id=id_search)

        Users.edit_account(
            userAccount,
            fname=firstname,
            lname=lastname,
            email=email,
            password=password,
            address=address,
            city=city,
            phone=phone,
            position=position,
        )
        current_user = User.objects.get(isLoggedIn=True)
        users = UserUtility.get_all_users()
        return render(request, "accountbase.html", {"users": users, "current_user": current_user})


class CourseBase(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, "course_base.html", {"courses": courses})

    def post(self, request):
        # courses = Course.objects.all()
        # if request.POST.get("course_code") in courses:
        #     course = Course.objects.get(request.POST.get("course_inst"))
        #     course.Course_Instructor = request.POST.get("course_inst")

        # result = Supervisor.create_course(
        #     request.POST.get("course_code"),
        #     request.POST.get("course_name"),
        #     request.POST.get("course_desc"),
        #     request.POST.get("course_inst"),
        #     request.POST.get("course_inst"),
        # )
        # if isinstance(result, TypeError):
        #     courses = Course.objects.all()
        #     users = UserUtility.get_all_users()
        #     return render(
        #         request,
        #         "createcourse.html",
        #         {"courses": courses, "users": users, "message": result}
        #     )
        # return render(request, "course_base.html", {"courses": courses})

        # button = request.POST.get("submit")
        #
        # Course.objects.get(Course_Code=)

        return render(request, "course_base.html")


class CreateCourse(View):
    def get(self, request):
        users = UserUtility.get_all_users()
        return render(request, "createcourse.html", {"users": users})

    def post(self, request):
        courses = Course.objects.all()

        result = Supervisor.create_course(
            request.POST.get("course_code"),
            request.POST.get("course_name"),
            request.POST.get("course_desc"),
            request.POST.get("course_inst"),
            request.POST.get("course_inst"),
        )
        if isinstance(result, TypeError):
            courses = Course.objects.all()
            users = UserUtility.get_all_users()
            return render(
                request,
                "createcourse.html",
                {"courses": courses, "users": users, "message": result}
            )
        return render(request, "course_base.html", {"courses": courses})

        # return render(request, "createcourse.html", {"success": "course created"})


class EditCourse(View):
    def get(self, request, **kwargs):
        course = Course.objects.get(Course_Code=kwargs["Course_Code"])
        users = UserUtility.get_all_users()

        return render(request, "courseedit.html", {"course": course, "users": users})

    def post(self, request, **kwargs):
        button = request.POST.get("button")
        courses = Course.objects.all()
        course = Course.objects.get(Course_Code=kwargs["Course_Code"])

        # If the user clicks on Delete Course button
        if button == "Delete Course":
            Supervisor.delete_course(course)

        else:
            result = Supervisor.edit_course(
                course,
                request.POST.get("course_code"),
                request.POST.get("course_name"),
                request.POST.get("course_desc"),
                request.POST.get("course_inst"),
                request.POST.get("course_inst_method"),
            )
            if isinstance(result, TypeError):
                courses = Course.objects.all()
                users = UserUtility.get_all_users()
                return render(
                    request,
                    "createsection.html",
                    {"courses": courses, "users": users, "message": result}
                )

        return render(request, "course_base.html", {"courses": courses})


class viewSection(View):
    def get(self, request,**kwargs):
        course = Course.objects.get(Course_Code=kwargs["Course_Code"])
        section=Section.objects.filter(Sec_Course=course).all()
        return render(request, "coursesection.html",{"sections": section})


class createSection(View):
    def get(self, request):
        course = Course.objects.all()
        users = UserUtility.get_all_users()
        return render(request, "createsection.html", {"courses": course, "users": users})

    def post(self, request):
        course = Course.objects.all()
        users = UserUtility.get_all_users()

        result = Supervisor.create_section(request.POST.get("section_name"), request.POST.get("course"),
                                           request.POST.get("section_inst"), datetime.datetime)
        if isinstance(result, ValueError):
            courses = Course.objects.all()
            users = UserUtility.get_all_users()
            return render(
                request,
                "createsection.html",
                {"courses": courses, "users": users, "message": result}
            )

        return render(request, "course_base.html", {"courses": course})


class ViewPersonalInformation(View):
    def get(self, request, **kwargs):
        id_search = kwargs["id"]
        user = User.objects.get(id=id_search)
        return render(request, "personal_information.html", {"user": user})
