from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import random

def coaheader(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.coa_header ORDER BY id ASC")
        data = cursor.fetchall()
    # print(data) 
    # return 
    context = {"data": data}
    return JsonResponse(context)
    # return render(request, 'company.html', context)\
       
@csrf_exempt
def insertcoaheader(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.coa_header ORDER BY id ASC")
        data = cursor.fetchall()
    context = {"data": data}
    
    if request.method == "POST":
        
        id = request.POST.get('id')
        if id is None or id == '':
            with connection.cursor() as cursor:
                cursor.execute("SELECT COALESCE(MAX(id)::integer, 0) FROM fin.coa_header")
                id = cursor.fetchone()[0] + 1
        company_id = request.POST.get('company_id')
        header_code = request.POST.get('header_code')
        header_name = request.POST.get('header_name')
        category_id = request.POST.get('category_id')
        
        if company_id is None or company_id == '':
            return JsonResponse({'status': 'error', 'message': 'company id is required'}, status=400)
        if header_code is None or header_code == '':
            return JsonResponse({'status': 'error', 'message': 'header code is required'}, status=400)
        if header_name is None or header_name == '':
            return JsonResponse({'status': 'error', 'message': 'header name is required'}, status=400)
        if category_id is None or category_id == '':
            return JsonResponse({'status': 'error', 'message': 'category id is required'}, status=400)
        
                                        

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO fin.coa_header (id, company_id, header_code, header_name, category_id)
                VALUES (%s, %s, %s, %s, %s)
            """, [id, company_id, header_code, header_name, category_id])
        
        # messages.success(request, "Data Terkirim")
        # return redirect('bankaccount')
    return JsonResponse(context)
    # return render(request, 'bankaccounttabel.html', context)

    
@csrf_exempt
def deletecoaheader(request, id):
    if id is None:
        return JsonResponse({'status': 'error', 'message': 'ID is required'}, status=400)
    
    
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM fin.coa_header WHERE id = %s", [id])
    context = {"message": "data berhasil dihapus"}
    return JsonResponse(context)


@csrf_exempt
def updatecoaheader(request, id):
    if request.method == "POST":

        # id = request.POST.get('id')
        # if id is None:
        #     return JsonResponse({'status': 'error', 'message': 'ID is required'}, status=400)
        company_id = request.POST.get('company_id')
        if company_id is None or company_id == '':
            return JsonResponse({'status': 'error', 'message': 'company id is required'}, status=400)
        header_code = request.POST.get('header_code')
        if header_code is None or header_code == '':
            return JsonResponse({'status': 'error', 'message': 'header code is required'}, status=400) 
        header_name = request.POST.get('header_name')
        if header_name is None or header_name == '':
            return JsonResponse({'status': 'error', 'message': 'header name is required'}, status=400)
        
        
        
        
      
    

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE fin.coa_header
                SET company_id = %s, header_code = %s, header_name = %s
                WHERE id = %s
            """, [company_id, header_code, header_name, id])
        
        # messages.success(request, "Data berhasil di update")
        # return redirect('company')  

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.coa_header WHERE id = %s", [id])
        data = cursor.fetchone()
    
    context = {"data": data}
    return JsonResponse(context)
    
    # return render(request, 'update.html', context)
