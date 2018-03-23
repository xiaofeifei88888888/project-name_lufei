# /usr/bin/env python
# encoding: utf-8
#desc 编码为表单形式的数据，通过data参数传递
import requests
import json
host = 'http://sit-rest.ifenqu.com/card'
endpoint = '/v1/cards/customCode'
url = ''.join([host, endpoint])
cookies = {
    'sit-ifq_identity':'NIzs6yOKLVw=',
    'ifq_access_token':'cffe22ebc3839bfcc6296437d8db1f6e',
    'ifq_refresh_token':'3b96e620c9ca9549cb79ca251d09de5a',
}
data = {
  "cardId": "CA15AF5EDDC7748VOE",
  "codes": "CO15AF5EDDC7748VOE,CO15AF5EDDC7748VOA"
}
headers = {'Content-type':'application/json'
           }

resp = requests.post(url,cookies=cookies,data=json.dumps(data), headers=headers)
print (resp.url)
print (resp.status_code)
print (resp.text)