import uuid

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from users.models import Account, EmailVerification
from datetime import timedelta
from django.utils.timezone import now


class UserLoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Email Address'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password'
    }))
    class Meta:
        model = Account
        fields = ('email', 'password')

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control ', }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', }))

    def save(self, commit=True):   #переопределили метод сейв
        user = super(UserRegistrationForm, self).save(commit=True)
        expiration = now()+timedelta(hours=48)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user



    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email','city', 'password1', 'password2']