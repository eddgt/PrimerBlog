# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from PrimerBlog.views import * 
 
def main(request):
    return render_to_response('main.html', {}, context_instance=RequestContext(request))