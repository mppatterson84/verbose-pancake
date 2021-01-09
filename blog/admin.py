from .models import Post, PostCategory
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(
        label='Post Body',
        required=True,
        widget=CKEditorUploadingWidget()
    )

    categories = forms.ModelMultipleChoiceField(
        queryset=PostCategory.objects.all(),
        required=False,
        # initial=PostCategory.objects.all()[:1]
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
            'categories',
        ]


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    readonly_fields = ('created_at', 'updated_at', 'slug')


class PostCategoryAdminForm(forms.ModelForm):
    category_name = forms.CharField()

    class Meta:
        model = PostCategory
        fields = [
            'category_name',
        ]


class PostCategoryAdmin(admin.ModelAdmin):
    form = PostCategoryAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
