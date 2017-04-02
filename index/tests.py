from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest, HttpResponse

from index.views import index_index


# Create your tests here.
class indexTest(TestCase):
    def test_root_url_resolves_to_index_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index_index)

    def test_root_url_return_the_right_html(self):
        request = HttpRequest()
        response = index_index(request)
        self.assertIn(bytes('<title>大学图书管理系统</title>', 'utf-8'), response.content)

