from django.test import TestCase
from django.urls import reverse
from ..models import Course


class TestCourseModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.obj_id = Course.objects.create(name='first_course', lectures_amount=5).pk

    def test_course_str_method(self):
        course = Course.objects.get(id=self.obj_id)
        self.assertTrue(isinstance(course, Course))
        self.assertEqual(course.__str__(), course.name)

    def test_course_get_absolute_url(self):
        course = Course.objects.get(id=self.obj_id)
        first_course_url = f"/{course.id}/{course.slug}/"
        self.assertEqual(first_course_url, course.get_absolute_url())
