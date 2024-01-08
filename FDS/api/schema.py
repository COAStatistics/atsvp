import graphene 
from graphene_django import DjangoObjectType, DjangoListField
from dashboard.models import Year, SectorName, StageShare, Marketing, Industry, Primary

class YearType(DjangoObjectType):
    class Meta:
        model = Year
        fields = ("Year",)

class SectorType(DjangoObjectType):
    class Meta:
        model = SectorName
        field = ('Name',)

class StageShareType(DjangoObjectType):
    class Meta:
        model = StageShare
        fields = (
            'id',
            'FarmGate',
            'TransGate',
            'ProcessGate',
            'TradeGate',
            'Sector',
            'Year',
        )

class MarketingType(DjangoObjectType):
    class Meta:
        model = Marketing
        fields = (
            "FarmShare",
            "MarketingShare",
            "Sector",
            "Year"
        )

class IndustryType(DjangoObjectType):
    class Meta:
        model = Industry
        fields = (
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
            "Sector",
            "Year"
        )

class PrimaryType(DjangoObjectType):
    class Meta:
        model = Primary
        fields = (
            "Compensation",
            "OperatingSurplus",
            "ConsumptionOfFixedCapital",
            "NetTaxes",
            "Imports",
            "Adjustment",
            "Sector",
            "Year"
        )

class Query(graphene.ObjectType):
    allYears = graphene.List(YearType)
    stageshare_by_year_and_sector = graphene.List(StageShareType, year=graphene.Int(required=True), sector=graphene.String(required=False))
    marketing_by_year_and_sector = graphene.List(MarketingType, year=graphene.Int(required=True), sector=graphene.String(required=False))
    industry_by_year_and_sector = graphene.List(IndustryType, year=graphene.Int(required=True), sector=graphene.String(required=False))
    primary_by_year_and_sector = graphene.List(PrimaryType, year=graphene.Int(required=True), sector=graphene.String(required=False))

    def resolve_allYears(root, info):
        return Year.objects.all()

    def resolve_stageshare_by_year_and_sector(root, info, year, sector):
        if sector:
            return StageShare.objects.filter(Year__Year=year, Sector__Name=sector)
        elif sector == "":
            return StageShare.objects.filter(Year__Year=year)
        else:
            return None
        
    def resolve_marketing_by_year_and_sector(root, info, year, sector):
        try:
            return Marketing.objects.filter(Year__Year=year, Sector__Name=sector)
        except Marketing.DoesNotExist:
            return None
        
    def resolve_industry_by_year_and_sector(root, info, year, sector):
        try:
            return Industry.objects.filter(Year__Year=year, Sector__Name=sector)
        except Industry.DoesNotExist:
            return None
        
    def resolve_primary_by_year_and_sector(root, info, year, sector):
        try:
            return Primary.objects.filter(Year__Year=year, Sector__Name=sector)
        except Primary.DoesNotExist:
            return None

schema = graphene.Schema(query = Query,)