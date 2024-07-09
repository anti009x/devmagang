from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import random
# Create your views here.


# Create your views here.


def coa(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.coa ORDER BY id ASC")
        data = cursor.fetchall()
    # print(data) 
    # return 
    context = {"data": data}
    return JsonResponse(context)
    # return render(request, 'company.html', context)
    

# @csrf_exempt
# def insertDataCoa(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM fin.coa ORDER BY company_id ASC")
#         data = cursor.fetchall()
#     context = {"data": data}
    
#     if request.method == "POST":
        
#         id = request.POST.get('id')
#         if id is None:
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT nextval('fin.coa_id_seq')")
#                 id_result = cursor.fetchone()
#                 if id_result:
#                     id = id_result[0]
#                 else:
#                     return JsonResponse({'status': 'error', 'message': 'Failed to generate ID'}, status=500)
#         company_id = request.POST.get('company_id')
#         coa_code = request.POST.get('coa_code') or ''.join([str(i) for i in range(1, 5)])
#         coa_name = request.POST.get('coa_name')
#         normal_balance = request.POST.get('normal_balance')
#         subheader = request.POST.get('subheader')
#         created_by = request.POST.get('created_by') or None
#         created_time = timezone.now().replace(microsecond=0)
#         updated_by = request.POST.get('updated_by') or None
#         updated_time = timezone.now().replace(microsecond=0)
#         is_deleted = request.POST.get('is_deleted') and False
#         deleted_by = request.POST.get('deleted_by') or None
#         deleted_time = request.POST.get('deleted_time') or None
#         is_bridging_acc = request.POST.get('is_bridging_acc') and False

        
#         # if company_id is None:
#         #     return JsonResponse({'status': 'error', 'message': 'Company ID is required'}, status=400)
#         # if coa_code is None:
#         #     return JsonResponse({'status': 'error', 'message': 'COA Code is required'}, status=400)
#         # if coa_name is None:
#         #     return JsonResponse({'status': 'error', 'message': 'COA Name is required'}, status=400)
        
        
                                 

#         # Simpan data ke dalam database
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 INSERT INTO fin.coa (company_id, coa_code, coa_name, normal_balance, subheader, created_by, created_time, updated_by, updated_time, is_deleted, deleted_by, deleted_time, is_bridging_acc)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#             """, [company_id, coa_code, coa_name, normal_balance, subheader, created_by, created_time, updated_by, updated_time, is_deleted, deleted_by, deleted_time, is_bridging_acc])
        
#         # messages.success(request, "Data Terkirim")
#         # return redirect('bankaccount')
#     return JsonResponse(context)
#     # return render(request, 'bankaccounttabel.html', context)


@csrf_exempt
def insertDataCoa(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.coa ORDER BY id ASC")
        data = cursor.fetchall()
    context = {"data": data}
    
    if request.method == "POST":
        
        id = request.POST.get('id')
        if id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT nextval('fin.coa_id_seq')")
                id = cursor.fetchone()[0]
        company_id = request.POST.get('company_id')
      
        coa_code = request.POST.get('coa_code') or ''.join([str(random.randint(0, 9)) for _ in range(6)])
        coa_name = request.POST.get('coa_name')
        normal_balance = request.POST.get('normal_balance')
        subheader_id = request.POST.get('subheader_id')
        created_by = request.POST.get('created_by') or None
        created_time = timezone.now().replace(microsecond=0)
        updated_by = request.POST.get('updated_by') or None
        updated_time = timezone.now().replace(microsecond=0)
        is_deleted = request.POST.get('is_deleted') or False
        deleted_by = request.POST.get('deleted_by') or None
        deleted_time = timezone.now().replace(microsecond=0)
        is_bridging_acc = request.POST.get('is_bridging_acc') or False
    
        
        if company_id is None:
            return JsonResponse({'status': 'error', 'message': 'Company ID is required'}, status=400)
        if coa_code is None:
            return JsonResponse({'status': 'error', 'message': 'COA Code is required'}, status=400)
        if coa_name is None:
            return JsonResponse({'status': 'error', 'message': 'COA Name is required'}, status=400)
        
                                 

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO fin.coa (id, company_id, coa_code, coa_name, normal_balance, subheader_id, created_by, created_time, updated_by, updated_time, is_deleted, deleted_by, deleted_time, is_bridging_acc)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, [id, company_id, coa_code, coa_name, normal_balance, subheader_id, created_by, created_time, updated_by, updated_time, is_deleted, deleted_by, deleted_time, is_bridging_acc])
        
        # messages.success(request, "Data Terkirim")
        # return redirect('bankaccount')
    return JsonResponse(context)
    # return render(request, 'bankaccounttabel.html', context)
    
@csrf_exempt
def DeleteDataCoa(request, id):
    if id is None:
        return JsonResponse({'status': 'error', 'message': 'ID is required'}, status=400)
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM fin.coa WHERE id = %s", [id])
    context = {"message": "data berhasil dihapus"}
    return JsonResponse(context)