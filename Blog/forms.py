from django import forms
from pagedown.widgets import PagedownWidget
from .models import Blog

class BlogForm(forms.ModelForm):
    description1 = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Blog
        fields = ["description1"]
