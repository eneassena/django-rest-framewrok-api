from django.test import TestCase

from django.contrib.auth.models import User
from .models import Post

# Create your tests here.


class BlogTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):

        # criando um usuário
        testuser1: User = User.objects.create(
            username='testusuario1', password='123abc'
        )
        testuser1.save()

        # criando um blog post
        post_context: Post = Post.objects.create(
            author=testuser1, title='Blog Title', body='lorem lorem lorem'
        )
        post_context.save()

    def test_blog_content(self):
        post: Post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEquals(author, 'testusuario1')
        self.assertEquals(title, 'Blog Title')
        self.assertEquals(body, 'lorem lorem lorem')
