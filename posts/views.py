from django.shortcuts import render
from django.views.generic import ListView
from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your views here.




class HomePage(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'all_posts'


class AboutPage(ListView):
    template_name = 'about.html'


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')