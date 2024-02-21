from django import forms

class PostForm(forms.Form):
    text=forms.CharField()
    image=forms.ImageField()
    description = forms.CharField(widget=forms.Textarea)
    