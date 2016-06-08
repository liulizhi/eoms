from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

from JuncheePaginator import JuncheePaginator

from django.contrib.auth.models import User
  
from django.template.context_processors import csrf
from django.template import RequestContext

from django.contrib.auth.decorators import login_required 


from models import Bbs, BBS_user

# Create your views here.

### begin user info 

def bbs_login(request, template_name):
    return render_to_response(template_name)

# only one csrf control
#@csrf_protect
def authen(request):
    #c = {}
    #c.update(csrf(request))
    if request.method == "POST":
        try:
            uname = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(username=uname, password=passwd)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['user'] = uname
                    response = HttpResponseRedirect('/')
                    response.set_cookie('username',uname,3600)
                    return response
                else:
                    return render_to_response('login.html', {'login_err': 'deactive'})
            else:
                return render_to_response('login.html', {'login_err': 'meserror'})
    
            return render_to_response('login.html', {'login_err': 'meserror'})
        except Exception:
            return render_to_response('login.html',  {'login_err': 'meserror'})
        
    return render_to_response('login.html',  {'login_err': 'meserror'})

def logout(request):
    #response = HttpResponse('logout !!')
    #response.delete_cookie()
    try:
        username = request.session.get('user')
        if (username != "None"):
            del request.session['user']
    except Exception:
        pass
    return render_to_response('login.html')

def userinfo(request):
    pass

def setting(request):
    pass

def account(request):
    pass

### end user info

@login_required(login_url="/login/")
def author(request, template_name):
    return render_to_response(template_name,  
                              {'user': request.user}
                              )

@login_required(login_url="/login/")
def index(request):
    bbs_list = Bbs.objects.all()
    page = request.GET.get('page')
    #paginator = Paginator(bbs_list, 2)
    paginator = JuncheePaginator(bbs_list, 8)
    try:
        bbs_list = paginator.page(page)
    except PageNotAnInteger:
        bbs_list = paginator.page(1)
    except EmptyPage:
        bbs_list = paginator.page(paginator.num_pages)
    return render_to_response('bbs_list.html', 
                              {'bbs_all_list': bbs_list, 
                               'user': request.user}
                              )
    
@login_required(login_url="/login/") 
def bbs_detail(request, bid):
    bbs_details = Bbs.objects.get(pk=bid)
    return render_to_response('bbs_detail.html',
                              {'bbs_details': bbs_details,
                               'user': request.user,}
                              )
    
def add_blog(request, template_name):
    author_list = BBS_user.objects.all()
    return render_to_response(template_name, 
                              {"author_list": author_list,
                               'user': request.user}
                              )  

def add_blog_pro(request):
    blog_title = request.POST.get("title")
    blog_author = request.POST.get("author")
    user = User.objects.get(username=blog_author)
    blogauthor = BBS_user.objects.get(user=user)
    #summary = request.POST.get("summary")
    content = request.POST.get("content")
    #print content, blog_author
    bbs_blog = Bbs.objects.create(
        
        title = blog_title,
        #summary = summary,
        author = blogauthor,
        content = content,
    )
    response = HttpResponseRedirect('/bbs/', 
                                    {'user': request.user}
                                    )
    return response

def delete_blog(request, bid):
    blog = Bbs.objects.get(pk=bid)
    blog.delete()
    return HttpResponseRedirect("/bbs/")

def manage_blog_list(request):
    bbs_list = Bbs.objects.all()
    return render_to_response('manage_bbs_list.html', 
                              {'bbs_list': bbs_list,
                               'user': request.user}
                              )
    
def search(request, template_name):

    return render_to_response(template_name)

def search_deal(request, *args, **kwargs ):
    search_content = request.POST.get("search")
    print args
    print kwargs
    print search_content
    return HttpResponseRedirect("/bbs/", 
                                {'user': request.user })

def dashboard(request, template_name):
    return render_to_response(template_name,
                              {'user': request.user}
                              )

    

