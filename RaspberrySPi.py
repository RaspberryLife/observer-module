#!/usr/bin/python
#-----------------------------------
# take photos and play alarmfile when motion is detected
#
# Author
: Jasmin Sunitsch
# Contact
: RaspberrySPiProjekt@gmail.com
# Date
: 30/01/2015
# Version
: 3.0
# Requires Raspberry Pi, PiCam, Motion Detector, WLAN or UMTS
#
#-----------------------------------
# -*- coding: UTF-8 -*-

import thread
import pygame
import RPi.GPIO as GPIO
import time 
import os
import subprocess

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

pygame.mixer.init()
alarmSound = pygame.mixer.Sound("./audio/alarm.wav")

def warte(t):
	sleepTime = 1-(t-time.time())
	if sleepTime < 0:
		sleepTime = 0
	time.sleep(sleepTime)

def playSound():
	if not pygame.mixer.get_busy():
		alarmSound.play(loops=5)

def getImage():
	bildName = (time.strftime("%H%M%S_%d%m%y"))			
	cmdString = 'sudo raspistill -o ./images/' + bildName + '.jpg --nopreview --timeout 1'
	subprocess.call(cmdString,shell=True)

try:
	print "Raumbetrachtung aktiv"
	
	while True:

		startTime = time.time()

		if GPIO.input(PIR_PIN):
			print "Erkenne Bewegung!"
			
			#thread.start_new_thread(playSound,(0,))
			#thread.start_new_thread(getImage,(0,))
			
			playSound()
			getImage()

		else:
			print "Keine Bewegung!"
	
		warte(startTime)		
	
except KeyboardInterrupt:

	print "Raumbetrachtung beendet"
	GPIO.cleanup()
