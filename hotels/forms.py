from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("Неверные данные")
            if not user.is_active:
                raise forms.ValidationError("Вы заблокированы")
        return super(LoginForm,self).clean(*args,**kwargs)

class RegistrationForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = [
            'username',
            'password',
            'confirm_password'
        ]

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if username and password:
            user = User.objects.filter(username=username)
            if user.exists():
                raise forms.ValidationError("Имя пользователя уже занято")
            if(password!=confirm_password):
                raise forms.ValidationError("Пароли не совпадают")

        return super(RegistrationForm,self).clean(*args,**kwargs)