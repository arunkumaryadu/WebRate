from django.forms import ModelForm
from website.models import Comment
from django import forms
from django import forms


class commentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ['coment']
        widgets={'coment': forms.Textarea(attrs={'rows':2, 'cols':55}),}

class editForm(ModelForm):
    class Meta():
        model=Comment
        fields=['coment']


     
