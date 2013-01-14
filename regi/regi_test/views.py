# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib import auth
from django.template import Context
from django.template.loader import get_template

from regi.myusermodel.admin import UserCreationForm, UserSetPasswordForm, UserChangePasswordForm
from regi.myusermodel.models import MyUser
from regi.myusermodel.forms import SendPassworForm

from django.http import Http404

import datetime
import string
import random


def get_user_name(request):
    
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/account/loggedin/")
    # else:
        # return HttpResponseRedirect("/invalid/")

    return render_to_response('login.html', locals(),\
    context_instance = RequestContext(request))

def loggedin_view(request):

    return render_to_response('loggedin.html', locals(),\
    context_instance = RequestContext(request))

def unique_str_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def user_creation(request):
    if request.method == 'POST':        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            cu = form.cleaned_data
            user = MyUser.objects.create_user(
                username = cu['username'],
                email = cu['email'],
                address = cu['address'],                
                date_of_birth = cu['date_of_birth'],
                activate_sting = unique_str_generator(10),                                
                password=cu['password1'])
            user.save()

            # activate = MyUser.objects.get(email = user.email)

            send_mail(
                    u'Регистрация на сайте',
                    get_template('registration/registration_message.txt').render(
                        Context({
                            'username': cu['username'],
                            'activate': user.activate_sting                                                        
                        })
                    ),
                    'hooper_spd@mail.ru',
                    [user.email]
                )                      

            return HttpResponseRedirect('/accounts/success/')                
    else:
        form = UserCreationForm()        

    return render_to_response('user_creation.html', locals(),\
    context_instance = RequestContext(request))


def user_activate(request, activate_key):

    user = MyUser.objects.get(activate_sting = activate_key)
    today = datetime.date.today()
    activation_pediod = user.date_create + datetime.timedelta(days=10)

    if user and today <= activation_pediod:
        user.is_active = True
        user.save()
    else:
        raise Http404     

    return render_to_response('activate.html', locals(),\
    context_instance = RequestContext(request))

def user_set_password(request, activate_key):
    
    user = MyUser.objects.get(activate_sting = activate_key)
    today = datetime.date.today()
    activation_pediod = user.date_create + datetime.timedelta(days=10)

    if user and today <= activation_pediod:
        if request.method == 'POST':
            form = UserSetPasswordForm(request.POST)
            if form.is_valid():
                usp = form.cleaned_data                
                user.set_password(usp['password1'])
                user.save()
                return HttpResponseRedirect('/accounts/success/')
        else:
            form = UserSetPasswordForm()

    return render_to_response('user_set_password.html', locals(),\
    context_instance = RequestContext(request))                

def send_password(request):

    if request.method == 'POST':
        form = SendPassworForm(request.POST)
        if form.is_valid():
            sp = form.cleaned_data
            email = sp['email']
            user = MyUser.objects.get(email = email)           

            send_mail(
                    u'Восстановление пароля',
                    get_template('registration/send_password.txt').render(
                        Context({                            
                            'activate_key': user.activate_sting,                                                                                    
                        })
                    ),
                    'hooper_spd@mail.ru',
                    [email]
                )

            return HttpResponseRedirect('/accounts/success/')
    else:
        form = SendPassworForm()

    return render_to_response('sendpassword.html', locals(),\
    context_instance = RequestContext(request))

def change_password(request):
    user_name = request.user.username
    user_all = request.user
    user = MyUser.objects.get(username = user_name)
    if request.method == 'POST':
        form = UserChangePasswordForm(request.POST)
        if form.is_valid():
            usp = form.cleaned_data                
            user.set_password(usp['password1'])
            user.save()
            return HttpResponseRedirect('/accounts/success/')
    else:
        form = UserChangePasswordForm()

    return render_to_response('change_password.html', locals(),\
    context_instance = RequestContext(request))        

def user_create_success(request):
    return render_to_response('success.html', locals(),\
    context_instance = RequestContext(request))


