import os

def getFname(reqString):  #получить ися файла из get запроса,
    s = reqString.decode().replace("GET /","").split('\r\n')[0].rsplit(' ')
    if(len(s[0])==0):
        return "index.html" # если имя не указанно вернутроь index.html
    else:
        fname = s[0].rsplit("?")[0]
        if(not fileExist(fname)): fname = "404.html"
        return fname

def fileExist(fname): # проверить есть ли такой файо в папке
    if(fname in os.listdir()):return True
    else:return False

s1 = b'GET / HTTP/1.1\r\nHost: 192.168.88.101\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
s2 = b'GET /style.css HTTP/1.1\r\nHost: 192.168.88.101\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
s3 = b'GET /style.css?t=99&q=333 HTTP/1.1\r\nHost: 192.168.88.101\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
s4 = b'GET /filexx1.html?t=99&q=333 HTTP/1.1\r\nHost: 192.168.88.101\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'

print("1:",getFname(s1))
fname = getFname(s1)
f = open(fname,"r")
l = "#"
n=0
while(len(l) > 0):
    n+=1
    l = f.readline().replace("\r\n","#")    
    print(n,":",l)

#for i in range(10):
#    l = f.readline().replace("\n","#")    
#    print(l)
f.close()
#print("2:",getFname(s2))
#print("3:",getFname(s3))
#print("4:",getFname(s4))