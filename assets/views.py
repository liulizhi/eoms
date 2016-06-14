from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required 

@login_required(login_url="/login/")
def dashboard(request, template_name):
    return render_to_response(template_name, 
                              {'user': request.user}
                              )
