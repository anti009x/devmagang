from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import logging

# Set up logging
logger = logging.getLogger(__name__)

@csrf_exempt
@require_POST
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')  

    if not username or not password:
        return JsonResponse({'status': 'error', 'message': 'Username and password are required'}, status=400)

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.users WHERE username = %s", [username])
        user = cursor.fetchone()

    if user is not None and check_password(password, user[4]):  
        auth_key = user[7]  
        user_id = user[0]  
        return JsonResponse({'status': 'success', 'message': 'Login successful', 'auth_key': auth_key, 'user_id': user_id, 'username': username})
    else:
        logger.error("Invalid username or password")
        return JsonResponse({'status': 'error', 'message': 'Invalid username or password'}, status=401)
    
    
@csrf_exempt
@require_POST
def logoutview(request):
    auth_key = request.META.get('HTTP_AUTHORIZATION')
    if auth_key:
        auth_key = auth_key.split(' ')[1]  
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM public.users WHERE auth_key = %s", [auth_key])
            user = cursor.fetchone()
            if user:
                logout(request)
                request.session.flush()
                return JsonResponse({'status': 'success', 'message': 'Logout successful'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid auth key'}, status=401)
    else:
        return JsonResponse({'status': 'error', 'message': 'Authorization header missing'}, status=400)