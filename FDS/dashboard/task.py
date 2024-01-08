from .utils import fetchRawData, importStageShare, importIndustry, importPrimary, importMarketing, updateIndustryCrossPrimary
from dashboard.models import Year, SectorName
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

def importNewData():
    StageData = fetchRawData(sheet_id="1vo1rTVqDO9_4xhylvG6w8OaEZb_CtmgC", sheet_name='stage')
    IndustryData = fetchRawData(sheet_id="1vo1rTVqDO9_4xhylvG6w8OaEZb_CtmgC", sheet_name='industry')
    PrimaryData = fetchRawData(sheet_id="1vo1rTVqDO9_4xhylvG6w8OaEZb_CtmgC", sheet_name='primary')
    TableData = fetchRawData(sheet_id="1vo1rTVqDO9_4xhylvG6w8OaEZb_CtmgC", sheet_name='latest')
    marketingData = fetchRawData(sheet_id="1vo1rTVqDO9_4xhylvG6w8OaEZb_CtmgC", sheet_name="marketing")
    for year in list(set(StageData['year'])):
        try:
            Year.objects.get(Year = year)
        except ObjectDoesNotExist:
            Year.objects.create(Year = year)
            updateIndustryCrossPrimary(TableData)
        importStageShare(StageData, year)
        importIndustry(IndustryData, year)
        importPrimary(PrimaryData,year)
        importMarketing(marketingData,year)
        
    return True