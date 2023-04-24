import myapp.models
from myapp.models import Course


class CourseUtility:
    @staticmethod
    def create_course(code, name, desc, inst):
        courses = CourseUtility.get_course_list()
        for course in courses:
            if course.Course_Code == code:
                return TypeError("A course with that code already exists!")
        if code is "":
            return TypeError("Course code cannot be blank!")
        elif name is "":
            return TypeError("Course name cannot be blank!")
        elif desc is "":
            return TypeError("Course description cannot be blank!")
        Course.objects.create(Course_Code=code, Course_Name=name, Course_Description=desc, Course_Instructor=inst)

    @staticmethod
    def get_course_list():
        return Course.objects.all()
