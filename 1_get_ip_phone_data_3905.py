import requests
import eventlet
from bs4 import BeautifulSoup
a=0
b=0
c=input("Masukkan IP Address, contoh: '172.8.8.' , jangan salah ketik ya, ada titik terakhir ya : ")
writeoutput = open('ipphone_web_content.txt','w')
url='http://'+c
while b < 255:
	urlloop=url+str(b)+'/Device_Information.html'
	try:
		with eventlet.timeout.Timeout(1):
			response = requests.get(urlloop,timeout=1)
		print ("OK -", urlloop)
		a=1
		print(a)
	except requests.exceptions.ReadTimeout:
		print ("READ TIMED OUT -", urlloop)
		a=2
		print(a)
	except requests.exceptions.ConnectionError:
		print ("CONNECT ERROR -", urlloop)
		a=2
		print(a)
	except eventlet.timeout.Timeout:
		print ("TOTAL TIMEOUT -", urlloop)
		a=2
		print(a)
	except requests.exceptions.RequestException:
		print ("OTHER REQUESTS EXCEPTION -", urlloop)
		a=2
		print(a)
	if a == 1:
		res = requests.get(urlloop)
		html_page = response.content
		soup = BeautifulSoup(html_page, features="lxml")
		titles = soup.find_all(['b','strong'])
		for title in titles:
			print(title.get_text())
			writeoutput.write(title.get_text()+'\n')
	else:
		print('error')
	b+=1