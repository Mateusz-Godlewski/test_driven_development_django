from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.


class BadTest(TestCase):

    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve("/")
    #     self.assertEqual(found.func, home_page)
    #
    #
    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode("utf8")
    #     expected_html = render_to_string("home.html")
    #     self.assertEqual(html, expected_html)
    #
    #
    # def test_using_django_client_to_check_if_returns_correct_html(self):
    #     response = self.client.get("/")
    #
    #     html = response.content.decode("utf8")
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.endswith('</html>'))
    #
    #     self.assertTemplateUsed(response, "home.html")


    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")