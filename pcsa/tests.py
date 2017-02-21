from django.contrib.auth.models import User
from django.test import TestCase
from pcsa.views import (delete_post_by_id,
                        get_post_by_id)


from pcsa.models import PcsaPost
from signup.models import Pcuser

# Create your tests here.

class PcsaTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_superuser(username='admin',
                                                password='password',
                                                email='')

        self.user2 = User.objects.create_superuser(username='admin2',
                                                password='password2',
                                                email='')

        self.user1.save()
        self.user2.save()

        self.o1 = Pcuser(user=self.user1)
        self.o2 = Pcuser(user=self.user2)

        self.o1.save()
        self.o2.save()

        self.post1 = PcsaPost(owner=self.o1,
                       title="Title 1",
                       description="Description 1")

        self.post2 = PcsaPost(owner=self.o2,
                       title="Title 2",
                       description="Description 2")

        self.post3 = PcsaPost(owner=self.o1,
                       title="Title 3",
                       description="Description 3")

        self.post4 = PcsaPost(owner=self.o2,
                       title="Title 4",
                       description="Description 4")

        self.post5 = PcsaPost(owner=self.o1,
                       title="Title 5",
                       description="Description 5")

        self.post1.save()
        self.post2.save()
        self.post3.save()
        self.post4.save()
        self.post5.save()



    def test_delete_post_by_id(self):

        self.assertTrue(delete_post_by_id(self.post1.id))
        self.assertTrue(delete_post_by_id(self.post2.id))
        self.assertTrue(delete_post_by_id(self.post3.id))

        self.assertFalse(delete_post_by_id(-999999))
        self.assertFalse(delete_post_by_id(-1))
        self.assertFalse(delete_post_by_id(100))
        self.assertFalse(delete_post_by_id(200))
        self.assertFalse(delete_post_by_id(300))
        self.assertFalse(delete_post_by_id(400))
        self.assertFalse(delete_post_by_id(500))
        self.assertFalse(delete_post_by_id(600))
        self.assertFalse(delete_post_by_id(999))
        self.assertFalse(delete_post_by_id(999999))

    def test_get_post_by_id(self):

       post = get_post_by_id(self.post1.id)
       self.assertIsNotNone(post)
       self.assertEqual(post, self.post1)
       self.assertEqual(post.id, self.post1.id)
       self.assertEqual(post.owner, self.post1.owner)
       self.assertEqual(post.title, self.post1.title)
       self.assertEqual(post.description, self.post1.description)

       post = get_post_by_id(self.post2.id)
       self.assertIsNotNone(post)
       self.assertEqual(post, self.post2)
       self.assertEqual(post.id, self.post2.id)
       self.assertEqual(post.owner, self.post2.owner)
       self.assertEqual(post.title, self.post2.title)
       self.assertEqual(post.description, self.post2.description)

       post = get_post_by_id(self.post3.id)
       self.assertIsNotNone(post)
       self.assertEqual(post, self.post3)
       self.assertEqual(post.id, self.post3.id)
       self.assertEqual(post.owner, self.post3.owner)
       self.assertEqual(post.title, self.post3.title)
       self.assertEqual(post.description, self.post3.description)

       self.assertIsNone(get_post_by_id(-999999))
       self.assertIsNone(get_post_by_id(-1))
       self.assertIsNone(get_post_by_id(100))
       self.assertIsNone(get_post_by_id(200))
       self.assertIsNone(get_post_by_id(300))
       self.assertIsNone(get_post_by_id(999))
       self.assertIsNone(get_post_by_id(999999))

       self.assertNotEqual(get_post_by_id(-999999), self.post1)
       self.assertNotEqual(get_post_by_id(-1), self.post1)
       self.assertNotEqual(get_post_by_id(100), self.post1)
       self.assertNotEqual(get_post_by_id(200), self.post1)
       self.assertNotEqual(get_post_by_id(300), self.post1)
       self.assertNotEqual(get_post_by_id(999), self.post1)
       self.assertNotEqual(get_post_by_id(999999), self.post1)

       self.assertNotEqual(get_post_by_id(-999999), self.post2)
       self.assertNotEqual(get_post_by_id(-1), self.post2)
       self.assertNotEqual(get_post_by_id(100), self.post2)
       self.assertNotEqual(get_post_by_id(200), self.post2)
       self.assertNotEqual(get_post_by_id(300), self.post2)
       self.assertNotEqual(get_post_by_id(999), self.post2)
       self.assertNotEqual(get_post_by_id(999999), self.post2)

       self.assertNotEqual(get_post_by_id(-999999), self.post3)
       self.assertNotEqual(get_post_by_id(-1), self.post3)
       self.assertNotEqual(get_post_by_id(100), self.post3)
       self.assertNotEqual(get_post_by_id(200), self.post3)
       self.assertNotEqual(get_post_by_id(300), self.post3)
       self.assertNotEqual(get_post_by_id(999), self.post3)
       self.assertNotEqual(get_post_by_id(999999), self.post3)

       self.assertNotEqual(get_post_by_id(self.post1.id), self.post2)
       self.assertNotEqual(get_post_by_id(self.post1.id), self.post3)

       self.assertNotEqual(get_post_by_id(self.post2.id), self.post1)
       self.assertNotEqual(get_post_by_id(self.post2.id), self.post3)

       self.assertNotEqual(get_post_by_id(self.post3.id), self.post1)
       self.assertNotEqual(get_post_by_id(self.post3.id), self.post2)
