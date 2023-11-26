
from django.db import models
    
class Full_Contract(models.Model):
    ID = models.AutoField(primary_key=True)
    Full_Contract_Code = models.CharField(max_length=50, blank=True, editable=False)
    Customer_Name = models.CharField(max_length=50)
    Year_Of_Birth = models.IntegerField()
    SSN = models.CharField(max_length=15)
    Customer_Address = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=15)
    Property_ID = models.IntegerField()
    Date_Of_Contract = models.DateField()
    Price = models.DecimalField(max_digits=18, decimal_places=0)
    Deposit = models.DecimalField(max_digits=18, decimal_places=0)
    Remain = models.DecimalField(max_digits=18, decimal_places=0)
    Status = models.BooleanField()

    def __str__(self):
        return f"{self.ID} - {self.Full_Contract_Code} - {self.Customer_Name}"
    
    def save(self, *args, **kwargs):
        if not self.Full_Contract_Code and not self.ID:
            super().save(*args, **kwargs)

            month = self.Date_Of_Contract.month
            year = self.Date_Of_Contract.year
            formatted_id = str(self.ID).zfill(5)
            self.Full_Contract_Code = f"PPC{year}{month}{formatted_id}"
        
        super().save(*args, **kwargs)

class Property(models.Model):
    ID = models.AutoField(primary_key=True)
    Property_Code = models.CharField(max_length=15, blank=True, editable=False)
    Property_Name = models.CharField(max_length=50)
    Property_Type_ID = models.IntegerField()
    Description = models.CharField(max_length=1000)
    District_ID = models.IntegerField()
    Mobile = models.CharField(max_length=15)
    Property_ID = models.IntegerField()
    Address = models.CharField(max_length=100)
    Area = models.IntegerField()
    Bed_Room = models.IntegerField()
    Bath_Room = models.IntegerField()
    Price = models.DecimalField(max_digits=18, decimal_places=0)
    Installment_Rate = models.FloatField()
    Avatar = models.ImageField(upload_to='images', blank=True, null=True)
    Album = models.ImageField(upload_to='images', blank=True, null=True)
    Property_Status_ID = models.IntegerField()

    def __str__(self):
        return f"{self.ID} - {self.Property_Code} - {self.Property_Name}"
    
    def save(self, *args, **kwargs):
        if not self.Property_Code and not self.ID:
            super().save(*args, **kwargs)
            formatted_id = str(self.ID).zfill(5)
            self.Property_Code = f"PPC2300{formatted_id}"
        
        super().save(*args, **kwargs)

class Invoice(models.Model):
    contract = models.OneToOneField(Full_Contract, on_delete=models.CASCADE, default="")
    property = models.OneToOneField(Property, on_delete=models.CASCADE, default="")