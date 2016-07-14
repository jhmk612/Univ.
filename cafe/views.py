from django.shortcuts import render, redirect
from .forms import PostForm, ReplyForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Post, Reply
# Create your views here.

def home(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, 'cafe/home.html', context)


@login_required
def post(request):
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)
    if request.method == 'POST':
        f=PostForm(request.POST)
        new_post=f.save(commit=False)
        new_post.writer=request.user
        new_post.save()

        return redirect('/view_post')

    else:
        f=PostForm()

    return render(request, 'cafe/post.html', {'form':f})


def view_post(request, pk):
    post=Post.objects.get(pk=pk)
    replies=Reply.objects.filter(pk=Reply.at)
    context={'post':post, 'replies':replies}
    return render(request, 'cafe/view_post.html', context)

def reply(request):
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)
    if request.method == 'POST':
        f=ReplyForm(request.POST)
        new_reply=f.save(commit=False)
        new_reply.writer=request.user
        new_reply.save()

        return redirect('.')

    else:
        f=ReplyForm()

    return render(request, 'cafe/view_post.html', {'form':f})

