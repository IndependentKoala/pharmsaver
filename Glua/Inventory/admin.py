from django.contrib import admin
from django.core.exceptions import PermissionDenied
from .models import Drug, Sale, Stocked, Measurement, LockedProduct, MarketingItem, IssuedItem, PickingList, Cannister, IssuedCannister, Client


class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch_no', 'stock', 'expiry_date', 'reorder_level')
    search_fields = ('name', 'batch_no')
    list_filter = ('expiry_date', 'stock')
    ordering = ('name',)


class SaleAdmin(admin.ModelAdmin):
    list_display = ('drug_sold', 'client', 'seller', 'date_sold', 'quantity', 'batch_no')
    search_fields = ('drug_sold', 'client__name', 'batch_no', 'legacy_client_name')
    list_filter = ('date_sold', 'client')
    readonly_fields = ('date_sold',)
    ordering = ('-date_sold',)


class StockedAdmin(admin.ModelAdmin):
    list_display = ('drug_name', 'number_added', 'supplier', 'staff', 'date_added')
    search_fields = ('drug_name__name', 'supplier')
    list_filter = ('date_added', 'staff')
    readonly_fields = ('date_added',)
    ordering = ('-date_added',)


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('name', 'expiry_date')
    search_fields = ('name',)
    list_filter = ('expiry_date',)
    ordering = ('name',)


class LockedProductAdmin(admin.ModelAdmin):
    list_display = ('drug', 'locked_by', 'date_locked', 'quantity', 'client')
    search_fields = ('drug__name', 'client__name')
    list_filter = ('date_locked', 'locked_by', 'client')
    readonly_fields = ('date_locked',)
    ordering = ('-date_locked',)

    def save_model(self, request, obj, form, change):
        # Check if the object is being updated (change == True)
        if change:
            original = LockedProduct.objects.get(pk=obj.pk)
            # If the product is locked, prevent any changes to it
            if original.date_locked and obj.drug != original.drug:
                raise PermissionDenied("Cannot update locked drugs.")

        # Call the parent method to save the object
        super().save_model(request, obj, form, change)


class MarketingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock')
    search_fields = ('name',)
    list_filter = ('stock',)
    ordering = ('name',)


class IssuedItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'issued_to', 'quantity_issued', 'issued_by', 'date_issued')
    search_fields = ('item', 'issued_to')
    list_filter = ('date_issued', 'issued_by')
    readonly_fields = ('date_issued',)
    ordering = ('-date_issued',)


class PickingListAdmin(admin.ModelAdmin):
    list_display = ('date', 'client', 'product', 'batch_no', 'quantity')
    search_fields = ('product', 'batch_no', 'client__name')
    list_filter = ('date', 'client')
    ordering = ('-date',)


class CanisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch_no', 'stock', 'litres')
    search_fields = ('name', 'batch_no')
    list_filter = ('stock',)
    ordering = ('name',)


class IssuedCanisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch_no', 'client', 'staff_on_duty', 'date_issued', 'action')
    search_fields = ('name', 'batch_no', 'client__name')
    list_filter = ('date_issued', 'staff_on_duty', 'client', 'action')
    readonly_fields = ('date_issued',)
    ordering = ('-date_issued',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'country_code', 'date_created')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('country_code', 'date_created')
    ordering = ('name',)


# Register all models with their custom admin classes
admin.site.register(Drug, DrugAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Stocked, StockedAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(LockedProduct, LockedProductAdmin)
admin.site.register(MarketingItem, MarketingItemAdmin)
admin.site.register(IssuedItem, IssuedItemAdmin)
admin.site.register(PickingList, PickingListAdmin)
admin.site.register(Cannister, CanisterAdmin)
admin.site.register(IssuedCannister, IssuedCanisterAdmin)
admin.site.register(Client, ClientAdmin)