#coding:utf-8
from django import forms
class snsForm(forms.Form):
    name = forms.CharField(label='姓名')
    content = forms.CharField(label="内容",widget=forms.Textarea)
