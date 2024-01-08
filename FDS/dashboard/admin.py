from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Register your models here.
from dashboard.models import Year, SectorName, Marketing, StageShare, Industry, Primary, IndustryCrossPrimary


class StageShareAdmin(admin.ModelAdmin):
    list_display = (
        'Sector',
        'Year',
        'FarmGate',
        'TransGate',
        'ProcessGate',
        'TradeGate',
    )
    
    list_editable = ('FarmGate','TransGate','ProcessGate','TradeGate')
    list_filter = ('Year', 'Sector__Name',)

class IndustryAdmin(admin.ModelAdmin):
    list_display = (
        "Year",
        "Sector",
        "Agribusiness",
        "FarmProduction",
        "FoodProcess",
        "Packaging",
        "Transportation",
        "WholesaleTrade",
        "RetailTrade",
        "Trade",
        "FoodService",
        "Energy",
        "FinanceInsurance",
        "Advertising",
        "Accounting",
    )
    
    list_editable = ("Agribusiness", "FarmProduction", "FoodProcess", "Packaging", "Transportation", 
                     "WholesaleTrade","RetailTrade", "Trade", "FoodService", "Energy","FinanceInsurance", 
                     "Advertising", "Accounting",)
    list_filter = ('Year', 'Sector__Name',)

class PrimaryAdmin(admin.ModelAdmin):
    list_display = (
        "Sector",
        "Year",
        "Compensation",
        "OperatingSurplus",
        "ConsumptionOfFixedCapital",
        "NetTaxes",
        "Adjustment",
        "Imports",
        
    )
    
    list_editable = ("Compensation", "OperatingSurplus", "ConsumptionOfFixedCapital", "NetTaxes",
                    "Adjustment", "Imports")
    list_filter = ('Year', 'Sector__Name',)

class MarketingAdmin(admin.ModelAdmin):
    list_display = (
        "Year",
        "Sector",
        "FarmShare",
        "MarketingShare",
    )
    
    list_editable = ("FarmShare", "MarketingShare",)
    list_filter = ('Year', 'Sector__Name',)

class IndustryCrossPrimaryAdmin(admin.ModelAdmin):
    list_display=(
        "Industry",
        "Compensation",
        "OperatingSurplus",
        "ConsumptionOfFixedCapital",
        "NetTaxes",
        "Imports",
        "Total",
    )
    
    list_editable = ("Compensation", "OperatingSurplus", "ConsumptionOfFixedCapital", "NetTaxes",
        "Imports", "Total",)
    list_filter = ("Industry",)

admin.site.register(Year)
admin.site.register(SectorName)
admin.site.register(StageShare,StageShareAdmin)
admin.site.register(Industry,IndustryAdmin)
admin.site.register(Primary,PrimaryAdmin)
admin.site.register(Marketing,MarketingAdmin)
admin.site.register(IndustryCrossPrimary,IndustryCrossPrimaryAdmin)
