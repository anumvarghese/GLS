from django.test import TestCase

# Create your tests here.

from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from app.views import home

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home(request) 
        html = response.content.decode('utf8') 
        self.assertIn('GLS', html)
        self.assertEqual(response.status_code, 200)  


