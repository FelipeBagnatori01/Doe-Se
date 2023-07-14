from django.forms import ModelForm
from django import forms
from .models import Post

class UploadForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":"8"}), label='')
    image = forms.ImageField(required = False, label='')
    class Meta:
        model = Post
        fields = ['text', 'image']