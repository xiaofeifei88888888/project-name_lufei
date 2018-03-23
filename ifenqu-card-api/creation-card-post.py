# /usr/bin/env python
# encoding: utf-8
#desc 编码为表单形式的数据，通过data参数传递
import requests
import json
cookies = {
    'sit-ifq_identity':'NIzs6yOKLVw=',
    'ifq_access_token':'cffe22ebc3839bfcc6296437d8db1f6e',
    'ifq_refresh_token':'3b96e620c9ca9549cb79ca251d09de5a',
}
data = {
    'beginTimestamp': '2018-03-28 12:00:00',
    'brandName': '海底捞',
    'cardType': 'CASH',
    'dateType': 'DATE_TYPE_FIX_TIME_RANGE',
    'description': '不可与其他优惠同享/n如需团购券发票，请向店员提出要求。',
    'endTimestamp': '2018-03-31 23:59:59',
    'fixedTerm': 60,
    'getLimit': 20,
    'notice': '请出示二维码核销卡券',
    'platformId': 'P123',
    'quantity': 100000,
    'servicePhone': '021-95559',
    'subTitle': '鸳鸯锅底+牛肉1份+土豆一份',
    'title': '双人套餐100元兑换券',
    'useCustomCode': 'false',
}
headers = {'Content-type':'application/json'
           }
url= 'http://sit-rest.ifenqu.com/card/v1/cards'
# , headers=headers
resp = requests.post(url,cookies=cookies,data=json.dumps(data), headers=headers)
print (resp.url)
print (resp.status_code)
print (resp.text)
