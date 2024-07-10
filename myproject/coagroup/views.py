from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import random

def coagroup(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.coa_group ORDER BY id ASC")
        data = cursor.fetchall()
    # print(data) 
    # return 
    context = {"data": data}
    return JsonResponse(context)
    # return render(request, 'company.html', context)\
        
@csrf_exempt
def insertcoagroup(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.coa_group ORDER BY id ASC")
        data = cursor.fetchall()
    context = {"data": data}
    
    if request.method == "POST":
        
        id = request.POST.get('id')
        if not id:
            with connection.cursor() as cursor:
                cursor.execute("SELECT COALESCE(MAX(id)::integer, 0) FROM fin.coa_group")
                id = cursor.fetchone()[0]
        else:
            try:
                id = int(id)
            except ValueError:
                return JsonResponse({'status': 'error', 'message': 'Invalid ID format'}, status=400)
        id += 99999
        description = request.POST.get('description')
        report_type = request.POST.get('report_type')
        flag_report = request.POST.get('flag_report')
        
        if description is None:
            return JsonResponse({'status': 'error', 'message': 'Description is required'}, status=400)
        if report_type is None:
            return JsonResponse({'status': 'error', 'message': 'Category Code is required'}, status=400)
        if flag_report is None:
            return JsonResponse({'status': 'error', 'message': 'Category Name is required'}, status=400)
        
                                        

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO fin.coa_group (id, description, report_type, flag_report)
                VALUES (%s, %s, %s, %s)
            """, [id, description, report_type, flag_report])
        
        # messages.success(request, "Data Terkirim")
        # return redirect('bankaccount')
    return JsonResponse(context)
    # return render(request, 'bankaccounttabel.html', context)
    
    

    
@csrf_exempt
def deletecoagroup(request, id):
    if id is None:
        return JsonResponse({'status': 'error', 'message': 'ID is required'}, status=400)
    
    
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM fin.coa_group WHERE id = %s", [id])
    context = {"message": "data berhasil dihapus"}
    return JsonResponse(context)


@csrf_exempt
def updatecoagroup(request, id):
    if request.method == "POST":

        # id = request.POST.get('id')
        # if id is None:
        #     return JsonResponse({'status': 'error', 'message': 'ID is required'}, status=400)
        description = request.POST.get('description')
        if description is None or description == '':
            return JsonResponse({'status': 'error', 'message': 'Description is required'}, status=400)
        report_type = request.POST.get('report_type')
        if report_type is None or report_type == '':
            return JsonResponse({'status': 'error', 'message': 'report type is required'}, status=400) 
        flag_report = request.POST.get('flag_report')
        if flag_report is None or flag_report == '':
            return JsonResponse({'status': 'error', 'message': 'flag report is required'}, status=400)
        
        
        
      
    

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE fin.coa_group
                SET description = %s, report_type = %s, flag_report = %s
                WHERE id = %s
            """, [description, report_type, flag_report, id])
        
        # messages.success(request, "Data berhasil di update")
        # return redirect('company')  

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.coa_group WHERE id = %s", [id])
        data = cursor.fetchone()
    
    context = {"data": data}
    return JsonResponse(context)
    
    # return render(request, 'update.html', context)
