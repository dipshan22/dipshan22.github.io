from django import forms
from . models import Books



class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=35)
    age = forms.IntegerField()

class BooksModelForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"