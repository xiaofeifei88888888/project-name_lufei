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
    "cardId": "CA16072BBD1A47L87A",
    "quantity": 200
}
headers = {'Content-type':'application/json'
           }
url='http://sit-rest.ifenqu.com/card/v1/cards'
resp = requests.put(url,cookies=cookies,data=json.dumps(data), headers=headers)
print (resp.url)
print (resp.status_code)
print (resp.text)
