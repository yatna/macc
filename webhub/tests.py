from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APITestCase
from webhub.models import Pcuser, Post
from webhub.serializers import PostSerializer

class PostAPITestCase(APITestCase):

    def setUp(self):

        u1 = User.objects.create_superuser(username='admin', password='password', email='')
        u1.save()

        o1 = Pcuser(user = u1)
        o1.save()

        p1 = Post(owner = o1,
                title_post = "Title 1",
                description_post = "Description 1")

        p2 = Post(owner = o1,
                title_post = "Title 2",
                description_post = "Description 2")

        p3 = Post(owner = o1,
                title_post = "Title 3",
                description_post = "Description 3")

        p1.save()
        p2.save()
        p3.save()

        #authenticate
        self.client.login(username='admin', password='password')

    def test_detail_positive_cases(self):
        
        post_list = Post.objects.all().order_by('id')

        for post in post_list:

            post_id = str(post.id)
            serializer = PostSerializer(post)
            content = JSONRenderer().render(serializer.data)

            #name of viewset is post-detail
            url = reverse('post-detail', args=[post_id])
            response = self.client.get(url)

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.accepted_media_type, 'application/json')
            self.assertEqual(response.render().content, content)

    def test_list_delete_cases(self):
        
        url = reverse('post-list')
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_list_head_cases(self):

        url = reverse('post-list')
        response = self.client.head(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_options_cases(self):

        url = reverse('post-list')
        response = self.client.options(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_post_cases(self):
        
        url = reverse('post-list')

        data = {'owner' : 1,
            'title_post' : 'Test 1',
            'description_post' : 'Test 1',
            'created' : datetime.now(),
            'updated' : datetime.now(),
            'id' : '1'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        data = {'owner' : 1,
            'title_post' : 'Test 2',
            'description_post' : 'Test 2',
            'created' : datetime.now(),
            'updated' : datetime.now(),
            'id' : '2'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        data = {'owner' : 1,
            'title_post' : 'Test 3',
            'description_post' : 'Test 3',
            'created' : datetime.now(),
            'updated' : datetime.now(),
            'id' : '3'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_list_put_cases(self):

        url = reverse('post-list')

        data = {'owner' : 1,
            'title_post' : 'Test 1',
            'description_post' : 'Test 1',
            'created' : datetime.now(),
            'updated' : datetime.now(),
            'id' : '1'}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        data = {'owner' : 1,
            'title_post' : 'Test 2',
            'description_post' : 'Test 2',
            'created' : datetime.now(),
            'updated' : datetime.now(),
            'id' : '2'}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        data = {'owner' : 1,
            'title_post' : 'Test 3',
            'description_post' : 'Test 3',
            'created' : datetime.now(),
            'updated' : datetime.now(),
            'id' : '3'}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_list_unauthenticated_cases(self):

        self.client.force_authenticate(user=None)
        url = reverse('post-list')

        data = {'owner' : 1,
            'title_post' : 'Test 1',
            'description_post' : 'Test 1',
            'created' : datetime.now(),
            'updated' : datetime.now(),
            'id' : '1'}

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.head(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.options(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        #unauthenticate
        self.client.force_authenticate(user=None)
