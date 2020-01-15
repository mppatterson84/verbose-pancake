from django.db import models
from datetime import datetime
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(default=datetime.now, blank=False)
    slug = models.SlugField(unique=False, blank=True, default='slug')
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField('blog.PostCategory')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.updated_at = datetime.now()
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post-detail', kwargs={'pk': self.pk, 'slug': self.slug})

class PostCategory(models.Model):
    category_name = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(unique=False, blank=True, default='slug')

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(PostCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Post Categories"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('category-detail', kwargs={'slug': self.slug,})