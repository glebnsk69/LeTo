import machine
import onewire, ds18x20
import time
import gc

dat=machine.Pin(12)
ds=ds18x20.DS18X20(onewire.OneWire(dat))
roms=ds.scan()
ds.convert_temp()


def readHtml(page='index.htm'):
    html = ""
    print('Open ',page)
    f=open(str(page),"r")
    l=f.readlines()
    for i in l:
        html=html+i
        print('==>',i)
    f.close()
    return html

def writeHtmlCount(num):
    f=open('test.txt',"a")
    f.write('Line: '+str(num)+'<br>')
    f.flush()
    f.close()


import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)
num=0
page='index.htm'

while True:
    print('==>')
    cl, addr = s.accept()
    req = cl.recv(1024)
    print('==>',req)
    
    if ('exp1' in req):
        page='Exp1.htm'
    else:
        if('exp2' in req): 
            page='Exp2.htm'

    print('client connected from', addr)
        
    html=str(readHtml(page))
   
    response = html 
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    num=num+1
    writeHtmlCount(num)
    cl.close()
    page='index.htm'
    gc.collect()