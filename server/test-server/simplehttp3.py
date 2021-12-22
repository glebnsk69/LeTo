import machine
import onewire, ds18x20
import time

dat=machine.Pin(12)
ds=ds18x20.DS18X20(onewire.OneWire(dat))
roms=ds.scan()
ds.convert_temp()

import socket

def web_page(request):
    html = "<html><head><title>HomeTempo</title><style>div{width:400;height:100;border: double 4px;border-radius: 12px;background-color: lightsteelblue;}h1 {color: midnightblue;font-size: 32;font-family: 'Times New Roman', Times, serif;font-weight: bold;}</style><body><center><div><h1>%s</h1></div></body></html>" % getTemp()
    return html

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
try:
    s.bind(addr)
    s.listen(1)
    print('try')
except:
    s.close()
    s.bind(addr)
    s.listen(1)
    print('except')

print('listening on', addr)

def getTemp():
 #   ds.convert_temp()
 #   time.sleep_ms(750)
 #   return ds.read_temp(roms[0])
    return 12.3

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))

    request = str(conn.recv(1024))
    print('The Content = %s' % request)
    response = web_page(request)
    
    print(response)
    conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    conn.sendall(response)
    conn.close()
