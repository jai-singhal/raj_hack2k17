from django import forms
from .models import AnonymousTip


class AnonymousTipForm(forms.Form):
    class Meta:
        model = AnonymousTip
        fields = '__all__'
        exclude = ['userid']

    # def __init__(self , *args, ** kwargs):
    #     super(AnonymousTipForm,self).__init__(*args, **kwargs)
    #
    # def clean(self):
    #     pass
