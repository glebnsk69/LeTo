# This file is executed on every boot (including wake-boot from deepsleep)


print("="*16,"Start boot.py","="*16)



#import esp
#esp.osdebug(None)
import gc
##import webrepl
#--------------------
##import network
##import time

#wlan=network.WLAN()
#sta=network.WLAN(network.STA_IF)
#sta.active(True)
#sta.connect('SIBERS','Shae2ah7')
#time.sleep_ms(500)

#print('-'*25)
#print(sta.isconnected())

#--------------------
##webrepl.start()
gc.collect()
