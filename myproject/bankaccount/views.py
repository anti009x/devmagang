from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.bank_account ORDER BY bankacc_id ASC")
        data = cursor.fetchall()
    # print(data) 
    context = {"data": data}
    return render(request, 'bankaccounttabel.html', context)


@csrf_exempt
def UpdateData(request, bankacc_id):
    if request.method == "POST":
        bankacc_name = request.POST.get('bankacc_name')
        bankacc_number = request.POST.get('bankacc_number')
        coa_code = request.POST.get('coa_code')
        coa_name = request.POST.get('coa_name')
        acc_label = request.POST.get('acc_label')

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE fin.bank_account
                SET bankacc_name = %s, bankacc_number = %s, coa_code = %s, coa_name = %s, acc_label = %s
                WHERE bankacc_id = %s
            """, [bankacc_name, bankacc_number, coa_code, coa_name, acc_label, bankacc_id])
        
        messages.success(request, "Data berhasil di update")
        return redirect('bankaccount')  

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.bank_account WHERE bankacc_id = %s", [bankacc_id])
        data = cursor.fetchone()
    
    if not data:
        # context = {"data": "notfound"}
        data = 'NotFound'
        context = {"data": []}
    else:
        context = {"data": [data]}
    
    return render(request, 'update.html', context)
@csrf_exempt
def insertData(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM fin.bank_account")
        data = cursor.fetchall()
    context = {"data": data}
    
    if request.method == "POST":
        bankacc_id = request.POST.get('bankacc_id')
        company_id = request.POST.get('company_id')
        bankacc_name = request.POST.get('bankacc_name')
        bankacc_number = request.POST.get('bankacc_number')
        coa_id = request.POST.get('coa_id')
        coa_code = request.POST.get('coa_code')
        coa_name = request.POST.get('coa_name')
        acc_label = request.POST.get('acc_label')

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO fin.bank_account (bankacc_id, company_id, bankacc_name, bankacc_number, coa_id, coa_code, coa_name, acc_label)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, [bankacc_id, company_id, bankacc_name, bankacc_number, coa_id, coa_code, coa_name, acc_label])
        
        messages.success(request, "Data Terkirim")
        return redirect('bankaccount')

    return render(request, 'bankaccounttabel.html', context)

@csrf_exempt
def DeleteData(request, id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM fin.bank_account WHERE bankacc_id = %s", [id])
    messages.success(request, "data berhasil dihapus")
    return redirect('bankaccount')
