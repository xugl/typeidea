# coding:utf-8
from django import forms


class CommentAdminForm(forms.ModelForm):
    pass
    # status = forms.BooleanField(label="是否可用",required=False)  #TODO: 处理布尔类型为我们所需要的
    #
    # def clean_status(self):
    #     if self.cleaned_data['status']:
    #         return 1
    #     else:
    #         return 2