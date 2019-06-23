#coding:utf-8
from django.contrib.auth.views import login
from django.shortcuts import render, redirect

def custom_login(request):
    if request.user.is_authenticated():
        return redirect('visao_geral')
    else:
        return login(request)