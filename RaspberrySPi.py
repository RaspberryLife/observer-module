#!/usr/bin/python
#-----------------------------------
# take photos and play alarmfile when motion is detected
#
# Author    : Jasmin Sunitsch
# Contact   : RaspberrySPiProjekt@gmail.com or Mail@JamBid.de
# Date      : 30/01/2015
#
# Requires Raspberry Pi, PiCam, Motion Detector, WLAN or UMTS 
# 
#
#-----------------------------------
# -*- coding: UTF-8 -*-

import thread
import pygame
import RPi.GPIO as GPIO
import time 
import os
import os.path
import subprocess
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.MIMEText import MIMEText

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)


pygame.init()
pygame.mixer.init()
alarmSound = pygame.mixer.Sound("./audio/alarm.wav")
bildName = 'na'

def mailSend():
	fromaddr = 'SEND-FROM-MAILADRESS'
	toaddrs  = 'SEND-ALARMTO-MAILADRESS'
	
	msg=MIMEMultipart()
	msg['From']='Spi - Observer'
	msg['To']='raspberryspiprojekt@gmail.com'
	msg['Subject']='Message from SPi - Motion detected'
	
	bildDateiName = './images/' + bildName + '.jpg'
	bildDatei = file(bildDateiName)
	image = MIMEImage(bildDatei.read(), _subtype="jpeg")
	msg.attach(image)

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
