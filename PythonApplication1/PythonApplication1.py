﻿from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class DefaultHttpServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        param = ''
        url = ''
        c = self.path
        temp = c.split("?")
        query_components = list(c.split("=") for c in temp[1].split("&"))
        for query in query_components:
            param += "&" + query[0] + "=" + query[1]
        url = 'http://openapi.e-gen.or.kr/openapi/service/rest/ErmctInfoInqireService/getEgytListInfoInqire?' + param + '&numOfRows=100&ServiceKey=FHlV2aXJriahVZyA8K86zVh2MbfmzRPOsXf9N5eHFWZaZBQ66vkxEI8sXLCFMHJ1SveL1Yu5bNpXty9kGs243g%3D%3D'
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

        # with open('data.json', 'w', encoding='utf-8') as f:
        #     f.write(data2)
        
        self.wfile.write(data2.encode("utf-8"));
        # self.wfile.write('HELLO WORLD')

if __name__ == '__main__':
	httpd = HTTPServer(('', 8881), DefaultHttpServerHandler)
	print ('Started Webserver port 8888...')
	httpd.serve_forever()