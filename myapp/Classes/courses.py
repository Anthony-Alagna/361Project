import myapp.models
from myapp.models import Section, CourseToUser


class Course:
    course_id = None
    name = None
    code = None
    instructor = None

    def __init__(self, course_id, name, code, instructor):
        self.course_id = course_id
        self.name = name
        self.code = code
        self.instructor = instructor

    def get_name(self):
        return self.name

    def set_name(self, _name):
        self.name = _name

    def get_code(self):
        return self.code

    def set_code(self, _code):
        self.code = _code

    def get_instructor(self):
        return self.instructor

    def set_instructor(self, _instructor):
        self.instructor = _instructor
