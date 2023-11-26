from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from homepage.models import Full_Contract, Property, Invoice


def home(request):

    invoices = Invoice.objects.all()

    data = []

    for invoice in invoices:

        # contract
        full_contract_code = invoice.contract.Full_Contract_Code
        customer_name = invoice.contract.Customer_Name   
        id = invoice.contract.ID    
        year_of_birth =invoice.contract.Year_Of_Birth
        ssn = invoice.contract.SSN
        customer_address = invoice.contract.Customer_Address
        mobile = invoice.contract.Mobile
        property_id = invoice.contract. Property_ID
        date_of_contract = invoice.contract.Date_Of_Contract
        price = invoice.contract.Price
        deposit = invoice.contract.Deposit
        remain = invoice.contract.Remain
        status = invoice.contract.Status
        

        # property
        id = invoice.property.ID
        property_name = invoice.property.Property_Name
        property_code = invoice.property.Property_Code
        property_type_id = invoice.property.Property_Type_ID
        description = invoice.property.Description
        district_id = invoice.property.District_ID
        mobile = invoice.property.Mobile
        property_id = invoice.property.Property_ID
        address = invoice.property.Address
        area = invoice.property.Area
        bedroom = invoice.property.Bed_Room
        bathroom = invoice.property.Bath_Room
        price = invoice.property.Price
        installment_rate = invoice.property.Installment_Rate
        avatar = invoice.property.Avatar
        album = invoice.property.Album
        property_status_id = invoice.property.Property_Status_ID


        

        
        data.append({
            
            # contract
            'id': id,
            'full_contract_code': full_contract_code,
            'customer_name': customer_name,
            'year_of_birth': year_of_birth,
            'ssn' : ssn,
            'customer_address':  customer_address,
            'mobile': mobile,
            'property_id': property_id,
            'date_of_contract': date_of_contract,
            'price': price,
            'deposit': deposit,
            'remain': remain,
            'status': status,

            # property
            'id': id,
            'property_name': property_name, 
            'property_code': property_code,
            'property_type_id' : property_type_id,
            'description': description,
            'district_id': district_id,
            'mobile': mobile,
            'property_id' : property_id,
            'address':  address,
            'area': area,
            'bedroom': bedroom,
            'bathroom' : bathroom,
            'price' :  price,
            'installment_rate': installment_rate,
            'avatar' :  avatar,
            'album': album,
            'property_status_id': property_status_id


            })

    return render(request, 'index.html', {'data': data})