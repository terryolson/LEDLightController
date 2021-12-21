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
	testData['DURATION'] = 20


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
        testData['R'] = 255
        testData['G'] = 40
        testData['B'] = 0

	red = {}
	red['TYPE'] = 'SET'
        red['R'] = 255
        red['G'] = 0
        red['B'] = 0

	green = {}
        green['TYPE'] = 'SET'
        green['R'] = 0
        green['G'] = 255
        green['B'] = 0

	white = {}
        white['TYPE'] = 'SET'
        white['R'] = 255
        white['G'] = 255
        white['B'] = 255


        pi0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "terry-rpi0"
        port = 10000
        pi0.connect((host, port))
        pi0.send(json.dumps(red).encode('utf-8'))
        pi0.close()

        pi1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "terry-rpi1"
        port = 10000
        pi1.connect((host, port))
        pi1.send(json.dumps(green).encode('utf-8'))
        pi1.close()

        pi2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "terry-rpi2"
        port = 10000
        pi2.connect((host, port))
        pi2.send(json.dumps(white).encode('utf-8'))
        pi2.close()


setInitalRGB()


