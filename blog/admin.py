from .models import Post, PostCatagory
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
            'published',
            'catagories',
        ]

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    readonly_fields = ('updated_at', 'slug')

class PostCatagoryAdminForm(forms.ModelForm):
    catagory_name = forms.CharField()

    class Meta:
        model = PostCatagory
        fields = [
            'catagory_name',
        ]

class PostCatagoryAdmin(admin.ModelAdmin):
    form = PostCatagoryAdminForm

admin.site.register(Post, PostAdmin)
admin.site.register(PostCatagory, PostCatagoryAdmin)