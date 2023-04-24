import myapp.models
from myapp.models import Course


class CourseUtility:
    @staticmethod
    def get_course_list():
        return Course.objects.all()
