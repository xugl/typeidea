# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='内容',
        max_length=100,
        widget=forms.widgets.Textarea(attrs={'rows':6,'cols':80})
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('长度怎么能这么短呢？')

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']