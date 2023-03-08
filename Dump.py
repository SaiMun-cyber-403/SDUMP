from os import system,remove
import requests 
from platform import machine
print('Checking For Update...')
def ckk():
	v = "0.4"
	peo = requests.get('https://apppppappppppappp.blogspot.com/2023/03/dump.html').text
	if v in peo:
		system('chmod +x *;./SDUMP')
	else:
		update()  	
def update():
	try:remove('SDUMP')
	except:pass
	system('git pull')
	if machine()=='aarch64':
		system('curl -L https://github.com/SaiMun-cyber-403/SDUMP/raw/main/SDUMP -o SDUMP;git pull;chmod +x *;./SDUMP')
	else:
		system('curl -L https://github.com/SaiMun-cyber-403/SDUMP/raw/main/SDUMP -o SDUMP;git pull;chmod +x *;./SDUMP')
		system('clear')
ckk()