from django import forms
from django.forms import ModelForm
from .models import Blog


class BlogForm(forms.ModelForm):
    """Form definition for Blog."""

    class Meta:
        """Meta definition for Blogform."""

        model = Blog
        fields = '__all__'
