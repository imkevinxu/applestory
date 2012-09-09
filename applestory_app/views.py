from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render, \
    redirect
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt

from applestory_app.models import *
from applestory_app.model_forms import *
from applestory_app.forms import *

### Utilities
def username_present(username):
    if User.objects.filter(username=username).count():
        return True
    return False



### View functions
def index(request):
    return render(request, "index.html", locals())


def register(request):
    if request.POST:
        if request.POST.get("username") and request.POST.get("email") and request.POST.get("password"):

            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            if username_present(username):
                return redirect("index")

            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                    else:
                        # Return a 'disabled account' error message
                        return redirect("index")
                else:
                    # Return an 'invalid login' error message.
                    return redirect("index")\

    return redirect("index")


def profile(request, username):


    return render(request, "profile.html", locals())

