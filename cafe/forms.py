from .models import Post, Reply
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'contents', 'tags']
        labels = {'title': '제목', 'contents':'내용', 'tags': '태그'}

class ReplyForm(forms.ModelForm):
    class Meta:
        model=Reply
        fields=['content',]
        labels={'content':'내용'}