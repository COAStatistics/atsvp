from .models import Year, SectorName, Industry, Primary, StageShare, Marketing, IndustryCrossPrimary
import pandas as pd
from django.conf import settings
import environ
import os
from django.core.exceptions import ObjectDoesNotExist

env = environ.Env()
environ.Env.read_env()
environ.Env.read_env(os.path.join(settings.BASE_DIR, '.env'))
file_url = env.str('File_url')

def fetchRawData(sheet_id, sheet_name):
    url = file_url.replace('sheet_id', sheet_id).replace('sheet_name', sheet_name)
    data = pd.read_csv(url)
    data = data[data[data.columns[:4]].notnull().all(axis=1)]
    return data

def importStageShare(data, year):
    data = data.query('year == %s' % year)
    data = data.fillna(0)
    cols = data.columns[3:]
    year = Year.objects.get(Year=year)
    for i in range(len(data)):
        try:
            sector = SectorName.objects.get(Name=data['ioName'].iloc[i])
        except ObjectDoesNotExist:
            sector = SectorName(Name=data['ioName'].iloc[i])
            sector.save()
        stage_share = StageShare(
            FarmGate=data[cols[0]].iloc[i],TransGate=data[cols[1]].iloc[i],
            ProcessGate=data[cols[2]].iloc[i],TradeGate=data[cols[3]].iloc[i],
            Year=year,Sector=sector)
        stage_share.save()
    return 'Done'

def importIndustry(data, year):
    data = data.query('year == %s' % year)
    data = data.fillna(0)
    cols = data.columns[3:]
    year = Year.objects.get(Year=year)
    for i in range(len(data)):
        try:
            sector = SectorName.objects.get(Name=data['ioName'].iloc[i])
        except ObjectDoesNotExist:
            sector = SectorName(Name=data['ioName'].iloc[i])
            sector.save()
        industry = Industry(
            Agribusiness=data[cols[0]].iloc[i], FarmProduction=data[cols[1]].iloc[i],
            FoodProcess=data[cols[2]].iloc[i], Packaging=data[cols[3]].iloc[i],
            Transportation=data[cols[4]].iloc[i], WholesaleTrade=data[cols[5]].iloc[i],
            RetailTrade=data[cols[6]].iloc[i], Trade=data[cols[7]].iloc[i],
            FoodService=data[cols[8]].iloc[i], Energy=data[cols[9]].iloc[i], 
            FinanceInsurance=data[cols[10]].iloc[i], Advertising=data[cols[11]].iloc[i], 
            Accounting=data[cols[12]].iloc[i],Year=year, Sector=sector)
        industry.save()
    return 'Done'

def importPrimary(data, year):
    data = data.query('year == %s' % year)
    data = data.fillna(0)
    cols = data.columns[3:]
    year = Year.objects.get(Year=year)
    for i in range(len(data)):
        try:
            sector = SectorName.objects.get(Name=data['ioName'].iloc[i])
        except ObjectDoesNotExist:
            sector = SectorName(Name=data['ioName'].iloc[i])
            sector.save()
        primary = Primary(
            Compensation=data[cols[0]].iloc[i], OperatingSurplus=data[cols[1]].iloc[i],
            ConsumptionOfFixedCapital=data[cols[2]].iloc[i], NetTaxes=data[cols[3]].iloc[i],
            Adjustment=data[cols[4]].iloc[i], Imports=data[cols[5]].iloc[i], 
            Year=year,Sector=sector)
        primary.save()
    return 'Done'

def importMarketing(data, year):
    data = data.query('year == %s' % year)
    data = data.fillna(0)
    cols = data.columns[3:]
    year = Year.objects.get(Year=year)
    for i in range(len(data)):
        try:
            sector = SectorName.objects.get(Name=data['ioName'].iloc[i])
        except ObjectDoesNotExist:
            sector = SectorName(Name=data['ioName'].iloc[i])
            sector.save()
        marketingShare = Marketing(
            FarmShare=data[cols[0]].iloc[i], MarketingShare=data[cols[1]].iloc[i], 
            Year=year, Sector=sector)
        marketingShare.save()
    return 'Done'

def updateIndustryCrossPrimary(data):
    cols = data.columns
    for i in range(len(data)):
        Row = IndustryCrossPrimary.objects.get(Industry=data[cols[0]].iloc[i])
        Row.Compensation = data[cols[1]].iloc[i]
        Row.OperatingSurplus = data[cols[2]].iloc[i]
        Row.ConsumptionOfFixedCapital = data[cols[3]].iloc[i]
        Row.NetTaxes = data[cols[4]].iloc[i]
        Row.Imports = data[cols[5]].iloc[i]
        Row.Total = data[cols[6]].iloc[i]
        Row.save()
    return 'Done'