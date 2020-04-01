#!/usr/bin/env python3
#############################################################################
# Filename    : DHT11.py
# Description : read the temperature and humidity data of DHT11
# Author      : freenove
# modification: 2018/08/03
########################################################################
import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT
DHTPin = 11     #define the pin of DHT11

def loop():
    dht = DHT.DHT(DHTPin)   #create a DHT class object
    sumCnt = 0              #number of reading times
    while(True):
        sumCnt += 1         #counting number of reading times
        chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
        #print ("The sumCnt is : %d, \t chk    : %d"%(sumCnt,chk))
        if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value
            print("%s,%.2f,%.2f"%(time.strftime("%Y-%m-%d %H:%M:%S"),dht.humidity,dht.temperature), flush=True)
        #    print("DHT11,OK!")
        #if(chk is dht.DHTLIB_ERROR_CHECKSUM): #data check has errors
        #    print("DHTLIB_ERROR_CHECKSUM!!")
        #elif(chk is dht.DHTLIB_ERROR_TIMEOUT):  #reading DHT times out
        #    print("DHTLIB_ERROR_TIMEOUT!")
        #else:               #other errors
        #    print("Other error!")

        time.sleep(2)

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()

