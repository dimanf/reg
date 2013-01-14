# -*- coding: utf-8 -*-
from django import forms

''' Класс формы для восстановления забытого пароля '''
class SendPassworForm(forms.Form):
    email = forms.EmailField(label='email')

