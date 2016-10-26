from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'desc')


class PhotoForm(forms.Form):
    title = forms.CharField(max_length=30)
    desc = forms.CharField(max_length=80, required=False)
    img = forms.ImageField(max_length=100)
