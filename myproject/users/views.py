from django.shortcuts import render
from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import uuid

# Create your views here.


def user(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.users ORDER BY user_id ASC")
        data = cursor.fetchall()
    # print(data) 
    # return 
    context = {"data": data}
    return JsonResponse(context)
    # return render(request, 'company.html', context)
    
    
    
@csrf_exempt
def insertDataUser(request):

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.users ORDER BY user_id ASC")
        data = cursor.fetchall()
    context = {"data": data}
    
    if request.method == "POST":
        user_id = request.POST.get('user_id', None)
        if user_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT nextval('public.users_user_id_seq')")
                user_id = cursor.fetchone()[0]
        company_id = request.POST.get('company_id') or None
        person_id = request.POST.get('person_id', None)
        if person_id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT nextval('public.users_user_id_seq')")
                person_id = cursor.fetchone()[0]
        username = request.POST.get('username') or None
        password_hash = make_password(request.POST.get('password_hash'))
        is_active = request.POST.get('is_active') or True
        auth_key = str(uuid.uuid4())
        created_by = request.POST.get('created_by') or None 
        created_time = timezone.now().replace(microsecond=0)
        updated_by = request.POST.get('updated_by') or None
        updated_time = timezone.now().replace(microsecond=0)
        is_deleted = request.POST.get('is_deleted') and False
        deleted_by = request.POST.get('deleted_by') or None
        deleted_time = request.POST.get('deleted_time') or None

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO public.users (user_id, company_id, person_id, username, password_hash, is_active, auth_key, created_by, created_time, updated_by, updated_time, is_deleted, deleted_by, deleted_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, [user_id, company_id, person_id, username, password_hash, is_active, auth_key, created_by, created_time, updated_by, updated_time, is_deleted, deleted_by, deleted_time])
        
        # messages.success(request, "Data Terkirim")
        # return redirect('user')
    return JsonResponse(context)
    # return render(request, 'usertabel.html', context)
    
@csrf_exempt
def DeleteDataUser(request, user_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM public.users WHERE user_id = %s", [user_id])
    context = {"message": "data berhasil dihapus"}
    return JsonResponse(context)


# @csrf_exempt
# def UpdateDataUser(request, user_id):
#     if request.method == "POST":
#         company_id = request.POST.get('company_id')
#         person_id = request.POST.get('person_id')
#         username = request.POST.get('username')
#         password_hash = make_password(request.POST.get('password') or '')
#         is_active = request.POST.get('is_active')
#         auth_key = str(uuid.uuid4())
#         created_by = request.POST.get('created_by')
#         created_time = timezone.now().replace(microsecond=0)
#         updated_by = request.POST.get('updated_by')
#         updated_time = timezone.now().replace(microsecond=0)
#         is_deleted = request.POST.get('is_deleted')
#         deleted_by = request.POST.get('deleted_by')
#         deleted_time = request.POST.get('deleted_time')
    

#         # Simpan data ke dalam database
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 UPDATE public.users
#                 SET company_id = %s, person_id = %s, username = %s, password_hash = %s, is_active = %s, auth_key = %s, created_by = %s, created_time = %s, updated_by = %s, updated_time = %s, is_deleted = %s, deleted_by = %s, deleted_time = %s
#                 WHERE user_id = %s
#             """, [company_id, person_id, username, password_hash, is_active, auth_key, created_by, created_time, updated_by, updated_time, is_deleted, deleted_by, deleted_time, user_id])
        
#         # messages.success(request, "Data berhasil di update")
#         # return redirect('company')  

#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM public.users WHERE user_id = %s", [user_id])
#         data = cursor.fetchone()
    
#     context = {"data": data}
#     return JsonResponse(context)