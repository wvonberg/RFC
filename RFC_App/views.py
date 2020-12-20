from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"landingPage.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landingPage')
            else:
                raise ValidationError('Registration Unsuccesful please try again')
            #customer_group = Group.objects.get(name='Customer')
            #customer_group.user_set.add(signup_user)
        return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) #yikes, on that data per parameter for authform
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landingPage')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')

def forum(request):
    context = {
        #'user': User.objects.get(pk=request.user.pk),
        'user_posts': Post.objects.all(),
    }
    return render(request,"forum.html", context)

def add_post(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            post = Post.objects.create(title=request.POST['title'], body=request.POST['body'], author=User.objects.get(pk=request.user.pk))
        print('post')
        return redirect('/forum')
    return redirect('/landingPage')


        #post = Post.objects.create(body=request.POST['body'], author=User.objects.get(id=request.session['username']))

def add_comment(request, id):
    #if 'user_id' not in request.session:
    #    return redirect('/')
    if request.method == "POST":
        user = User.objects.get(pk=request.user.pk)
        post = Post.objects.get(id=id)
        Comment.objects.create(comment=request.POST['comment'], user=user, post=post)
        return redirect(f"/goto_post/{post.id}")
    return redirect('/forum')

def single_post_page(request, id):
    post_with_id = Post.objects.filter(id=id)
    if len(post_with_id) > 0:
        context = {
            'post': Post.objects.get(id=id)
        }
        return render(request, 'single_post_page.html', context)
    else:
        return redirect('/landingPage')

def tech_support(request, id):
    return render(request,"techsupport.html")


# @login_required(login_url=signin)
def rules(request):
    return render(request, 'rules.html')

def speakeasy(request):
    if request.method == "POST":
        # get_user = User.objects.get(pk=request.user.pk)
        # if user.profile:
        #     get_profile = Profile.objects.get(user=get_user)
        #     get_profile.speakeasy = True
        #     get_profile.save()
        # else:
        #     new_profile = Profile.objects.create(user=get_user, speakeasy=True)
        return render(request, 'speakeasy.html')
    return redirect('rules')

def arena(request):
    pass


