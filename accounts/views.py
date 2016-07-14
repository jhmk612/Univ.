from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.

def signup(request):
    if request.method=='POST':
        f=SignupForm(request.POST)

        if f.is_valid():
            f.save()

            return redirect('/accounts/login')
    else:
        f=SignupForm()

    return render(request, 'accounts/signup.html', {'form':f})

