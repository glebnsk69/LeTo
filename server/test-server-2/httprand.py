import machine
import onewire, ds18x20
import time
import gc
from urandom import getrandbits as rnd

#dat=machine.Pin(12)
#ds=ds18x20.DS18X20(onewire.OneWire(dat))
#roms=ds.scan()
#ds.convert_temp()

def getTemp():
    return rnd(6)/10



def sendPage(fileName,cl):
    print('Start reading ', fileName)
    f = open(str(fileName),'r', encoding="utf-8")
    while True:
        resp=f.read(512)
        if not resp:
            break
        r=cl.send(resp)
        print('Send html. ',r,' bites')
    print('End reading ', fileName)
    f.close()



import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)
page='index.htm'

while True:
    cl, addr = s.accept()
    req = cl.recv(1024)
    print('==>',req)
    
    if ('exp1' in req):
        page='Exp1.htm'
    else:
        if('exp2' in req): 
            page='Exp2.htm'

    print('client connected from', addr)
    r = cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    print('Send HTTP/1.0 200 ',r ,' bites')
    sendPage(page,cl)
    print('Send html. ',r,' bites')
    cl.close()
    page='index.htm'
    gc.collect()
