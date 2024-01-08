from django.conf import settings


def ga_tracking_id(request):
    try:
        return {'ga_tracking_id': settings.GA_TRACKING_ID}
    except AttributeError:
        return {'ga_tracking_id': ''}


def use_ga(request):
    try:
        return {'use_ga': settings.USE_GA}
    except AttributeError:
        return {'use_ga', False}


def aprp_version(request):
    try:
        return {'aprp_version': settings.APRP_VERSION}
    except AttributeError:
        return {'aprp_version': None}

def tableau_update_year(request):
    try:
        return {'tableau_update_year': settings.TABLEAU_UPDATE_YEAR}
    except AttributeError:
        return {'tableau_update_year': ''}

def tableau_update_month(request):
    try:
        return {'tableau_update_month': settings.TABLEAU_UPDATE_MONTH}
    except AttributeError:
        return {'tableau_update_month': ''}

def web_name(request):
    try:
        return {'web_name': settings.WEB_NAME}
    except AttributeError:
        return {'web_name': ''}