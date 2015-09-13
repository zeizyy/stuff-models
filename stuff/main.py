import datetime

from django.http import JsonResponse
from django.contrib.auth import hashers
from django import db

from stuff import models

# APIs for accessing Users

def create_user(request):
    if request.method != 'POST':
        return _error_response(request, "must make POST request")
    if 'f_name' not in request.POST or     \
       'l_name' not in request.POST or     \
       'password' not in request.POST or   \
       'username' not in request.POST:
        return _error_response(request, "missing required fields")

    u = models.User(username=request.POST['username'],                         \
                    f_name=request.POST['f_name'],                             \
                    l_name=request.POST['l_name'],                             \
                    password=hashers.make_password(request.POST['password']),  \
                    is_active=False,                                           \
                    date_joined=datetime.datetime.now()                        \
                    )

    try:
        u.save()
    except db.Error:
        return _error_response(request, "db error")

    return _success_response(request, {'user_id': u.pk})

def lookup_user(request, user_id):
    if request.method != 'GET':
        return _error_response(request, "must make GET request")

    try:
        u = models.User.objects.get(pk=user_id)
    except models.User.DoesNotExist:
        return _error_response(request, "user not found")

    return _success_response(request, {'username': u.username,      \
                                       'f_name': u.f_name,          \
                                       'l_name': u.l_name,          \
                                       'is_active': u.is_active,    \
                                       'date_joined': u.date_joined \
                                       })

def update_user(request, user_id):
    if request.method != 'POST':
        return _error_response(request, "must make POST request")

    try:
        u = models.User.objects.get(pk=user_id)
    except models.User.DoesNotExist:
        return _error_response(request, "user not found")

    changed = False
    if 'f_name' in request.POST:
        u.f_name = request.POST['f_name']
        changed = True
    if 'l_name' in request.POST:
        u.l_name = request.POST['l_name']
        changed = True
    if 'password' in request.POST:
        u.password = hashers.make_password(request.POST['password'])
        changed = True
    if 'is_active' in request.POST:
        u.is_active = request.POST['is_active']
        changed = True

    if not changed:
        return _error_response(request, "no fields updated")

    u.save()

    return _success_response(request)

def _error_response(request, error_msg):
    return JsonResponse({'ok': False, 'error': error_msg})

def _success_response(request, resp=None):
    if resp:
        return JsonResponse({'ok': True, 'resp': resp})
    else:
        return JsonResponse({'ok': True})

