from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1',
            password='abc123'
        )
        testuser1.save()

        # Create a blog post
        test_post = Post.objects.create(
            title='Blog Title',
            body='Body content...',
            author=testuser1,
            published=True
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        expected_author = f'{post.author}'
        expected_slug = f'{post.slug}'
        expected_published = f'{post.published}'
        expected_category = f'{post.categories}'
        self.assertEqual(expected_title, 'Blog Title')
        self.assertEqual(expected_body, 'Body content...')
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_slug, 'blog-title')
        self.assertEqual(expected_published, 'True')