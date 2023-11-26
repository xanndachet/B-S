from django.contrib import admin
from homepage.models import Full_Contract, Property, Invoice

class estateAdmin(admin.ModelAdmin):
    list_display = ['ID']
    search_fields = ['ID']
    list_filter = ['ID']
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['get_full_contract_code', 'get_property_code']

    def get_full_contract_code(self, obj):
        return obj.contract.Full_Contract_Code

    get_full_contract_code.short_description = 'Full_Contract_Code'

    def get_property_code(self, obj):
        return obj.property.Property_Code

    get_property_code.short_description = 'Property_Code'

admin.site.register(Invoice, InvoiceAdmin)

admin.site.register(Full_Contract, estateAdmin)
admin.site.register(Property, estateAdmin)

