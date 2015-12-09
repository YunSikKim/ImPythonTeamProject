from urllib.request import urlopen
from bs4 import BeautifulSoup
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class DefaultHttpServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		param = ''
		method = ''
		url = ''
		c = self.path
		temp = c.split("?")
		query_components = list(c.split('=') for c in temp[1].split("&"))
		for query in query_components:
			if query[0] != 'method':
				param += "&" + query[0] + "=" + query[1]
			else:
				method += query[1]
		
		if method == '0':
			url += 'http://openapi.e-gen.or.kr/openapi/service/rest/ErmctInfoInqireService/getEgytLcinfoInqire?' + param + '&pageNo=1&numOfRows=10&ServiceKey=dTLz2zeqOB5BenN%2FtHECFHX5onmNjqdJ41W24Q38p4PMn%2BMPxsSowWg8X2pJEdNLBvmRyxMuHZMyEQkavolOYw%3D%3D'
		else:
			url += 'http://openapi.e-gen.or.kr/openapi/service/rest/ErmctInfoInqireService/getEgytListInfoInqire?' + param + '&pageNo=1&numOfRows=10&ServiceKey=dTLz2zeqOB5BenN%2FtHECFHX5onmNjqdJ41W24Q38p4PMn%2BMPxsSowWg8X2pJEdNLBvmRyxMuHZMyEQkavolOYw%3D%3D'
		
		
		data = urlopen(url)
		
		
		soup = BeautifulSoup(data, from_encoding="utf-8")
		
		print(url)		
		
			
		elist = []
	
		for items in soup.findAll('item'):
			temp = []
			if method == '0':
				for item in items: 
					tempsplit = str(item).split('>', 1)
					print(tempsplit)
					if tempsplit[0] == '<distance':
						temp.append(item.string)
					if tempsplit[0] == '<dutyname':
						temp.append(item.string)
					if tempsplit[0] == '<dutyaddr':
						temp.append(item.string)
					if tempsplit[0] == '<dutytel1':
						temp.append(item.string)
					if tempsplit[0] == '<latitude':
						temp.append(item.string)
					if tempsplit[0] == '<longitude':
						temp.append(item.string)
					
					print(temp)
			else:
				for item in items: 
					tempsplit = str(item).split('>', 1)
					print(tempsplit)
					if tempsplit[0] == '<dutyname':
						temp.append(item.string)
					if tempsplit[0] == '<dutyaddr':
						temp.append(item.string)
					if tempsplit[0] == '<dutytel1':
						temp.append(item.string)
					if tempsplit[0] == '<wgs84lat':
						temp.append(item.string)
					if tempsplit[0] == '<wgs84lon':
						temp.append(item.string)
					
					print(temp)
			elist.append(temp)
	
		jsondata = []
	
		dic = {}
	
		if method == '0':
			for item in elist:
				dic = dict(DISTANCE=item[0], DUTY_NAME=item[2], DUTY_ADDR=item[1], DUTY_TEL1=item[3], LATITUDE=item[4], LONGITUDE=item[5])
				jsondata.append(dic)
		else:
			for item in elist:
				dic = dict(DUTY_NAME=item[1], DUTY_ADDR=item[0], DUTY_TEL1=item[2], LATITUDE=item[3], LONGITUDE=item[4])
				jsondata.append(dic)
	
		data2 = json.dumps(jsondata, ensure_ascii=False)
	
		print(data2)
	
		# with open('data.json', 'w', encoding='utf-8') as f:
		#     f.write(data2)
				
		self.wfile.write(data2.encode("UTF-8"));
		# self.wfile.write('HELLO WORLD')
				


if __name__ == '__main__':
	httpd = HTTPServer(('', 8888), DefaultHttpServerHandler)
	print ('Started Webserver port 8888...')
	httpd.serve_forever()