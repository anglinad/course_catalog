from django.test import TestCase
from ..forms import SearchForm


class TestForms(TestCase):

    def setUp(self):
        self.form = SearchForm(data={'query': 'test'})

    def test_search_form_valid_data(self):
        self.assertTrue(self.form.is_valid())

    def test_search_form_no_data(self):
        form = SearchForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
