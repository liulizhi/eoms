from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from models import Host, Machine_Room
from forms import HostForm

@login_required(login_url="/login/")
def dashboard(request, template_name):
    host_lists = Host.objects.all()
    return render_to_response(template_name, 
                              {'user': request.user,
                               'host_lists': host_lists,
                               }
                              )


@login_required(login_url="/login/")
def add(request, template_name):
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            host_info = form.save()
            host_info.save()
            return HttpResponseRedirect('/assets/')
            #return HttpResponseRedirect('/')
    else:
        form = HostForm()
    return render_to_response(template_name, 
                              {'user': request.user,
                               'form': form,
                               }
                              )

@login_required(login_url="/login/")    
def delete(request):
    pass

@login_required(login_url="/login/")
def update(request):
    pass

@login_required(login_url="/login/")
def search(request, template_name):
    search_q = request.GET.get('search')
    host_msg_lists = Host.objects.filter(Q(ipaddr__icontains = search_q) | Q(hostname__icontains = search_q))  
    return render_to_response(template_name, 
                          {'user': request.user,
                           'host_lists': host_msg_lists,
                           }
                          )
    
    
    