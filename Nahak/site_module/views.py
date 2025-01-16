from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View

from site_module.forms import RegisterForm, LoginForm
from site_module.models import User


#
class RegisterView(View):
    def get(self, request: HttpRequest):
        register_form = RegisterForm
        context = {
            'register_form': register_form,
        }
        return render(request, 'register_page.html', context)

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = register_form.cleaned_data['username']
            user_email = register_form.cleaned_data['email']
            user_password = register_form.cleaned_data['password']
            user_mobile = register_form.cleaned_data['mobile']
            if User.objects.filter(email__iexact=user_email):
                messages.error(request, 'ایمیل وارد شده وجود دارد')
                return redirect(reverse('register_page'))

            if User.objects.filter(mobile__iexact=user_mobile):
                messages.error(request, 'موبایل وارد شده وجود دارد')
                return redirect(reverse('register_page'))

            new_user = User(
                username=user_name,
                email=user_email,
                email_active_code=get_random_string(80),
                is_active=False,
                is_staff=False,

            )
            if user_mobile is not None:
                new_user.mobile = user_mobile
            new_user.set_password(user_password)
            new_user.save()

            messages.success(request, 'ثبت نام با موفقیت انجام شد')
            return redirect(reverse('home_page'))
        messages.error(request, 'فیلد ها را به درستی پر کنید')
        return render(request, 'register_page.html', {'register_form': register_form})


def active_account_view(request: HttpRequest, active_code):
    user = User.objects.filter(email_active_code__iexact=active_code).first()
    if user is not None:
        if not user.is_active:
            user.is_active = True
            user.email_active_code = get_random_string(80)
            messages.success(request, 'حساب شما با موفقیت فعال شد')
            user.save()
            return redirect('home_page')
        else:
            return HttpResponse('<h1>حساب شما فعال میباشد</h1>')

    else:
        raise Http404('کاربر یافت نشد')


class LoginView(View):
    def get(self, request: HttpRequest):
        login_form = LoginForm
        context = {
            'login_form': login_form,
        }
        return render(request, 'login_page.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # user_email = login_form.cleaned_data['email']
            # user_mobile = login_form.cleaned_data['number']
            user = login_form.cleaned_data['user']
            login(request, user)
            return redirect('home_page')

        context = {
            'login_form': login_form,
        }

        return render(request, 'login_page.html', context)
