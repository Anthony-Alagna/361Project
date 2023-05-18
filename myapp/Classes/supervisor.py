from myapp.models import User, Course
from myapp.Classes.users import Users


class Supervisor(Users):
    @staticmethod
    def create_account(
        first_name, last_name, email, password, address, city, phone, account_type
    ):
        users = User.objects.all()
        for user in users:
            if user.email == email:
                return ValueError(
                    "That username already exists - please choose another"
                )

        if (
            first_name == ""
            or last_name == ""
            or email == ""
            or password == ""
            or address == ""
            or city == ""
            or phone == ""
            or account_type == ""
        ):
            return ValueError("You're missing a field - please fill in all fields")

        else:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                address=address,
                city=city,
                phone_number=phone,
                positions=account_type,
            )
            return user

    @staticmethod
    def create_course(code, name, desc, inst, inst_method):
        courses = Course.objects.all()
        for course in courses:
            if course.Course_Code == code:
                return TypeError("A course with that code already exists!")
        if code == "":
            return TypeError("Course code cannot be blank!")
        elif name == "":
            return TypeError("Course name cannot be blank!")
        elif desc == "":
            return TypeError("Course description cannot be blank!")
        return Course.objects.create(
            Course_Code=code,
            Course_Name=name,
            Course_Description=desc,
            Course_Instructor=inst,
            Course_Instruction_Method=inst_method,
        )

    @staticmethod
    def edit_course(course, code, name, desc, inst, inst_method):
        courses = Course.objects.all()

        # Check if code from input is not the same as old code
        if code != course.Course_Code:
            for c in courses:
                if c.Course_Code == code:
                    return TypeError("A course with that code already exists!")

        if code == "":
            return TypeError("Course code cannot be blank!")
        elif name == "":
            return TypeError("Course name cannot be blank!")
        elif desc == "":
            return TypeError("Course description cannot be blank!")

        course.Course_Code = code
        course.Course_Name = name
        course.Course_Description = desc
        course.Course_Instructor = inst
        course.Course_Instruction_Method = inst_method
        course.save()

    @staticmethod
    def delete_course(course):
        course.delete()

    def deleteUser(username):
        user = User.objects.filter(email=username)
        user.delete()
