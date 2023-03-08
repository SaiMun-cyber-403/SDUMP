from os import system,remove
import requests 
from platform import machine
print('Checking For Update...')
def ckk():
	v = "0.5"
	peo = requests.get('https://apppppappppppappp.blogspot.com/2023/03/dump.html').text
	if v in peo:
		if machine()=='aarch64':
			system('chmod +x *;./SDUMP')
		else:
			system('chmod +x *;./SDUMP32')
	else:
		update()  	
def update():
	try:
		remove('SDUMP')
		remove('SDUMP32')
	except:pass
	try:remove('Dump.py')
	except:pass
	system('git pull')
	if machine()=='aarch64':
		system('curl -L https://github.com/SaiMun-cyber-403/SDUMP/raw/main/SDUMP -o SDUMP;git pull;chmod +x *;./SDUMP')
	else:
		system('curl -L https://github.com/SaiMun-cyber-403/SDUMP/raw/main/SDUMP32 -o SDUMP32;git pull;chmod +x *;./SDUMP')
		system('clear')
ckk()