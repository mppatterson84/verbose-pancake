from django import forms
from blog.models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='', 
        required=True, 
        widget=forms.TextInput(
            attrs={
                "placeholder": "Post Title", 
                "class": "form-control"
            }
        )
    )

    body = forms.CharField(
        label='',
        required=True,
        widget=CKEditorWidget()
    )

    published = forms.CharField(
        label='Published',
        required=False,
        widget=forms.CheckboxInput()
    )
    
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'published',
        ]