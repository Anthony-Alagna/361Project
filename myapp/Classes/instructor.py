from myapp.models import User, Course
from myapp.Classes.users import Users


class Instructor(Users):
    @staticmethod
    def get_assignments(instructor):
        courses = Course.objects.all()
        inst_courses = []
        for c in courses:
            if c.Course_Instructor == instructor:
                inst_courses.append(instructor)
        return inst_courses
