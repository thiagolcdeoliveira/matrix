# coding: utf-8
from django import forms


def ValidationSQL(sql):
    proibido=['insert','update','delete','drop','alter','create']
    for proibid in  proibido:
        if proibid.lower() in sql.lower():
            raise forms.ValidationError("É proibido usar esse comando!")
    else:
        return sql

