import gc
import socket
import machine
import os
import onewire
import ds18x20
import time
import json

dat = machine.Pin(12)
ds = ds18x20.DS18X20(onewire.OneWire(dat))
roms = ds.scan()
ds.convert_temp()

rtc = machine.RTC()

def getTemp():
    pin.value(0)
    ds.convert_temp()
    time.sleep_ms(750)
    pin.value(1)
    return round(ds.read_temp(roms[0]),1), round(ds.read_temp(roms[1]),1)


def getJson():
    ds.convert_temp()
    time.sleep_ms(750)
    temp = ds.read_temp(roms[0])
    temp2 = ds.read_temp(roms[1])
    temp2 = round(temp2,2)
    temp = round(temp, 2)
    myTime = rtc.datetime()[5]*60+rtc.datetime()[6]
    print("time=",myTime,"t1=",temp,"t2=",temp2)
    return json.dumps({'time':myTime,'temp1':temp,'temp2':temp2})


def getFname(reqString):  #получить ися файла из get запроса,
    s = reqString.decode().replace("GET /","").split('\r\n')[0].rsplit(' ')
    if(len(s[0])==0):
        return "index.html" # если имя не указанно вернутроь index.html
    else:
        fname = s[0].rsplit("?")[0]
        print("getFname: ",fname)
        if(fname=="temp.json"): 
            print("JSON!") 
            fname="temp.json"
            return(fname)
        if(not fileExist(fname)): fname = "404.html"
        return fname

def fileExist(fname): # проверить есть ли такой файл в папке
    if(fname in os.listdir()):
        print("file ",fname," exists")
        return True
    else:return False

def getFileExt(fName):
    f = fName.split(".")
    return(f[len(f)-1])

def sendData(c,fName):
    print("sendData:",fName)
    if(fName=="temp.json"):
        l = getJson()
        c.send(l)
    else: 
        sendFile(c,fName)
    
def sendFile(c,fName):
    print("sendFile: ",fName)
    f = open(fName,'r')
    l = "#"
    while(len(l) > 0):
        l = f.readline()
        c.send(l)


#pin = machine.Pin(2,machine.Pin.OUT)
#pin.value(1)

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)
contentType = ["HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n","HTTP/1.0 200 OK\r\nContent-type: text/css\r\n\r\n","HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n"]

while True:
    cl, addr = s.accept()
    req = cl.recv(1024)
    print(req)
    fName = getFname(req)
    print(fName)
    if(getFileExt(fName) == "css"):
        cl.send(contentType[1])
    else:
        if(fName=="temp.json"):
            cl.send(contentType[2])
        else:
            cl.send(contentType[0])
    
    print("before sendFile")
    #sendFile(cl,fName)
    sendData(cl,fName)
    print("after sendFile")
#    cl.send("<html><head><title>LETo Project</title><style>div{width:400;height:100;border: double 4px;border-radius: 12px;background-color: lightsteelblue;}h1 {color: midnightblue;font-size: 32;font-family: 'Times New Roman', Times, serif;font-weight: bold;}</style><body><center><div><h1>LeTo</h1></div></body></html>")
    
    cl.close()
    gc.collect()


