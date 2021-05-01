#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        if id == 584188524195:
                print("Sustainable goal 1: No Poverty")
        print(id)
        if id == 584184985815:
	        print("Sustainable goal 5: Gender Equaility")
finally:
        GPIO.cleanup()
