

import time
import socket
import json

def setRGB(r, g, b):
	# testData = '{"TYPE":"CHANGE","R":r,"G":g,"B":b,"DURATION":20}'
	testData = {}
	testData['TYPE'] = 'CHANGE'
	testData['R'] = r
	testData['G'] = g
	testData['B'] = b
	testData['DURATION'] = 60


	pi0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = "terry-rpi0"
	port = 10000
	pi0.connect((host, port))
	pi0.send(json.dumps(testData).encode('utf-8'))
	pi0.close()	

	pi1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "terry-rpi1"
        port = 10000
        pi1.connect((host, port))
        pi1.send(json.dumps(testData).encode('utf-8'))
        pi1.close()

	pi2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "terry-rpi2"
        port = 10000
        pi2.connect((host, port))
        pi2.send(json.dumps(testData).encode('utf-8'))
        pi2.close()

	time.sleep(30)

def setInitalRGB():
        # testData = '{"TYPE":"CHANGE","R":r,"G":g,"B":b,"DURATION":20}'
        testData = {}
        testData['TYPE'] = 'SET'
        testData['R'] = 0
        testData['G'] = 0
        testData['B'] = 0


        pi0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "terry-rpi0"
        port = 10000
        pi0.connect((host, port))
        pi0.send(json.dumps(testData).encode('utf-8'))
        pi0.close()

        pi1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "terry-rpi1"
        port = 10000
        pi1.connect((host, port))
        pi1.send(json.dumps(testData).encode('utf-8'))
        pi1.close()

        pi2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "terry-rpi2"
        port = 10000
        pi2.connect((host, port))
        pi2.send(json.dumps(testData).encode('utf-8'))
        pi2.close()


setInitalRGB()


