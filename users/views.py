from urllib import request
from django.shortcuts import HttpResponseRedirect, redirect
from django.contrib import auth, messages

from django.contrib.messages.views import SuccessMessageMixin

from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required

from users.models import Account, EmailVerification
from users.forms import UserLoginForm, UserRegistrationForm
from django.urls import reverse, reverse_lazy


#USER VERIFICATION

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            email = False
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid login or password')
            return redirect('users:login')
    else:
        form = UserLoginForm()
    context = {
        'forms': form
    }
    return render(request, 'users/signin.html', context)
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out!')
    return redirect('users:login')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        email = request.POST['email']


        if Account.objects.filter(email=email).exists():
            messages.error(request, 'Sorry! Email is already taken')


        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Low level of password')
            return redirect('users:register')
        return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def dashboard(request):
    return render(request, 'users/dashboard.html')


def forgotPassword(request):
    if request.method == 'POST':
        email=request.POST['email']
        if Account.objects.get(email=email).exists():
            user = Account.objects.get(email__exact=email)  # SELECT ... WHERE email=email.POST
        else:
            messages.error(request, 'Account does not exist!')


    return render(request, 'users/forgotPassword.html')


class EmailVerificationView(TemplateView):
    template_name = 'users/email_verification.html'

    def get(self, *args, **kwargs):
        code = kwargs['code']
        user = Account.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
