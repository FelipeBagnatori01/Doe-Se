from django.forms import ModelForm
from django import forms
from django.db import models
from .models import Post
from django.contrib.auth import get_user_model

class UploadForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":"8"}), label='')
    image = forms.ImageField(required = False, label='')
    class Meta:
        model = Post
        fields = ['text', 'image']