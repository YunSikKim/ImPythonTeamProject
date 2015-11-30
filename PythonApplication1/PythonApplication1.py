from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

url = 'http://openapi.e-gen.or.kr/openapi/service/rest/ErmctInfoInqireService/getEgytListInfoInqire?&Q0=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&Q1=%EC%A2%85%EB%A1%9C%EA%B5%AC&numOfRows=100&ServiceKey=FHlV2aXJriahVZyA8K86zVh2MbfmzRPOsXf9N5eHFWZaZBQ66vkxEI8sXLCFMHJ1SveL1Yu5bNpXty9kGs243g%3D%3D'
data = urlopen(url)

soup = BeautifulSoup(data, from_encoding="utf-8")

elist = []

for items in soup.findAll('item'):
    temp = []
    for item in items: 
        temp.append(item.string)
    elist.append(temp)

jsondata = []

dic = {}

for item in elist:
    dic = dict(name=item[3], emclsName=item[2], address=item[0], representTel=item[4], emergencyTel=item[5], latitude=item[9], longitude=item[10])
    jsondata.append(dic)

for item in jsondata:
    print(item)

data2 = json.dumps(jsondata, ensure_ascii=False)

with open('data.json', 'w', encoding='utf-8') as f:
    f.write(data2)