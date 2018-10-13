# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CommentForm
from comment.models import Comment
from django.shortcuts import redirect


class CommentView(TemplateView):
    template_name = 'comment/result.html'

    def post(self,request,*args,**kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            succeed = True
        else:
            succeed = False

        context = {
            'success': succeed,
            'form': comment_form
        }

        return self.render_to_response(context)