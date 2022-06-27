from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import AboutPageView, HomePageView


class HomePageTests(SimpleTestCase):

    def setUp(self) -> None:
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_urls(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):

    def setUp(self) -> None:
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_urls(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_correct_html(self):
        self.assertContains(self.response, 'About')

    def test_aboutpage_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
