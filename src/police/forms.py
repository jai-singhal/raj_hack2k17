from django.contrib.auth import authenticate
from django import forms
from django.utils.translation import ugettext_lazy as _



class UsersLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UsersLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name":"username",
            "placeholder":"Username"})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            "name":"password",
            "placeholder":"Password"})

    def clean(self, *args, **keyargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError(_("Invalid Credentials"))

        return super(UsersLoginForm, self).clean(*args, **keyargs)
