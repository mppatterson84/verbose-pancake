from .models import Post
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

class PostAdminForm(forms.ModelForm):
    body = forms.CharField(
        label='Post Body',
        required=True,
        widget=CKEditorWidget()
    )
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'author',
            'created_at',
            'updated_at',
            'slug',
        ]

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    readonly_fields = ('updated_at', 'slug')

admin.site.register(Post, PostAdmin)