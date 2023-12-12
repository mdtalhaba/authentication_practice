from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required

def Register(req) :
    if not req.user.is_authenticated :
        if req.method == 'POST' :
            register_form = RegistrationForm(req.POST)
            if register_form.is_valid() :
                messages.success(req, 'Your Registration Successfull')
                register_form.save()
                return redirect('login')
        else :
            register_form = RegistrationForm()
        return render(req, 'register.html', {'form' : register_form })
    else :
        return redirect('home')


def user_login(req) :
    if not req.user.is_authenticated :
        if req.method == 'POST' :
            login_form = AuthenticationForm(req, data=req.POST)
            if login_form.is_valid() :
                user_name = login_form.cleaned_data['username']
                user_pass = login_form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_pass)
                if user is not None :
                    messages.success(req, 'Logged In Successfully')
                    login(req, user)
                    return redirect('profile')
        else :
            login_form = AuthenticationForm()
        return render(req, 'login.html', {'form' : login_form })
    else :
        return redirect('home')


@login_required(login_url='/login/')
def user_logout(req) :
    logout(req)
    messages.success(req, 'Logged Out Successfully')
    return redirect('login')


@login_required(login_url='/login/')
def profile(req) :
    if req.method == 'POST' :
            changeUser_form = ChangeUserForm(req.POST, instance=req.user)
            if changeUser_form.is_valid() :
                messages.success(req, 'Your Profile Updated Successfull')
                changeUser_form.save()
                return redirect('profile')
    else :
            changeUser_form = ChangeUserForm(instance=req.user)
    return render(req, 'profile.html', {'form' : changeUser_form })


@login_required(login_url='/login/')
def pass_change(req) :
    if req.method == 'POST' :
        pass_form = PasswordChangeForm(user=req.user, data=req.POST)
        if pass_form.is_valid() :
            messages.success(req, 'Your Password Changed Successfull')
            pass_form.save()
            update_session_auth_hash(req, pass_form.user)
            return redirect('profile')

    else :
        pass_form = PasswordChangeForm(user=req.user)

    return render(req, 'pass_change.html', {'form' : pass_form, 'type' : 'Change'})


@login_required(login_url='/login/')
def set_pass(req) :
    if req.method == 'POST' :
        pass_form = SetPasswordForm(user=req.user, data=req.POST)
        if pass_form.is_valid() :
            messages.success(req, 'Your Password Set Successfull')
            pass_form.save()
            update_session_auth_hash(req, pass_form.user)
            return redirect('profile')

    else :
        pass_form = SetPasswordForm(user=req.user)

    return render(req, 'pass_change.html', {'form' : pass_form, 'type' : 'Set'})
