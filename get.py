from multiprocessing import Process as pro
from time import sleep

def op():
    print('Load the web', end='')
    while True:
        for x in range(6):
            print('.',end='',flush=True)
            sleep(0.3)
        print('\b ',end='')
        for x in range(5):
            print('\b\b',end=' ',flush=True)
            sleep(0.1)
        print('\b',end='')

p = pro(target=op)
p.start()
import requests, os
from bs4 import BeautifulSoup as be
uwu = os.getcwd().split('/')
if 'figlet' not in uwu:
    os.chdir('/data/data/com.termux/files/usr/share/figlet')
r = be(requests.get('http://www.figlet.org/fontdb.cgi').text, 'html.parser')
r = [x.text+'.flf' for x in r.find_all('a') if 'flf' in x['href']]
ls = os.listdir()
p.kill()
print('Ok!\ndownloading')

for x in r:
    if x in ls:
        pass
    else:
        open(x,'w').write(requests.get('http://www.figlet.org/fonts/'+x).text)
        print('downloaded:',x)
