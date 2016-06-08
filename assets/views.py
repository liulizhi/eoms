from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def dashboard(request, template_name):
    return render_to_response(template_name, 
                              {'user': request.user}
                              )
