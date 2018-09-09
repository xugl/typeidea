# coding:utf-8
from django import forms

class PostAdminForm(forms.ModelForm):
    status = forms.BooleanField(label="是否删除",required=False)  #TODO: 处理布尔类型为我们所需要的
    desc= forms.CharField(widget=forms.Textarea,label='摘要',required=False)

    def clean_status(self):
        if self.cleaned_data['status']:
            return 1
        else:
            return 3

class CategoryAdminForm(forms.ModelForm):
    status = forms.BooleanField(label="是否可用",required=False)  #TODO: 处理布尔类型为我们所需要的

    def clean_status(self):
        if self.cleaned_data['status']:
            return 1
        else:
            return 2

class TagAdminForm(forms.ModelForm):
    status = forms.BooleanField(label="是否可用",required=False)  #TODO: 处理布尔类型为我们所需要的

    def clean_status(self):
        if self.cleaned_data['status']:
            return 1
        else:
            return 2