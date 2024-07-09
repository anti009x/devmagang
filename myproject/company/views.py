from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def company(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.company ORDER BY company_id ASC")
        data = cursor.fetchall()
    # print(data) 
    # return 
    context = {"data": data}
    return JsonResponse(context)
    # return render(request, 'company.html', context)
    
    
@csrf_exempt
def insertDataCompany(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.company ORDER BY company_id ASC")
        data = cursor.fetchall()
    context = {"data": data}
    
    if request.method == "POST":
        company_id = request.POST.get('company_id')
        company_name = request.POST.get('company_name')
        com_abbr = request.POST.get('com_abbr')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        contact_person = request.POST.get('contact_person')
        address = request.POST.get('address')
        city = request.POST.get('city')
        province = request.POST.get('province')
        postal_code = request.POST.get('postal_code')
        fax = request.POST.get('fax')
        website = request.POST.get('website')
                                 

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO public.company (company_id, company_name, com_abbr, phone, email, contact_person, address, city, province, postal_code, fax, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, [company_id, company_name, com_abbr, phone, email, contact_person, address, city, province, postal_code, fax, website])
        
        # messages.success(request, "Data Terkirim")
        # return redirect('bankaccount')
    return JsonResponse(context)
    # return render(request, 'bankaccounttabel.html', context)
    
    
@csrf_exempt
def DeleteDataCompany(request, company_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM public.company WHERE company_id = %s", [company_id])
    context = {"message": "data berhasil dihapus"}
    return JsonResponse(context)


@csrf_exempt
def UpdateDataCompany(request, company_id):
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        com_abbr = request.POST.get('com_abbr')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        contact_person = request.POST.get('contact_person')
        address = request.POST.get('address')
        city = request.POST.get('city')
        province = request.POST.get('province')
        postal_code = request.POST.get('postal_code')
        fax = request.POST.get('fax')
        website = request.POST.get('website')
    

        # Simpan data ke dalam database
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE public.company
                SET company_name = %s, com_abbr = %s, phone = %s, email = %s, contact_person = %s, address = %s, city = %s, province = %s, postal_code = %s, fax = %s, website = %s
                WHERE company_id = %s
            """, [company_name, com_abbr, phone, email, contact_person, address, city, province, postal_code, fax, website, company_id])
        
        # messages.success(request, "Data berhasil di update")
        # return redirect('company')  

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.company WHERE company_id = %s", [company_id])
        data = cursor.fetchone()
    
    context = {"data": data}
    return JsonResponse(context)
    
    # return render(request, 'update.html', context)
