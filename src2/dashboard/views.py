import json
import os
import re
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# from django.http import JsonResponse, HttpResponseRedirect
# from django.conf import settings
# from django.utils import translation
from django.shortcuts import (
    redirect,
    render,
)
from .Tableau_url.Tableau_url_forDjango import runall
from bs4 import BeautifulSoup as bs
import requests

# from functools import wraps
# from .utils import (
#     jarvismenu_extra_context,
#     product_selector_ui_extra_context,
#     watchlist_base_chart_tab_extra_context,
#     chart_tab_extra_context,
#     watchlist_base_chart_contents_extra_context,
#     product_selector_base_extra_context,
#     watchlist_base_integration_extra_context,
#     product_selector_base_integration_extra_context,
# )
# from apps.watchlists.models import Watchlist
# from apps.configs.models import (
#     Config,
#     Chart,
#     Type,
# )

# def query(view):
#     extra_context = dict()

#     # Query params
#     params = view.request.GET
#     department = params.get('department')
#     print('query_department=',department)
#     dollar = params.get('dollar')
#     print('query_dollar=',dollar)
#     date_range = params.get('date_range')
#     print('query_date_range=',date_range)

#     return extra_context


# def login_required(view):
#     """
#     Custom login_required to handle ajax request
#     Check user is login and is_active
#     """
#     @wraps(view)
#     def inner(request, *args, **kwargs):
#         if not request.user.is_authenticated() or not request.user.is_active:
#             if request.is_ajax():
#                 # if is ajax return 403
#                 return JsonResponse({'login_url': settings.LOGIN_URL}, status=403)
#             else:
#                 # if not ajax redirect login page
#                 return redirect(settings.LOGIN_URL)
#         return view(request, *args, **kwargs)
#     return inner


# class LoginRequiredMixin(object):
#     @classmethod
#     def as_view(cls, **kwds):
#         return login_required(super().as_view(**kwds))


class BrowserNotSupport(TemplateView):
    redirect_field_name = 'redirect_to'
    template_name = 'browser-not-support.html'


class Index(TemplateView):
    redirect_field_name = 'redirect_to'
    template_name = 'index.html'


class About(TemplateView):
    redirect_field_name = 'redirect_to'
    template_name = 'ajax/about.html'


# class DailyReport(LoginRequiredMixin, TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'ajax/daily-report.html'


# class ProductSelector(LoginRequiredMixin, TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'ajax/product-selector.html'

#     def get_context_data(self, **kwargs):
#         context = super(ProductSelector, self).get_context_data(**kwargs)
#         context['configs'] = Config.objects.order_by('id')
#         context['types'] = Type.objects.order_by('id')
#         return context


# class ProductSelectorUI(LoginRequiredMixin, TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'ajax/product-selector-ui.html'

#     def post(self, request, **kwargs):
#         self.kwargs['POST'] = request.POST
#         return self.render_to_response(self.get_context_data())

#     def get_context_data(self, **kwargs):
#         context = super(ProductSelectorUI, self).get_context_data(**kwargs)
#         extra_context = product_selector_ui_extra_context(self)
#         context.update(extra_context)
#         return context


# class JarvisMenu(LoginRequiredMixin, TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'ajax/jarvismenu.html'

#     def get_context_data(self, **kwargs):
#         context = super(JarvisMenu, self).get_context_data(**kwargs)
#         extra_context = jarvismenu_extra_context(self)
#         context.update(extra_context)
#         return context


# class ChartTabs(LoginRequiredMixin, TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'ajax/chart-tab.html'
#     watchlist_base = False

#     def get_context_data(self, **kwargs):
#         context = super(ChartTabs, self).get_context_data(**kwargs)
#         if self.watchlist_base:
#             extra_context = watchlist_base_chart_tab_extra_context(self)
#         else:
#             extra_context = chart_tab_extra_context(self)
#         context.update(extra_context)
#         return context


# class ChartContents(LoginRequiredMixin, TemplateView):
#     redirect_field_name = 'redirect_to'
#     no_data = False  # custom
#     watchlist_base = False
#     product_selector_base = False

#     def get_template_names(self):
#         if self.no_data:
#             return 'ajax/no-data.html'
#         else:
#             chart_id = self.kwargs.get('ci')
#             chart = Chart.objects.get(id=chart_id)
#             return chart.template_name

#     def post(self, request, **kwargs):
#         self.kwargs['POST'] = request.POST
#         return self.render_to_response(self.get_context_data())

#     def get_context_data(self, **kwargs):
#         context = super(ChartContents, self).get_context_data(**kwargs)
#         if self.watchlist_base:
#             extra_context = watchlist_base_chart_contents_extra_context(self)
#             context.update(extra_context)
#         elif self.product_selector_base:
#             extra_context = product_selector_base_extra_context(self)
#             context.update(extra_context)

#         # no data checking, if series_options is empty, render no-data template
#         if not context['series_options']:
#             self.no_data = True

#         return context


# class IntegrationTable(LoginRequiredMixin, TemplateView):
#     redirect_field_name = 'redirect_to'
#     no_data = False  # custom
#     to_init = True  # custom  # default is True
#     watchlist_base = False
#     product_selector_base = False

#     def get_template_names(self):
#         # set template_name if no assign yet

#         if self.no_data:
#             return 'ajax/no-data.html'

#         if self.to_init:
#             return 'ajax/integration-panel.html'
#         else:
#             return 'ajax/integration-row.html'

#     def post(self, request, **kwargs):
#         self.kwargs['POST'] = request.POST
#         return self.render_to_response(self.get_context_data())

#     def get_context_data(self, **kwargs):
#         context = super(IntegrationTable, self).get_context_data(**kwargs)
#         if self.watchlist_base:
#             extra_context = watchlist_base_integration_extra_context(self)
#             context.update(extra_context)
#         elif self.product_selector_base:
#             extra_context = product_selector_base_integration_extra_context(
#                 self)
#             context.update(extra_context)

#         # no data checking, if series_options or option is empty, render no-data template
#         if self.to_init:
#             if not context['series_options']:
#                 self.no_data = True
#         else:
#             if not context['option']:
#                 self.no_data = True

#         return context
# class GetTableauServerTicket(TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'gettableauserverticket.html'

#     def get_context_data(self, **kwargs):
#         context = super(GetTableauServerTicket, self).get_context_data(**kwargs)
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',}
#         data = {
#             'username':'CoaStat',
#             'server':'https://bigdata.coa.gov.tw',
#             'client_ip':'132.145.121.250',
#             'target_site':'stattab',
#             'submittable':'Get Ticket',
#         }
#         session = requests.Session()
#         response = session.post('https://bigdata.coa.gov.tw/trusted', headers=headers, data=data)
#         soup = bs(response.text, 'html.parser')
#         # context['Ticket'] = str(soup)
#         return str(soup)
def getTicket():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',}
    data = {
        'username':'Coasta',
        'server':'https://bigdata.moa.gov.tw',
        'client_ip':'125.227.27.199',
        'target_site':'stattab',
        'submittable':'Get Ticket',
    }
    session = requests.Session()
    response = session.post('https://bigdata.moa.gov.tw/trusted', headers=headers, data=data)
    soup = bs(response.text, 'html.parser')
    ticket = str(soup)
    return ticket

def replaceTicket(embed_code):
    pattern = re.compile("<param name='ticket' value='(.*)'/")
    old_ticket = re.findall(pattern,embed_code)[0]
    new_ticket = getTicket()
    # print('old_ticket=',old_ticket)
    # print('new_ticket=',new_ticket)
    if new_ticket == '-1':
        print('get Tableau Server Ticket error')
        return None
    new_embed_code = embed_code.replace(old_ticket,new_ticket)
    return new_embed_code


class Tableau_base(TemplateView):
    '''子類別所需的重要/共同資料，組織在父類變數'''
    # --1.讀全部嵌入碼(coa\src\dashboard\Tableau_url.json)
    file_path = os.path.join(os.path.dirname(__file__), 'Tableau_url_server.json')
    with open(file_path, 'r', encoding='utf-8') as json_file:
        wb_dict = json.loads(json_file.read())
    # --2.其他
    redirect_field_name = 'redirect_to'
    # 定義每個選單按鈕對應的預設模板
    template_names = [
        'tableau1_1_1.html',
        'tableau2_1_1.html',
        'tableau3_1_1.html',
        'tableau4_1_1.html',
        # 'tableau5_1_1.html',
        # 'tableau6_1_1.html',
        # 'tableau7_1_1.html',
        # 'tableau8_1_1.html',
    ]
    # 每個form的四種嵌入碼，由子類override
    post_embed_code = None

    @classmethod
    def reload_json(cls, request, refresh):
        '''
        根據refresh的值，更新父類變數wb_dict
        0: http://DNS/tableau_reloadjson/0/，手動小編輯views.py旁邊的json檔，用此網址重讀json並更新class變數
        1: http://DNS/tableau_reloadjson/1/，執行selenium全部重爬，在Tableau_url目錄裡重造Tableau_url_inner.json
        2: http://DNS/tableau_reloadjson/2/，將Tableau_url目錄裡的json更新到外面，並重讀
        '''
        # print('refresh=',refresh)
        if refresh == '0':
            with open(cls.file_path, 'r', encoding='utf-8') as json_file:
                cls.wb_dict = json.loads(json_file.read())
            #
            return HttpResponse('Tableau_url.json 重讀完畢')
        elif refresh == '1':
            try:
                runall()
                #
                return HttpResponse('Tableau_url.json 重新爬蟲完畢，確認Tableau_url目錄裡的json無誤後，refresh下2更新views.py外面的json')
            except Exception as err:
                return HttpResponse('重新爬蟲失敗，Error= ' + str(err))
        elif refresh == '2':
            inner_json = os.path.join(os.path.dirname(__file__), r'Tableau_url\Tableau_url_inner.json')
            with open(inner_json, 'r', encoding='utf-8') as inner_json_file:
                with open(cls.file_path, 'w', encoding='utf-8') as outer_json_file:
                    inner_data = inner_json_file.read()
                    outer_json_file.write(inner_data)  # inner寫到外面json
                    cls.wb_dict = json.loads(inner_data)  # inner更新class變數
            #
            return HttpResponse('將Tableau_url目錄裡的Tableau_url_inner.json更新到外面Tableau_url.json，並重讀Tableau_url.json完畢')
        else:
            return HttpResponse('請確認refresh參數')

    def get_which(self, request):
        '''根據網址區分不同按鈕'''
        # 子類self調用此方法，得到按了哪個選單按鈕的對應數字，1 到 8
        url = request.build_absolute_uri()
        which = int(re.search('tableau([1-8])', url).group(1))
        return which

    # 點menu
    def get(self, request, *args, **kwargs):
        '''點左側menu後的處理'''
        # 根據網址，判斷按了menu哪一按鈕
        which = self.get_which(request)
        # 從父類讀最新的wb_dict，決定出嵌入碼
        get_embed_code = [
            self.wb_dict['作物生產']['meta']['作物_面積']['embed'],
            self.wb_dict['畜禽產品']['meta']['儀表板窗格 1']['embed'],
            self.wb_dict['水產品']['meta']['儀表板窗格 1']['embed'],
            self.wb_dict['林業產品']['meta']['儀表板窗格 1']['embed'],
            # self.wb_dict['農產品_產品別']['meta']['產品別']['embed'],
            # self.wb_dict['農產品_製品別']['meta']['製品別']['embed'],
            # self.wb_dict['SSG']['meta']['SSG']['embed'],
            # self.wb_dict['豬肉進出口']['meta']['豬肉進出口']['embed'],
        ]
        # embed_code = 'test'
        embed_code = replaceTicket(get_embed_code[which-1])
        # 根據menu按鈕，決定模板
        template_name = self.template_names[which-1]
        #
        # return HttpResponse(f'{embed_code}')
        return render(request, template_name, locals())

    # 點form
    def post(self, request, *args, **kwargs):
        '''點form radio後的處理'''
        # 根據網址，判斷按了menu哪一按鈕
        which = self.get_which(request)
        # 根據表單按鈕決定模板及嵌入碼
        self.dollar = dollar = request.POST['dollar']
        self.date_range = date_range = request.POST['date_range']
        self.dollar_page = dollar_page = (dollar == 'USD' and 1) or 2
        self.date_range_page = date_range_page = (date_range == 'year' and 1) or (date_range == 'month' and 2)  or (date_range == 'accumulation' and 3)
        # 決定出嵌入碼及模板
        embed_code = self.post_embed_code  # 調用子類的property
        # print(f'{embed_code}')
        template_name = f'tableau{which}_{dollar_page}_{date_range_page}.html'
        # template_name = 'tableau1_1_1.html'
        #
        # return HttpResponse(f'{embed_code}')
        return render(request, template_name, locals())


class Index(TemplateView):
    redirect_field_name = 'redirect_to'
    template_name = 'index.html'

    def get(self, request):
        which = request.GET.get('which') or 'nothing'
        print('which=', which)
        return render(request, self.template_name, {'which': which})


class Tableau1(Tableau_base):   #作物生產
    '''每個按鈕點選後，表單切換四種嵌入碼'''
    @property
    def post_embed_code(self):
        # 從父類讀最新的wb_dict，決定出嵌入碼
        post_embed_code = {
            '作物生產': replaceTicket(self.wb_dict['作物生產']['meta']['作物_面積']['embed']),
            # 'USDmonth': replaceTicket(self.wb_dict['貿易總覽_月']['meta']['概況']['embed']),
            # 'USDaccumulation': replaceTicket(self.wb_dict['貿易總覽_累計']['meta']['概況']['embed']),
            # 'NTDyear': replaceTicket(self.wb_dict['貿易總覽(台幣)']['meta']['概況']['embed']),
            # 'NTDmonth': replaceTicket(self.wb_dict['貿易總覽_月(台幣)']['meta']['概況']['embed']),
            # 'NTDaccumulation': replaceTicket(self.wb_dict['貿易總覽_累計(台幣)']['meta']['概況']['embed']),
        }
        return post_embed_code['作物生產']


class Tableau2(Tableau_base):   #畜禽產品
    '''每個按鈕點選後，表單切換四種嵌入碼'''
    @property
    def post_embed_code(self):
        # 從父類讀最新的wb_dict，決定出嵌入碼
        post_embed_code = {
            '畜禽產品': replaceTicket(self.wb_dict['畜禽產品']['meta']['儀表板窗格 1']['embed']),
            # 'USDmonth': replaceTicket(self.wb_dict['貿易總覽_月']['meta']['進出口']['embed']),
            # 'USDaccumulation': replaceTicket(self.wb_dict['貿易總覽_累計']['meta']['進出口']['embed']),
            # 'NTDyear': replaceTicket(self.wb_dict['貿易總覽(台幣)']['meta']['進出口']['embed']),
            # 'NTDmonth': replaceTicket(self.wb_dict['貿易總覽_月(台幣)']['meta']['進出口']['embed']),
            # 'NTDaccumulation': replaceTicket(self.wb_dict['貿易總覽_累計(台幣)']['meta']['進出口']['embed']),
        }
        return post_embed_code['畜禽產品']


class Tableau3(Tableau_base):   #水產品
    '''每個按鈕點選後，表單切換四種嵌入碼'''
    @property
    def post_embed_code(self):
        # 從父類讀最新的wb_dict，決定出嵌入碼
        post_embed_code = {
            '水產品': replaceTicket(self.wb_dict['水產品']['meta']['儀表板窗格 1']['embed']),
            # 'USDmonth': replaceTicket(self.wb_dict['國家_產品別_月']['meta']['國家別']['embed']),
            # 'USDaccumulation': replaceTicket(self.wb_dict['國家_產品別_累計']['meta']['國家別']['embed']),
            # 'NTDyear': replaceTicket(self.wb_dict['國家_產品別(台幣)']['meta']['國家別']['embed']),
            # 'NTDmonth': replaceTicket(self.wb_dict['國家_產品別_月(台幣)']['meta']['國家別']['embed']),
            # 'NTDaccumulation': replaceTicket(self.wb_dict['國家_產品別_累計(台幣)']['meta']['國家別']['embed']),
        }
        return post_embed_code['水產品']


class Tableau4(Tableau_base):   #林業產品
    '''每個按鈕點選後，表單切換四種嵌入碼'''
    @property
    def post_embed_code(self):
        # 從父類讀最新的wb_dict，決定出嵌入碼
        post_embed_code = {
            '林業產品': replaceTicket(self.wb_dict['林業產品']['meta']['儀表板窗格 1']['embed']),
            # 'USDmonth': replaceTicket(self.wb_dict['國家_製品別_月']['meta']['國家別']['embed']),
            # 'USDaccumulation': replaceTicket(self.wb_dict['國家_製品別_累計']['meta']['國家別']['embed']),
            # 'NTDyear': replaceTicket(self.wb_dict['國家_製品別(台幣)']['meta']['國家別-製品別']['embed']),
            # 'NTDmonth': replaceTicket(self.wb_dict['國家_製品別_月(台幣)']['meta']['國家別']['embed']),
            # 'NTDaccumulation': replaceTicket(self.wb_dict['國家_製品別_累計(台幣)']['meta']['國家別']['embed']),
        }
        return post_embed_code[self.dollar + self.date_range]


# class Tableau5(Tableau_base):   #農產品別/產品別
#     '''每個按鈕點選後，表單切換四種嵌入碼'''
#     @property
#     def post_embed_code(self):
#         # 從父類讀最新的wb_dict，決定出嵌入碼
#         post_embed_code = {
#             'USDyear': replaceTicket(self.wb_dict['農產品_產品別']['meta']['產品別']['embed']),
#             'USDmonth': replaceTicket(self.wb_dict['農產品_產品別_月']['meta']['產品別月']['embed']),
#             'USDaccumulation': replaceTicket(self.wb_dict['農產品_產品別_累計']['meta']['產品別月累計']['embed']),
#             'NTDyear': replaceTicket(self.wb_dict['農產品_產品別(台幣)']['meta']['產品別(台幣)']['embed']),
#             'NTDmonth': replaceTicket(self.wb_dict['農產品_產品別_月(台幣)']['meta']['產品別月(台幣)']['embed']),
#             'NTDaccumulation': replaceTicket(self.wb_dict['農產品_產品別_累計(台幣)']['meta']['產品別累計(台幣)']['embed']),
#         }
#         return post_embed_code[self.dollar + self.date_range]


# class Tableau6(Tableau_base):   #農產品別/製品別
#     '''每個按鈕點選後，表單切換四種嵌入碼'''
#     @property
#     def post_embed_code(self):
#         # 從父類讀最新的wb_dict，決定出嵌入碼
#         post_embed_code = {
#             'USDyear': replaceTicket(self.wb_dict['農產品_製品別']['meta']['製品別']['embed']),
#             'USDmonth': replaceTicket(self.wb_dict['農產品_製品別_月']['meta']['製品別月']['embed']),
#             'USDaccumulation': replaceTicket(self.wb_dict['農產品_製品別_累計']['meta']['製品別月累計']['embed']),
#             'NTDyear': replaceTicket(self.wb_dict['農產品_製品別(台幣)']['meta']['製品別(台幣)']['embed']),
#             'NTDmonth': replaceTicket(self.wb_dict['農產品_製品別_月(台幣)']['meta']['製品別月(台幣)']['embed']),
#             'NTDaccumulation': replaceTicket(self.wb_dict['農產品_製品別_累計(台幣)']['meta']['製品別累計(台幣)']['embed']),
#         }
#         return post_embed_code[self.dollar + self.date_range]


# class Tableau7(Tableau_base):   #SSG
#     '''每個按鈕點選後，表單切換四種嵌入碼'''
#     @property
#     def post_embed_code(self):
#         # 從父類讀最新的wb_dict，決定出嵌入碼
#         post_embed_code = {
#             'SSG': replaceTicket(self.wb_dict['SSG']['meta']['SSG']['embed']),
#         }
#         return post_embed_code['SSG']


# class Tableau8(Tableau_base):   #豬肉進出口
#     '''每個按鈕點選後，表單切換四種嵌入碼'''
#     @property
#     def post_embed_code(self):
#         # 從父類讀最新的wb_dict，決定出嵌入碼
#         post_embed_code = {
#             '豬肉進出口': replaceTicket(self.wb_dict['豬肉進出口']['meta']['豬肉進出口']['embed']),
#         }
#         return post_embed_code['豬肉進出口']


# class Tableautest(TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'tableautest.html'


# class Tableautrusted(TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'tableautrusted.html'


# class WebPublicIP(TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'webpublicip.html'

#     def get_context_data(self, **kwargs):
#         context = super(WebPublicIP, self).get_context_data(**kwargs)
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',}
#         check_public_IP_list = ['http://checkip.amazonaws.com','https://ifconfig.me/ip','https://ipecho.net/plain']
#         ip_result = dict()
#         for u in check_public_IP_list:
#             response = requests.get(u, headers=headers)
#             soup = bs(response.text, 'html.parser')
#             result=str(soup).strip()
#             hostname = u.replace('http://','').replace('https://','')
#             ip_result[hostname] = result
#         context['ip_result'] = ip_result
#         return context


# class Tableau1(TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'tableau1_1_1.html'

    # # 點menu
    # def get(self, request, *args, **kwargs):
    #     embed_code = wb_dict['貿易總覽']['meta']['概況']['embed']
    #     return render(request, type(self).template_name, locals())

    # def post(self, request, *args, **kwargs):
    #     self.kwargs['POST'] = request.POST
    #     dollar = self.kwargs['POST'].get('dollar')
    #     date_range = self.kwargs['POST'].get('date_range')
    #     if dollar == 'NTD':
    #         dollar_page = 2
    #     else:
    #         dollar_page = 1
    #     if date_range == 'month':
    #         date_range_page = 2
    #     else:
    #         date_range_page = 1

        # which = dollar + date_range
        # if which == 'USDyear':
        #     embed_code = wb_dict['貿易總覽']['meta']['概況']['embed']
        # elif which == 'USDmonth':
        #     embed_code = wb_dict['貿易總覽_月']['meta']['概況']['embed']
        # elif which == 'NTDyear':
        #     embed_code = None
        # elif which == 'NTDmonth':
        #     embed_code = None
        # # print('dollar_page={},date_range_page={}'.format(dollar_page,date_range_page))
        # # return redirect('../tableau1_{}_{}'.format(dollar_page,date_range_page))
        # return render(request, 'tableau1_{}_{}.html'.format(dollar_page, date_range_page), locals())


# class Tableau2(TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'tableau2_1_1.html'

    # # 點menu
    # def get(self, request, *args, **kwargs):
    #     embed_code = wb_dict['貿易總覽']['meta']['進出口']['embed']
    #     return render(request, type(self).template_name, locals())

    # def post(self, request, *args, **kwargs):
    #     self.kwargs['POST'] = request.POST
    #     dollar = self.kwargs['POST'].get('dollar')
    #     date_range = self.kwargs['POST'].get('date_range')
    #     if dollar == 'NTD':
    #         dollar_page = 2
    #     else:
    #         dollar_page = 1
    #     if date_range == 'month':
    #         date_range_page = 2
    #     else:
    #         date_range_page = 1

        # which = dollar + date_range
        # if which == 'USDyear':
        #     embed_code = wb_dict['貿易總覽']['meta']['進出口']['embed']
        # elif which == 'USDmonth':
        #     embed_code = wb_dict['貿易總覽_月']['meta']['進出口']['embed']
        # elif which == 'NTDyear':
        #     embed_code = None
        # elif which == 'NTDmonth':
        #     embed_code = None

        # return render(request, 'tableau2_{}_{}.html'.format(dollar_page, date_range_page), locals())


# class Tableau3(TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'tableau3_1_1.html'

#     # 點menu
#     def get(self, request, *args, **kwargs):
#         embed_code = wb_dict['國家-產品別']['meta']['國家別']['embed']
#         return render(request, type(self).template_name, locals())

#     def post(self, request, *args, **kwargs):
#         self.kwargs['POST'] = request.POST
#         dollar = self.kwargs['POST'].get('dollar')
#         date_range = self.kwargs['POST'].get('date_range')
#         if dollar == 'NTD':
#             dollar_page = 2
#         else:
#             dollar_page = 1
#         if date_range == 'month':
#             date_range_page = 2
#         else:
#             date_range_page = 1

#         which = dollar + date_range
#         if which == 'USDyear':
#             embed_code = wb_dict['國家-產品別']['meta']['國家別']['embed']
#         elif which == 'USDmonth':
#             embed_code = wb_dict['國家-產品別-月']['meta']['國家別']['embed']
#         elif which == 'NTDyear':
#             embed_code = None
#         elif which == 'NTDmonth':
#             embed_code = None

#         return render(request, 'tableau3_{}_{}.html'.format(dollar_page, date_range_page), locals())


# class Tableau4(TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'tableau4_1_1.html'

#     # 點menu
#     def get(self, request, *args, **kwargs):
#         embed_code = wb_dict['國家-製品別']['meta']['國家別-製品別']['embed']
#         return render(request, type(self).template_name, locals())

#     def post(self, request, *args, **kwargs):
#         self.kwargs['POST'] = request.POST
#         dollar = self.kwargs['POST'].get('dollar')
#         date_range = self.kwargs['POST'].get('date_range')
#         if dollar == 'NTD':
#             dollar_page = 2
#         else:
#             dollar_page = 1
#         if date_range == 'month':
#             date_range_page = 2
#         else:
#             date_range_page = 1

#         which = dollar + date_range
#         if which == 'USDyear':
#             embed_code = wb_dict['國家-製品別']['meta']['國家別-製品別']['embed']
#         elif which == 'USDmonth':
#             embed_code = wb_dict['國家-製品別-月']['meta']['國家別']['embed']
#         elif which == 'NTDyear':
#             embed_code = None
#         elif which == 'NTDmonth':
#             embed_code = None

        # return render(request, 'tableau4_{}_{}.html'.format(dollar_page, date_range_page), locals())


# class Tableau5(TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'tableau5_1_1.html'

#     # 點menu
#     def get(self, request, *args, **kwargs):
#         embed_code = wb_dict['產品別']['meta']['不同品項歷年進口量及進口國家—以產品別區分']['embed']
#         return render(request, type(self).template_name, locals())

#     def post(self, request, *args, **kwargs):
#         self.kwargs['POST'] = request.POST
#         dollar = self.kwargs['POST'].get('dollar')
#         date_range = self.kwargs['POST'].get('date_range')
#         if dollar == 'NTD':
#             dollar_page = 2
#         else:
#             dollar_page = 1
#         if date_range == 'month':
#             date_range_page = 2
#         else:
#             date_range_page = 1

#         which = dollar + date_range
#         if which == 'USDyear':
#             embed_code = wb_dict['產品別']['meta']['不同品項歷年進口量及進口國家—以產品別區分']['embed']
#         elif which == 'USDmonth':
#             embed_code = wb_dict['產品別月']['meta']['不同品項月進口量及進口國家—以製品別區分']['embed']
#         elif which == 'NTDyear':
#             embed_code = None
#         elif which == 'NTDmonth':
#             embed_code = None

#         return render(request, 'tableau5_{}_{}.html'.format(dollar_page, date_range_page), locals())


# class Tableau6(TemplateView):
#     redirect_field_name = 'redirect_to'
#     template_name = 'tableau6_1_1.html'

#     # 點menu
#     def get(self, request, *args, **kwargs):
#         embed_code = wb_dict['製品別']['meta']['不同品項歷年進口量及進口國家—以製品別區分']['embed']
#         return render(request, type(self).template_name, locals())

#     def post(self, request, *args, **kwargs):
#         self.kwargs['POST'] = request.POST
#         dollar = self.kwargs['POST'].get('dollar')
#         date_range = self.kwargs['POST'].get('date_range')
#         if dollar == 'NTD':
#             dollar_page = 2
#         else:
#             dollar_page = 1
#         if date_range == 'month':
#             date_range_page = 2
#         else:
#             date_range_page = 1

#         which = dollar + date_range
#         if which == 'USDyear':
#             embed_code = wb_dict['製品別']['meta']['不同品項歷年進口量及進口國家—以製品別區分']['embed']
#         elif which == 'USDmonth':
#             embed_code = wb_dict['製品別月']['meta']['不同品項月進口量及進口國家—以製品別區分']['embed']
#         elif which == 'NTDyear':
#             embed_code = None
#         elif which == 'NTDmonth':
#             embed_code = None

#         return render(request, 'tableau6_{}_{}.html'.format(dollar_page, date_range_page), locals())
