#!usr/bin/env python
# _*_ coding:utf-8 _*_

from django import forms


class PanelForm(forms.Form):
    """panel forms"""

    name = forms.CharField()
    password = forms.CharField()
