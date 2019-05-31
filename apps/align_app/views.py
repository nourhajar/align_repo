from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from datetime import datetime
import bcrypt

def index(request):
    if 'id' in request.session:
        del request.session['id']
        del request.session["username"]
        del request.session["email"]
    return render(request, 'align_app/index.html')

def register(request):

    request.session["username"] = request.POST["username"]
    request.session["email"] = request.POST["email"]

    errors = User.objects.basic_validator(request.POST, True)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)

        return redirect('/')

    if request.method == "POST":

        hashpw = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
        user = User.objects.create(username=request.POST["username"], email=request.POST["email"], password=hashpw, sun_sign=request.POST['sun_sign'], moon_sign=request.POST['moon_sign'], rising_sign=request.POST['rising_sign'])
        user.save()

        request.session["id"] = user.id

        return redirect('/dashboard')

def login(request):

    errors = User.objects.basic_validator(request.POST, False)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/')

    if request.method == "POST":

        user = User.objects.get(email=request.POST["email"])
        request.session["id"] = user.id
        request.session["username"] = user.username
        request.session["email"] = user.email

        return redirect('/dashboard')


def dash(request):

    if 'id' not in request.session:
        return redirect('/')
    else:
        context = {
            "all_users": User.objects.all()
        }
        return render(request, 'align_app/venus.html', context)

def message(request, id):

    if 'id' not in request.session:
        return redirect('/')
    else:
        x = User.objects.get(id=id)
        context = {
            "all_messages": Message.objects.filter(recipient=x).order_by("-created_at"),
            "recipient": x
        }
        return render(request, 'align_app/mercury.html', context)

def profile(request, id):

    if 'id' not in request.session:
        return redirect('/dashboard')
    else:
        x = User.objects.get(id=id)
        context = {
            "all_messages": Message.objects.filter(recipient=x).order_by("-created_at"),
            "recipient": x
        }
        return render(request, 'align_app/rising.html', context)

def create_message(request, id):

    x = User.objects.get(username=request.session['username'])
    y = request.POST['message']
    z = User.objects.get(id=id)
    Message.objects.create(user=x, recipient=z, message=y)
    return redirect("/mercury/" + id)

def create_comment(request, id):

    x = User.objects.get(username=request.session['username'])
    y = request.POST['comment']
    z = request.POST['message_id']
    a = Message.objects.get(id=z)
    Comment.objects.create(message=a, user=x, comment=y)
    return redirect("/mercury/" + id)

def delete_comment(request, id):
    x = request.POST['comment_id']
    c = Comment.objects.get(id=x)
    c.delete()
    return redirect("/mercury/" + id)