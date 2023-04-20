import myapp.models
from myapp.models import Course, Section, CourseToUser

class Course:
    def __init__(self, courseID, name, code, instructor, ta_list):
        self.courseID = courseID  # TODO Do we need this?
        self.name = name
        self.code = code
        self.instructor = instructor
        self.ta_list = ta_list

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

    # TODO how to make a setter for a list?
    def get_ta(self):
        return self.ta_list

    def set_ta(self, _ta_list):
        self.ta_list = _ta_list
