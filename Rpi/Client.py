#! /usr/bin/python3
# -*- coding: utf-8 -*-

from socket import *
from select import *
import sys
from time import ctime
import json
from collections import OrderedDict
import serial
import time
import os

#������ ����
HOST = '18.218.71.35' # EC2 ���� �ּ�
PORT = 10000 
BUFSIZE = 1024
ADDR = (HOST,PORT)

# �Ƶ��̳�� ����
if os.path.exists("/dev/ttyACM0") :
    tty = "/dev/ttyACM0"
elif os.path.exists("/dev/ttyACM1") :
    tty = "/dev/ttyACM1"

ArduinoSerial = serial.Serial(tty, 9600);
ArduinoSerial.flushInput();

# ������ �����ϱ� ���� ���� ����
clientSocket = socket(AF_INET, SOCK_STREAM)	
try:
	# ������ ���� �õ�
	clientSocket.connect(ADDR)	
	print("success!")
	data = clientSocket.recv(BUFSIZE)
	data_str = data.decode("UTF-8")
	print(data.decode())
	led = data_str.split(' ')[0]
	interval = data_str.split(' ')[1]		

	ArduinoSerial.write(b'StartDevice')
	print("StartDevice")
	time.sleep(3)

	if (led == "ledbad"):
			ArduinoSerial.write(b'StartLed')
			print("StartLed")
			time.sleep(5)

except Exception as e:
    print('%s:%s'%ADDR)
    sys.exit()