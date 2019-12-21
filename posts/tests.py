from django.test import TestCase
from django.urls import reverse, resolve
from .views import *
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post


class TestPosts(TestCase):

    def test_post_status_code(self):
        url = reverse('testimonials')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_resolves_post_view(self):
        view = resolve('/')
        self.assertEqual(view.func, list_testimonials)


class TestAPICreate(APITestCase):
    def test_create(self):
        url = reverse('api-list-testimonials')
        data = {'name': 'API_test_user', 'post': 'post created via API'}
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Post.objects.get().name, 'API_test_user')



