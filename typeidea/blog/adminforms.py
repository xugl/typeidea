# coding:utf-8
from django import forms

from dal import autocomplete
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Tag

class PostAdminForm(forms.ModelForm):
    status = forms.BooleanField(label="是否删除",required=False)  #TODO: 处理布尔类型为我们所需要的
    desc= forms.CharField(widget=forms.Textarea,label='摘要',required=False)

    content = forms.CharField(widget=CKEditorUploadingWidget(), label='正文', required=True)

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类',
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签',
    )

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