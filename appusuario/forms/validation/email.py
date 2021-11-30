# coding: utf-8
from django import forms
from django.contrib.auth.models import User


def ValidationEmail(email):
    if not User.objects.filter(email=email):
        return email
    else:
        raise forms.ValidationError("Email já cadastrado!")


def ValidationEmailConvidado(email):
    if not User.objects.filter(email=email) and not User.objects.filter(username=email):
        return email
    else:
        raise forms.ValidationError("Email já cadastrado!")
