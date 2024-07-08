# from django.db import models

# # Create your models here.
# class BankAccount(models.Model):
    # bankacc_id = models.AutoField(primary_key=True)
    # company_id = models.CharField(max_length=10)
    # bankacc_name = models.CharField(max_length=100)
    # bankacc_number = models.CharField(max_length=20, unique=True)
    # coa_id = models.IntegerField()
    # coa_code = models.CharField(max_length=10)
    # coa_name = models.CharField(max_length=100)
    # acc_label = models.CharField(max_length=10)

#     class Meta:
#         db_table = 'fin.bank_account'  # Specify the schema and table name

#     def __str__(self):
#         return f"{self.bankacc_name} - {self.bankacc_number}"