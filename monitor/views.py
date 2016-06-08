from django.shortcuts import render, render_to_response

# Create your views here.

def dashboard(request, template_name):
    data01 = {"su": [23, 23, 45, 2, 4, 5, 8 ,9, 24, 6, 28, 19],
              "qi": [18, 24, 39, 6, 8, 6, 8 ,20, 25, 9, 19, 29],
              "rui": [20, 23, 47, 2, 7, 5, 8 ,9, 24, 4, 28, 14],
              "suqirui": [21, 23, 41, 9, 4, 7, 24 ,28, 24, 24, 26, 15]}
    return render_to_response(template_name, 
                              {'user': request.user,
                               'data01': data01,}
                              )
