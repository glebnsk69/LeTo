# This file is executed on every boot (including wake-boot from deepsleep)
import gc
#import network
import mywifi
import termohttp3

#sta_if = network.WLAN(network.STA_IF);
#sta_if.active(True)
#sta_if.connect("0370-mobile", "Vfhn2007")

#print(sta_if.ifconfig())

#import esp
#esp.osdebug(None)
#import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)

#import webrepl
#webrepl.start()
gc.collect()
#import termohttp3
