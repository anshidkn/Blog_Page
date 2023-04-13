from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from page.models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        # exclude=("user")
        fields=('title','description','user','image')
        widgets={
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "image":forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            "user":forms.TextInput(attrs={'class':'form-control','value':'','id':'usr','type':'hidden'})
            # "user": forms.HiddenInput(),
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model=Comment 
        fields=('comment',)
        widgets={
            "comment": forms.Textarea(attrs={'class': 'form-control'}),

        }