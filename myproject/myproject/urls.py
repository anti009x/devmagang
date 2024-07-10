"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bankaccount import views

from django.urls import include, path
from taildiwndcss.views import taildwindcss
from company.views import company, insertDataCompany, DeleteDataCompany, UpdateDataCompany
from users.views import user, insertDataUser, DeleteDataUser
from login.views import login_view, logoutview, reset_password
from interestrate.views import interestrate, insertDataSukuBunga, DeleteDataSukuBunga, UpdateDataSukuBunga
from chartofaccount.views import coa, insertDataCoa, DeleteDataCoa
from coacategory.views import coacategory, insertcoacategory, DeleteCoaCategory, UpdateCoaCategory



urlpatterns = [
      
    path('admin/', admin.site.urls),
    
    #login
    path('login/', login_view, name='login'),
    path('logout/', logoutview, name='logout'),
    path('resetpassword/', reset_password, name='resetpassword'),
    
    #coa 
    path('coa/',coa,name ='coa'),
    path('coa/insert/', insertDataCoa, name='insert'),
    path('coa/delete/<int:id>', DeleteDataCoa, name='delete'),
    # path('coa/update/<int:id>', UpdateDataCoa, name='update'),
    
    #coacategory
    path ('coacategory/', coacategory, name='coacategory'),
    path('coacategory/insert/', insertcoacategory, name='insert'),
    path('coacategory/delete/<int:id>', DeleteCoaCategory, name='delete'),
    path ('coacategory/update/<int:id>', UpdateCoaCategory, name='update'),
    #Suku Bunga
    path('sukubunga/', interestrate, name='sukubunga'),
    path ('sukubunga/insert', insertDataSukuBunga, name='insert'),
    path ('sukubunga/delete/<int:id>', DeleteDataSukuBunga, name='delete'),
    path ('sukubunga/update/<int:id>', UpdateDataSukuBunga, name='update'),
    
    #BankAccount
    path('bankaccount/', views.index, name='bankaccount'),
    path('bankaccount/insert', views.insertData, name='insert'),
    path('bankaccount/delete/<int:id>', views.DeleteData, name='delete'),
    path('bankaccount/update/<int:bankacc_id>', views.UpdateData, name='update'),
    
    #Company
    path('company/', company, name='company'),
    path('company/insert', insertDataCompany, name='insert'),
    path('company/delete/<str:company_id>', DeleteDataCompany, name='delete'),
    path('company/update/<str:company_id>', UpdateDataCompany, name='update'),
    
    #user
    path ('users/',user,name='user'),
    path ('users/insert', insertDataUser, name='insert'),
    path ('users/delete/<int:user_id>', DeleteDataUser, name='delete'),
    # path ('users/update/<str:user_id>', UpdateDataUser, name='update'),
    
    
    

    path("__reload__/", include("django_browser_reload.urls")),
    path('taildwindcss/', taildwindcss, name='taildwindcss'),


]
