from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

# 회원가입
def signup(request):
    print('---- signup ----')

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            auth_login(request, user)
            return redirect('home')
        else:
            return render('pages/page.html', {'msg' : '회원가입 실패, 다시 시도해주세요.'})
    else:
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form' : form,})
    # return render(request, 'board/main.html')

# 로그인
def login(request):
    print('---- login ----')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form' : form,})

# 프로필
@login_required
def profile(request):
    print('---- profile ----')
    return render(request, 'accounts/profile.html')

# 패스워드 변경
