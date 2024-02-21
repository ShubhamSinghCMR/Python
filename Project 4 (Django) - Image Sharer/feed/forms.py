from django import forms

class PostForm(forms.Form):
    text=forms.CharField(label="Image Caption")
    image=forms.ImageField(label="Select Image")
    description = forms.CharField(label="Story behind it", widget=forms.Textarea)
    