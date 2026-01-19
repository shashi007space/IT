from django import forms
from .models import Platform, Link, Folder


class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name', 'logo']


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['platform', 'name']


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'url', 'platform', 'folder']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Link title'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'platform': forms.Select(attrs={'class': 'form-control'}),
            'folder': forms.Select(attrs={'class': 'form-control'}),
        }
