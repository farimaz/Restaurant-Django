from django import forms

class CommentForms(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=200)
    massage = forms.CharField(widget=forms.Textarea)