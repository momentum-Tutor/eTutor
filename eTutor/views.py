from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse, JsonResponse
from users.models import User
from .models import Language

def homePage(request):
    allusers = User.objects.all()
    if request.user.is_authenticated:
        return render(request, 'eTutor/homepage.html', {'allusers': allusers})
    else: 
        return render(request, 'eTutor/welcome_page.html')

# def homePage(request):
#     allusers = User.objects.all()
#     language_contains_query = request.GET.get('lang_contains')

#     if language_contains_query != ' ' and language_contains_query is not None:
#         allusers = allusers.filter(body_icontains = language_contains_query)
        
#     context = {
#         'queryset': allusers
#     }
#     if request.user.is_authenticated:
#         return render(request, 'eTutor/homepage.html', {'allusers': allusers})
#     else: 
#         return render(request, 'eTutor/welcome_page.html')

def logout(request):
    return render(request, 'eTutor/homepage.html')


def usersPage(request):
    allusers = User.objects.all()
    return render(request, 'eTutor/all_users.html', {'allusers': allusers})


