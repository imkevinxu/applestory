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

def redirect_login(request):
    if request.user.is_authenticated():
        return redirect("profile", username=request.user)
    else:
        return redirect("index")




### View functions
def index(request):
    return render(request, "index.html", locals())



#TODO: REALLY JANKY REGISTRATION ERROR CHECKING
def register(request):
    if request.POST:
        if request.POST.get("username") and request.POST.get("email") and request.POST.get("password"):

            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            if username_present(username):
                return redirect("index", msg="Username already taken")

            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        # Success!
                        login(request, user)
                        return redirect_login(request)
                    else:
                        # Return a 'disabled account' error message
                        return redirect("index", msg="Account has been disabled")
                else:
                    # Return an 'invalid login' error message.
                    return redirect("index", msg="Invalid login")
        else:
            return redirect("index", msg="Missing required field")

    return render(request, "index.html", locals())


def profile(request, username=None):
    if username is None:
        return redirect("index")
        # Should return 404 Error

    if not username_present(username):
        return redirect("index")
        # Should return 404 Error

    return render(request, "profile.html", locals())

