from django.forms import ModelForm
from django import forms
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
      model = Profile
      exclude = ['user']
      widgets = {
        'image': forms.FileInput(attrs={'class': 'form-control'}),
        'info': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Summary about yourself', 'class': 'form-control'})
      }