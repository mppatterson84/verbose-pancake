from django.utils.text import slugify


def slug_logic(self, i):
    from blog.models import Post
    i += 1
    slug_filter = Post.objects.filter(slug__exact=self.slug)
    if len(slug_filter) > 0:
        if not slug_filter[0].pk == self.pk:
            self.slug = f"{slugify(self.title)}-{len(slug_filter)+i}"
            slug_logic(self, i)


def get_unique_slug(self):
    self.slug = slugify(self.title)
    i = 0
    slug_logic(self, i)
