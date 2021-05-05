from django.test import TestCase
from django.urls import reverse
from ..models import Course
from ..forms import SearchForm


class TestViews(TestCase):

    def setUp(self):
        self.course = Course.objects.create(name='first_course', lectures_amount=5)
        self.list_url = reverse('catalog:course_list')
        self.detail_url = reverse('catalog:course_detail', args=[self.course.id, self.course.slug])
        self.search_url = reverse('catalog:course_search')

    def test_course_list(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/course/list.html')

    def test_course_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/course/detail.html')

    def test_course_search(self):
        response = self.client.get(self.search_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/course/search.html')

