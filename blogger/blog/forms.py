from django import forms
from . import models



class CreateBlogPost(forms.ModelForm):
    
    class Meta:
        model = models.BlogPost
        fields = ["title","slug","content","author","thumb"]
