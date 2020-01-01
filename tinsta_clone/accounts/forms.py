from django import forms
from django.contrib.auth.models import User

class SignUpFrom(forms.ModelForm):
    password = forms.CharField(label = 'password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email',]

    def clean_Repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['Repeat_password']:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return cd['Repeat_password']