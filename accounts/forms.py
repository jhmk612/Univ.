from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    last_name=forms.CharField(max_length=10)
    first_name=forms.CharField(max_length=10)

    def save(self, commit=True):
        user=super(SignupForm,self).save(commit=False)
        user.last_name=self.cleaned_data['last_name']
        user.first_name=self.cleaned_data['first_name']
        if commit:
            user.save()
        return user

    class Meta:
        model=User
        fields = ['username', 'password1', 'password2', 'last_name', 'first_name']
        labels = {'username': '아이디를 입력하세요', 'password1':'패스워드를 입력하세요', 'password2': '패스워드를 다시 한 번 입력하세요', 'last_name':'성을 적어주세요', 'first_name':'이름을 적어주세요'}