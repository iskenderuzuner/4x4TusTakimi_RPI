
import time

import RPi.GPIO as GPIO

from keypad import keypad
 

GPIO.setwarnings(False)

 

if __name__ == '__main__':

    # Initialize

    kp = keypad(columnCount = 3)

 

    # waiting for a keypress

    digit = None

    while digit == None:

        digit = kp.getKey()

    # Print result

    print digit

    time.sleep(0.5)

 

    ###### 4 Digit wait ######

    seq = []

    for i in range(7):

        digit = None

        while digit == None:

            digit = kp.getKey()

        seq.append(digit)

        time.sleep(0.4)

 

    # Check digit code
print(seq)
if seq == [4, 2, 5, 2 , 0 , 3 , 1]:
    print('sifre dogru!')
    GPIO.setup(11,GPIO.OUT)#pinlerin durmunu cikis yaptik
    GPIO.output(11,True)# 12 nolu pini +5v cikis verdik
    time.sleep(5)# bekleme suresi belirledik
    GPIO.output(11,False)#12 nolu pini 0v'a dusurduk.
else: # cevap python del ise
    print('sifre yanlis!')
    GPIO.setup(12,GPIO.OUT)#pinlerin durmunu cikis yaptik
    GPIO.output(12,True)# 12 nolu pini +5v cikis verdik
    time.sleep(5)# bekleme suresi belirledik
    GPIO.output(12,False)#12 nolu pini 0v'a dusurduk.