# -*- coding: utf-8 -*-
import socket

class Server:
    def send_answer(self, conn, status="200 OK", typ="text/plain; charset=utf-8", data=""):
        print("===> send_answer",data)
        data = data.encode("utf-8")
        print("===> 1")
        conn.send(b"HTTP/1.1 " + status.encode("utf-8") + b"\r\n")
        conn.send(b"Server: simplehttp\r\n")
        conn.send(b"Connection: close\r\n")
        conn.send(b"Content-Type: " + typ.encode("utf-8") + b"\r\n")
        conn.send(b"Content-Length: " + bytes(len(data)) + b"\r\n")
        conn.send(b"\r\n")# после пустой строки в HTTP начинаются данные
        print("===> 9",data)
        conn.send(data)

    def RouteAdd(self, path, funcname):
        print("17: RouteAdd("+path+","+funcname)
        if path not in self.routes:
            self.routes[path] = funcname

    def parse(self, conn, addr):# обработка соединения в отдельной функции
        data = b""
        while not b"\r\n" in data: # ждём первую строку
            tmp = conn.recv(1024)
            if not tmp: # сокет закрыли, пустой объект
                break
            else:
                data += tmp
                print(data)

            if not data: # данные не пришли
                return # не обрабатываем

            udata = data.decode("utf-8")
            # берём только первую строку
            udata = udata.split("\r\n", 1)[0]
#            print("udata:",udata)
            # разбиваем по пробелам нашу строку
            method, string, protocol = udata.split(" ", 2)
#            print("metod;",metod,"string;",string,"protocol;",protocol)
            if string.find('?') != -1:
                address = string.split('?')[0]
                params = dict(b.split('=') for b in string.split('?')[1].split('&'))
                print("===== params ======")
                print(params)
            else:
                address = string
                params = {}
            if method != "GET":
                print("===== method != GET ======")
                self.send_answer(conn, "404 Not Found", data="Page not found(1)")
                return
            print("===address,self.routes===")
            print(address,self.routes)
            print("====================")
            if address in self.routes:
                print("=== address in self.routes True===")
                if len(params) > 0:
                    print("===== len(params) > 0 self.routes ======")
                    print("===>")
                    print("===>self.routes",self.routes)
                    address = '/ya.ru'
                    print("===>adderss    ",address)
                    print("===>params     ",params)
                    
                    print("===>self.routes[address]",self.routes[address])
                    print("===>")
                    self.send_answer(conn, typ="text/html; charset=utf-8", data=self.routes[address](address, params))
#                    self.send_answer(conn, typ="text/html; charset=utf-8", data='123456')
                else:
                    try:
                        self.send_answer(conn, typ="text/html; charset=utf-8", data=self.routes[address]())
                        pass
                    except:
                        self.send_answer(conn, typ="text/html; charset=utf-8", data=self.routes[address](address))
                        pass
                return
            else:
                self.send_answer(conn, "404 Not Found", data="Page not found(2)")
                return

    def __init__(self,port=8080):
        self.routes = {'/test.htm','/Exp1.htm','/Exp2.htm','/ya.ru'}
        self.stop = False
        self.sock = socket.socket()
        self.sock.bind( ("", port) )
        self.sock.settimeout(2)
        self.sock.listen(5)

    def Run(self):
        try:
            while 1: # работаем постоянно
                try:
                    if self.stop: break
                    conn, addr = self.sock.accept()
                except:
                    continue
                try:
                    print('self.parse(conn, addr)',addr)
                    self.parse(conn, addr)
                except:
                    self.send_answer(conn, "500 Internal Server Error", data="Error 500!")
                    print('Run except',addr)
                finally:
                # так при любой ошибке
                # сокет закроем корректно
                    conn.close()
        finally:
            self.sock.close()
            # так при возникновении любой ошибки сокет
            # всегда закроется корректно и будет всё хорошо