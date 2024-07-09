from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



# Create your views here.

def interestrate(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.interest_rate ORDER BY id ASC")
        data = cursor.fetchall()
    # print(data) 
    # return 
    context = {"data": data}
    return JsonResponse(context)
    # return render(request, 'company.html', context)
    

@csrf_exempt
def insertDataSukuBunga(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.company ORDER BY company_id ASC")
        data = cursor.fetchall()
    context = {"data": data}
    
    if request.method == "POST":
        
        id = request.POST.get('id')
        if id is None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT nextval('fin.interest_rate_id_seq')")
                id = cursor.fetchone()[0]
        company_id = request.POST.get('company_id')
        opsi_key = request.POST.get('opsi_key')
        opsi_val = request.POST.get('opsi_val')
        
        if company_id is None:
            return JsonResponse({'status': 'error', 'message': 'Company ID is required'}, status=400)
        if opsi_key is None:
            return JsonResponse({'status': 'error', 'message': 'Opsi Key is required'}, status=400)
        if opsi_val is None:
            return JsonResponse({'status': 'error', 'message': 'Opsi Val is required'}, status=400)
                                 

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO fin.interest_rate (id, company_id, opsi_key, opsi_val)
                VALUES (%s, %s, %s, %s)
            """, [id, company_id, opsi_key, opsi_val])
        
        # messages.success(request, "Data Terkirim")
        # return redirect('bankaccount')
    return JsonResponse(context)
    # return render(request, 'bankaccounttabel.html', context)
    
@csrf_exempt
def DeleteDataSukuBunga(request, id):
    if id is None:
        return JsonResponse({'status': 'error', 'message': 'ID is required'}, status=400)
    
    
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM fin.interest_rate WHERE id = %s", [id])
    context = {"message": "data berhasil dihapus"}
    return JsonResponse(context)

    

@csrf_exempt
def UpdateDataSukuBunga(request, id):
    if request.method == "POST":

        # id = request.POST.get('id')
        # if id is None:
        #     return JsonResponse({'status': 'error', 'message': 'ID is required'}, status=400)
        company_id = request.POST.get('company_id')
        if company_id is None:
            return JsonResponse({'status': 'error', 'message': 'Company ID is required'}, status=400)
        opsi_key = request.POST.get('opsi_key')
        if opsi_key is None:
            return JsonResponse({'status': 'error', 'message': 'Opsi Key is required'}, status=400)
        opsi_val = request.POST.get('opsi_val')
        if opsi_val is None:
            return JsonResponse({'status': 'error', 'message': 'Opsi Val is required'}, status=400)
      
    

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE fin.interest_rate
                SET company_id = %s, opsi_key = %s, opsi_val = %s
                WHERE id = %s
            """, [company_id, opsi_key, opsi_val, id])
        
        # messages.success(request, "Data berhasil di update")
        # return redirect('company')  

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.interest_rate WHERE id = %s", [id])
        data = cursor.fetchone()
    
    context = {"data": data}
    return JsonResponse(context)
    
    # return render(request, 'update.html', context)
