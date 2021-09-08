from django.forms import ModelForm
from accounts.models import MyUser


class LoginForm(ModelForm):
    '''Simple login form'''
    class Meta:
        model = MyUser
        fields = ('username', 'password')