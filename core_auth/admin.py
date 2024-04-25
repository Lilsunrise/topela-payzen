from django.contrib import admin
from .models import Address, Account, Party, Client, Pro, Intermediary, BusinessRelationship, BusinessAgreement, Offer, SaaSWork

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'zipcode', 'town')
    search_fields = ('street', 'zipcode', 'town')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'gender', 'status')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('gender', 'status')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'ctype')
    search_fields = ('name', 'ctype')
    list_filter = ('ctype',)

@admin.register(Pro)
class ProAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'subscribed')
    search_fields = ('name', 'company_name')
    list_filter = ('subscribed',)

@admin.register(Intermediary)
class IntermediaryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(BusinessRelationship)
class BusinessRelationshipAdmin(admin.ModelAdmin):
    list_display = ('intermediary', 'provider', 'consumer', 'nature', 'status')
    search_fields = ('intermediary__name', 'provider__name', 'consumer__name')
    list_filter = ('nature', 'status')

@admin.register(BusinessAgreement)
class BusinessAgreementAdmin(admin.ModelAdmin):
    list_display = ('business_relationship', 'nature', 'status')
    search_fields = ('business_relationship__intermediary__name', 'business_relationship__provider__name', 'business_relationship__consumer__name')
    list_filter = ('nature', 'status')

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'pricing', 'duration', 'recurrent_payment_date')
    search_fields = ('title',)
    list_filter = ('duration',)

@admin.register(SaaSWork)
class SaaSWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'business_agreement', 'proposal', 'status', 'worktype', 'work_start_date', 'work_end_date')
    search_fields = ('title',)
    list_filter = ('status', 'worktype')
