# coding:utf-8

from django import forms


class LinkAdminForm(forms.ModelForm):
    status = forms.BooleanField(label="是否删除", required=False)

    def clean_status(self):
        if self.cleaned_data['status']:
            return 2
        else:
            return 1


class SideBarAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label='内容', required=False)
