import json
import requests
import urlparse
from bs4 import BeautifulSoup
import xlwt

cookies = {
    "ali_apache_id": "27.4.199.208.146679517936.678180.2",
    "acs_usuc_t": "acs_rt=afade78fb5844a2ebc43f3f5ff43c9dc",
    "ali_beacon_id": "27.4.199.208.1466795181389.532432.8",
    "_gat": "1",
    "cna": "cb3aD/oBL3QCARsEx9BtAvyt",
    "xman_us_f": "x_l=0&x_locale=en_US&no_popup_today=n&x_user=IN|Azad|Lance|ifm|796869527&last_popup_time=1466795223251",
    "xman_us_t": "x_lid=in1176185458dhjr&sign=y&x_user=5MgE3h2evWMtqGCrrikvihoun1HNrPRO6mBn1g3WSzg=&ctoken=_ssbazlnc0ro&need_popup=y&l_source=alibaba",
    "intl_locale": "en_US",
    "JSESSIONID": "0UzG+AmcoO6Fe5SZcJgjLY5z",
    "ali_apache_track": "mt=1|mid=in1176185458dhjr",
    "ali_apache_tracktmp": "W_signed=Y",
    "_ga": "GA1.2.1569042526.1466795183",
    "l": "Ah0dKaTtzO35pQ60UwEeyZeYrfMXOlGM",
    "acs_rt": "27.4.199.208.1466795182809.1"
}


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"
}


all_items = []

def get_initial_data(search_text):

    print " Getting initial data"

    search_url = 'http://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&SearchText={search_text}&dmtrack_pageid=06sm6rkcpyacwrwwm4ai6u7cev155867d33e525204&XPJAX=1'.format(
        search_text=search_text)
    rep = requests.get(search_url, cookies=cookies, headers=headers)
    rep_data = rep.json()
    pagination = rep_data['pagination']
    total_pages = pagination['total']
    pagination_url = pagination['urlRule']
    # product_list = rep_data['normalList']

    return {
        'total_pages': total_pages,
        'pagination_url': pagination_url
    }

def products_from_page(page_url, page_no):
    # json_page_query = '?dmtrack_pageid=0fp3m1p8ihexu9k702u59kqn3z155865e5d31102a1&XPJAX=1'
    print "getting products on page ", str(page_no)

    query = {
        'dmtrack_pageid': '0fp3m1p8ihexu9k702u59kqn3z155865e5d31102a1',
        'XPJAX': 1
    }

    page_no_url = 'http:' + page_url.format(page_no)

    rep = requests.get(
        page_no_url, params=query, cookies=cookies, headers=headers)

    rep_data = rep.json()
    product_list = rep_data['normalList']
    all_items.extend(product_list)


def get_final_data_for_product(product):
    supplier_url = product['supplierHref']
    supplier_domain = urlparse.urlparse(supplier_url).hostname
    supplier_page = "http://" + supplier_domain + '/contactinfo.html'
    rep = requests.get(
        supplier_page, cookies=cookies, headers=headers)

    content = rep.content
    soup = BeautifulSoup(content, 'html.parser')

    try:
        contact_info = soup.find_all('div', class_="sensitive-info")[0]
    except Exception, e:
        contact_info = None

    try:
        company_infos = soup.find_all(
            'table', class_="company-info-data table")[0].find_all('td')
    except Exception, e:
        company_infos = None

    try:
        name = soup.find('h1', class_='name').text.strip()
    except Exception, e:
        name = None

    try:
        year = 2016 - int(product['supplierYear'])
    except Exception, e:
        year = None

    try:
        mqq = product['minOrder']
    except Exception, e:
        mqq = None

    try:
        factory_name = company_infos[1].text
    except Exception, e:
        factory_name = None
    try:
        location = company_infos[3].text
    except Exception, e:
        location = None
    try:
        website = company_infos[5].find('a').get('href')
    except Exception, e:
        website = None

    try:
        telephone = contact_info.find_all('dd')[0].text
    except Exception, e:
        telephone = None
    try:
        mobile = contact_info.find_all('dd')[1].text
    except Exception, e:
        mobile = None
    try:
        fax = contact_info.find_all('dd')[2].text
    except Exception, e:
        fax = None

    data = {
        "factory_name": factory_name,
        "year": year,
        "name": name,
        'telephone': telephone,
        'mobile': mobile,
        'fax': fax,
        "website": website,
        "location": location,
        "mqq": mqq
    }

    print data

    return data


def generate_exel(final_data):
    print "Creating exel"
    print "Products = ", str(len(final_data))

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Cliffton")
    count = 1
    for record in final_data:

        print count
        try:
            sheet.write(count, 0, record['factory_name'])
            sheet.write(count, 1, record['year'])
            sheet.write(count, 2, record['name'])
            sheet.write(count, 3, record['telephone'])
            sheet.write(count, 4, record['mobile'])
            sheet.write(count, 5, record['fax'])
            sheet.write(count, 6, record['website'])
            sheet.write(count, 7, record['location'])
            sheet.write(count, 8, record['mqq'])
        except Exception, e:
            pass
        count = count + 1
    workbook.save("ali.xls")



d = get_initial_data('caps')

print d

page_url = d['pagination_url']
for i in range(1, int(d['total_pages'])):
    print "on page ", str(i)
    products_from_page(page_url, i)


final_data = []

print "total products = ", str(len(all_items))

for product in all_items:
    try:
        data = get_final_data_for_product(product)
        final_data.append(data)
    except Exception, e:
        pass

generate_exel(final_data)
