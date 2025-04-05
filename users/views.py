from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.forms import UserRegisterForm, UserLoginForm, UserForm


def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('dogs:index'))

    form = UserRegisterForm()
    context = {
        'title': 'Создать аккаунт',
        'form': form
    }

    return render(request,'users/user_register.html', context=context)

def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('dogs:index'))
                else:
                    return HttpResponse('Аккаунт не активен')

    context = {
        'title': 'Вход в аккаунт',
        'form': UserLoginForm()
    }
    return render(request, 'users/user_login.html', context=context)


@login_required
def user_profile_view(request):
    user_object = request.user
    context = {
        'title': f'Ваш профиль {user_object.first_name} {user_object.last_name}'
    }
    return render(request, 'users/user_profile_read_only.html', context=context)


def user_logout_view(request):
    logout(request)
    return redirect('dogs:index')

