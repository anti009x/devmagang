from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import random

def coacategory(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.coa_category ORDER BY id ASC")
        data = cursor.fetchall()
    # print(data) 
    # return 
    context = {"data": data}
    return JsonResponse(context)
    # return render(request, 'company.html', context)\
        
@csrf_exempt
def insertcoacategory(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.coa_category ORDER BY id ASC")
        data = cursor.fetchall()
    context = {"data": data}
    
    if request.method == "POST":
        
        id = request.POST.get('id')
        if id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT nextval('fin.coa_category_id_seq')")
                id = cursor.fetchone()[0]
        company_id = request.POST.get('company_id')
        category_code = request.POST.get('category_code') or ''.join([str(random.randint(0,9)) for _ in range(6)])
        category_name = request.POST.get('category_name')
        group_id = request.POST.get('group_id')
        
        if company_id is None:
            return JsonResponse({'status': 'error', 'message': 'Company ID is required'}, status=400)
        if category_code is None:
            return JsonResponse({'status': 'error', 'message': 'Category Code is required'}, status=400)
        if category_name is None:
            return JsonResponse({'status': 'error', 'message': 'Category Name is required'}, status=400)
        if group_id is None:
            return JsonResponse({'status':'error','message': 'group_id is Required'},status=400)
                                        

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO fin.coa_category (id, company_id, category_code, category_name, group_id)
                VALUES (%s, %s, %s, %s, %s)
            """, [id, company_id, category_code, category_name, group_id])
        
        # messages.success(request, "Data Terkirim")
        # return redirect('bankaccount')
    return JsonResponse(context)
    # return render(request, 'bankaccounttabel.html', context)
    
    

    
@csrf_exempt
def DeleteCoaCategory(request, id):
    if id is None:
        return JsonResponse({'status': 'error', 'message': 'ID is required'}, status=400)
    
    
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM fin.coa_category WHERE id = %s", [id])
    context = {"message": "data berhasil dihapus"}
    return JsonResponse(context)


@csrf_exempt
def UpdateCoaCategory(request, id):
    if request.method == "POST":

        # id = request.POST.get('id')
        # if id is None:
        #     return JsonResponse({'status': 'error', 'message': 'ID is required'}, status=400)
        company_id = request.POST.get('company_id')
        if company_id is None:
            return JsonResponse({'status': 'error', 'message': 'Company ID is required'}, status=400)
        category_code = request.POST.get('category_code')
        if category_code is None:
            return JsonResponse({'status': 'error', 'message': 'Category Code is required'}, status=400) 
        category_name = request.POST.get('category_name')
        if category_name is None:
            return JsonResponse({'status': 'error', 'message': 'Category Name is required'}, status=400)
        group_id = request.POST.get('group_id')
        if group_id is None:
            return JsonResponse({'status': 'error', 'message': 'Group ID is required'}, status=400)
        
        
        
      
    

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE fin.coa_category
                SET company_id = %s, category_code = %s, category_name = %s, group_id = %s
                WHERE id = %s
            """, [company_id, category_code, category_name, group_id, id])
        
        # messages.success(request, "Data berhasil di update")
        # return redirect('company')  

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.coa_category WHERE id = %s", [id])
        data = cursor.fetchone()
    
    context = {"data": data}
    return JsonResponse(context)
    
    # return render(request, 'update.html', context)
