from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from stores.stores_auth.forms import SignUpForm, SignInForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    else:
        form = SignUpForm()

    context = {
        'form': form
    }
    return render(request, 'auth/sign_up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.GET['next'] is not '':
                return redirect(request.GET.get('next'))
            return redirect('index')
    else:
        form = SignInForm()

    context = {'form': form}
    return render(request, 'auth/sign_in.html', context)


def sign_out(request):
    logout(request)
    return redirect('index')
