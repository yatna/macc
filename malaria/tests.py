from django.contrib.auth.models import User
from django.test import TestCase
from malaria.models import Post, RevPost
from malaria.services import create_revpost, delete_post_by_id, get_post_by_id
from webhub.models import Pcuser


class MalariaTests(TestCase):

    def setUp(self):
        """Setup the test database"""

        self.u1 = User.objects.create_superuser(username='admin',
                                                password='password',
                                                email='')

        self.u1.save()

        self.o1 = Pcuser(user=self.u1)
        self.o1.save()

        self.p1 = Post(owner=self.o1,
                       title_post="Title 1",
                       description_post="Description 1")

        self.p2 = Post(owner=self.o1,
                       title_post="Title 2",
                       description_post="Description 2")

        self.p3 = Post(owner=self.o1,
                       title_post="Title 3",
                       description_post="Description 3")

        self.p1.save()
        self.p2.save()
        self.p3.save()

    def test_create_revpost(self):

        revpost = create_revpost(self.o1,
                                 self.p1,
                                 self.p1.title_post,
                                 self.p1.description_post)

        self.assertIsNotNone(revpost)
        self.assertEqual(RevPost.objects.get(pk=revpost.id), revpost)
        self.assertEqual(revpost.owner_rev, self.o1)
        self.assertEqual(revpost.owner_rev_post, self.p1)
        self.assertEqual(revpost.title_post_rev, self.p1.title_post)
        self.assertEqual(revpost.description_post_rev, self.p1.description_post)
        self.assertEqual(revpost.title_change, True)
        self.assertEqual(revpost.description_change, True)

        revpost = create_revpost(self.o1,
                                 self.p2,
                                 self.p2.title_post,
                                 self.p2.description_post)

        self.assertIsNotNone(revpost)
        self.assertEqual(RevPost.objects.get(pk=revpost.id), revpost)
        self.assertEqual(revpost.owner_rev, self.o1)
        self.assertEqual(revpost.owner_rev_post, self.p2)
        self.assertEqual(revpost.title_post_rev, self.p2.title_post)
        self.assertEqual(revpost.description_post_rev, self.p2.description_post)
        self.assertEqual(revpost.title_change, True)
        self.assertEqual(revpost.description_change, True)

        revpost = create_revpost(self.o1,
                                 self.p3,
                                 self.p3.title_post,
                                 self.p3.description_post)

        self.assertIsNotNone(revpost)
        self.assertEqual(RevPost.objects.get(pk=revpost.id), revpost)
        self.assertEqual(revpost.owner_rev, self.o1)
        self.assertEqual(revpost.owner_rev_post, self.p3)
        self.assertEqual(revpost.title_post_rev, self.p3.title_post)
        self.assertEqual(revpost.description_post_rev, self.p3.description_post)
        self.assertEqual(revpost.title_change, True)
        self.assertEqual(revpost.description_change, True)

        revpost = create_revpost(None,
                                 self.p1,
                                 self.p1.title_post,
                                 self.p1.description_post)

        self.assertIsNone(revpost)

        revpost = create_revpost(self.o1,
                                 None,
                                 self.p1.title_post,
                                 self.p1.description_post)

        self.assertIsNone(revpost)

        revpost = create_revpost(self.o1,
                                 self.p1,
                                 None,
                                 self.p1.description_post)

        self.assertIsNone(revpost)

        revpost = create_revpost(self.o1,
                                 self.p1,
                                 self.p1.title_post,
                                 None)

        self.assertIsNone(revpost)

        revpost = create_revpost(None,
                                 self.p1,
                                 self.p1.title_post,
                                 None)

        self.assertIsNone(revpost)

        revpost = create_revpost(self.o1,
                                 None,
                                 self.p1.title_post,
                                 None)

        self.assertIsNone(revpost)

        revpost = create_revpost(self.o1,
                                 None,
                                 None,
                                 None)

        self.assertIsNone(revpost)

        revpost = create_revpost(None,
                                 None,
                                 None,
                                 self.p1.description_post)

        self.assertIsNone(revpost)

        revpost = create_revpost(None,
                                 None,
                                 None,
                                 None)

        self.assertIsNone(revpost)

    def test_delete_post_by_id(self):

        self.assertTrue(delete_post_by_id(self.p1.id))
        self.assertTrue(delete_post_by_id(self.p2.id))
        self.assertTrue(delete_post_by_id(self.p3.id))

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

        post = get_post_by_id(self.p1.id)
        self.assertIsNotNone(post)
        self.assertEqual(post, self.p1)
        self.assertEqual(post.id, self.p1.id)
        self.assertEqual(post.owner, self.p1.owner)
        self.assertEqual(post.title_post, self.p1.title_post)
        self.assertEqual(post.description_post, self.p1.description_post)

        post = get_post_by_id(self.p2.id)
        self.assertIsNotNone(post)
        self.assertEqual(post, self.p2)
        self.assertEqual(post.id, self.p2.id)
        self.assertEqual(post.owner, self.p2.owner)
        self.assertEqual(post.title_post, self.p2.title_post)
        self.assertEqual(post.description_post, self.p2.description_post)

        post = get_post_by_id(self.p3.id)
        self.assertIsNotNone(post)
        self.assertEqual(post, self.p3)
        self.assertEqual(post.id, self.p3.id)
        self.assertEqual(post.owner, self.p3.owner)
        self.assertEqual(post.title_post, self.p3.title_post)
        self.assertEqual(post.description_post, self.p3.description_post)

        self.assertIsNone(get_post_by_id(-999999))
        self.assertIsNone(get_post_by_id(-1))
        self.assertIsNone(get_post_by_id(100))
        self.assertIsNone(get_post_by_id(200))
        self.assertIsNone(get_post_by_id(300))
        self.assertIsNone(get_post_by_id(999))
        self.assertIsNone(get_post_by_id(999999))

        self.assertNotEqual(get_post_by_id(-999999), self.p1)
        self.assertNotEqual(get_post_by_id(-1), self.p1)
        self.assertNotEqual(get_post_by_id(100), self.p1)
        self.assertNotEqual(get_post_by_id(200), self.p1)
        self.assertNotEqual(get_post_by_id(300), self.p1)
        self.assertNotEqual(get_post_by_id(999), self.p1)
        self.assertNotEqual(get_post_by_id(999999), self.p1)

        self.assertNotEqual(get_post_by_id(-999999), self.p2)
        self.assertNotEqual(get_post_by_id(-1), self.p2)
        self.assertNotEqual(get_post_by_id(100), self.p2)
        self.assertNotEqual(get_post_by_id(200), self.p2)
        self.assertNotEqual(get_post_by_id(300), self.p2)
        self.assertNotEqual(get_post_by_id(999), self.p2)
        self.assertNotEqual(get_post_by_id(999999), self.p2)

        self.assertNotEqual(get_post_by_id(-999999), self.p3)
        self.assertNotEqual(get_post_by_id(-1), self.p3)
        self.assertNotEqual(get_post_by_id(100), self.p3)
        self.assertNotEqual(get_post_by_id(200), self.p3)
        self.assertNotEqual(get_post_by_id(300), self.p3)
        self.assertNotEqual(get_post_by_id(999), self.p3)
        self.assertNotEqual(get_post_by_id(999999), self.p3)

        self.assertNotEqual(get_post_by_id(self.p1.id), self.p2)
        self.assertNotEqual(get_post_by_id(self.p1.id), self.p3)

        self.assertNotEqual(get_post_by_id(self.p2.id), self.p1)
        self.assertNotEqual(get_post_by_id(self.p2.id), self.p3)

        self.assertNotEqual(get_post_by_id(self.p3.id), self.p1)
        self.assertNotEqual(get_post_by_id(self.p3.id), self.p2)
