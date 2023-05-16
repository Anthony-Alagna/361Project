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
        users = UserUtility.get_all_users()
        return render(request, "accountbase.html", {"users": users})

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
        return render(request, "accountbase.html", {"users": users})


class EditAccount(View):
    def get(self, request, *args, **kwargs):
        id_search = kwargs["id"]
        user = User.objects.get(id=id_search)
        return render(request, "editaccount.html", {"user": user})


class CourseBase(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, "course_base.html", {"courses": courses})

    def post(self, request):
        courses = Course.objects.all()
        result = Supervisor.create_course(
            request.POST.get("course_code"),
            request.POST.get("course_name"),
            request.POST.get("course_desc"),
            request.POST.get("course_inst"),
        )
        if isinstance(result, TypeError):
            courses = Course.objects.all()
            users = UserUtility.get_all_users()
            return render(
                request,
                "createcourse.html",
                {"courses": courses, "users": users, "message": result},
            )
        return render(request, "course_base.html", {"courses": courses})


class CreateCourse(View):
    TEMPLATE = "createcourse.html"

    def get(self, request):
        users = UserUtility.get_all_users()
        return render(request, "createcourse.html", {"users": users})

    def post(self, request):
        return render(request, "createcourse.html", {"success": "course created"})


class EditCourse(View):
    def get(self, request, *args, **kwargs):
        c_code = kwargs["Course_Code"]
        course = Course.objects.get(Course_Code=c_code)
        users = UserUtility.get_all_users()

        return render(request, "courseedit.html", {"course": course, "users": users})

    def post(self, request, *args, **kwargs):
        course_code = kwargs["Course_Code"]
        actCourse = Course.objects.get(Course_Code=course_code)
        users = UserUtility.get_all_users()

        courses = Course.objects.all()
        res = request.POST
        made_instructor = request.POST.get("course_inst")
        first_name = made_instructor.split()
        inst = actCourse.Course_Instructor

        if "delete_user" in res:
            if inst == "":
                return render(
                    request,
                    "courseedit.html",
                    {
                        "message": "no instructor to remove",
                        "courses": courses,
                        "users": users,
                    },
                )
            else:
                actCourse = Supervisor.removeInstructorFromClass(
                    inst, course_code)
                return render(
                    request,
                    "courseedit.html",
                    {
                        "message": "Instructor has been removed from the course",
                        "course": actCourse,
                        "users": users,
                    },
                )
        elif "save_ch" in res:
            if made_instructor == "":
                actCourse.save()
                courses = Course.objects.all()
                return render(request, "course_base.html", {"courses": courses})
            elif first_name == actCourse.Course_Instructor:
                return render(
                    request,
                    "courseedit.html",
                    {
                        "message": "Instructor is already assigned to this course",
                        "course": actCourse,
                        "users": users,
                    },
                )
            else:
                prof = User.objects.get(User_fName=first_name[0])
                # have to set act courses = to it becauuse it returned in addINstructor
                actCourse = Supervisor.addInstructor(
                    prof.User_fName, course_code)
                user = User.objects.all()
                return render(
                    request,
                    "course_base.html",
                    {
                        "message": "instructor has successfully changed",
                        "courses": courses,
                        "user": user,
                    },
                )


class ViewPersonalInformation(View):
    def get(self, request, **kwargs):
        id_search = kwargs["id"]
        user = User.objects.get(id=id_search)
        return render(request, "personal_information.html", {"user": user})

    def post(self, request):
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone_number")
        address = request.POST.get("address")
        position = request.POST.get("position")
        userAccount = Users.getUserByUsername(request.session["username"])

        Users.editInfo(
            userAccount,
            fname=firstname,
            lname=lastname,
            email=email,
            phone=phone,
            address=address,
            position=position,
        )
        return render(
            request, "personal_information.html", {
                "success": "information updated"}
        )

class ContactMembers(View):
    def get(selfself, request):
        return render(request, "contact_members.html")

    def post(self, request):
        return render(request, "contact_members.html")