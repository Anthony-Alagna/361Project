import myapp.models
from myapp.models import Course


class CourseUtility:
    @staticmethod
    def create_course(name, code, desc):
        if name is "" or code is "" or desc is "":
            return TypeError("missing field")
        else:
            Course.objects.create(Course_Name=name, Course_Code=code, Course_Description=desc)

    @staticmethod
    def get_course_list():
        return Course.objects.all()
