from django import forms
from captcha.fields import ReCaptchaField
from .models import Comment

class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ['author', 'content', 'captcha', 'parent_comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add the 'form-control' class to the widget of the 'content' field
        self.fields['author'].widget.attrs.update({'class': 'form-control disabled'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'cols': 30, 'rows': 5})

        # Hide the parent_comment field for top-level comments
        self.fields['parent_comment'].widget = forms.HiddenInput()
        self.fields['parent_comment'].required = False
