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


class AnonymousUsersLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(AnonymousUsersLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name":"username"})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            "name":"password"})

    def clean(self, *args, **keyargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError("Invalid Credentials")

        return super(AnonymousUsersLoginForm, self).clean(*args, **keyargs)
