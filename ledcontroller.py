import socket
import sys
import json
import time
import subprocess
import traceback 

r_val = 0
g_val = 0
b_val = 0

r_pin = "9"
g_pin = "11"
b_pin = "10"

LastUpdate_R = 0
LastUpdate_G = 0
LastUpdate_B = 0

max_value = 255
min_value = 0

ticks_per_second = 20


def getSafeRGBValue(inValue):
	returnValue = 0
	numberValue = 0
	
	try:

		if(isinstance(inValue, str)):
			numberValue = int(inValue)
		else:
			numberValue = inValue

		if (numberValue > max_value):
			returnValue = max_value
		elif (numberValue < min_value):
			returnValue = min_value
		else:
			returnValue = numberValue
	except:
		print("BAD DATA in RGB Value")

	return returnValue



def RGBBreathe(R, G, B, inTime):
	
	current_R = 0;
	current_G = 0;
	current_B = 0;

	sleep_time = float(1.0/float(ticks_per_second))

	#print(str(R),str(G),str(B),str(inTime))

	num_ticks = int((ticks_per_second * float(inTime)) / 2)
	for x in range (0, num_ticks):
		current_R = getSafeRGBValue(int((float(x) / float(num_ticks) * float(R))))
		current_G = getSafeRGBValue(int((float(x) / float(num_ticks) * float(G))))
		current_B = getSafeRGBValue(int((float(x) / float(num_ticks) * float(B))))

		writeRGB(current_R, current_G, current_B)
		time.sleep(sleep_time)


	
	for x in range (num_ticks, 0, -1):
		current_R = getSafeRGBValue(int((float(x) / float(num_ticks) * float(R))))
		current_G = getSafeRGBValue(int((float(x) / float(num_ticks) * float(G))))
		current_B = getSafeRGBValue(int((float(x) / float(num_ticks) * float(B))))
	
		writeRGB(current_R, current_G, current_B)
		time.sleep(sleep_time)

	writeRGB(0, 0, 0)

def RGBChange(R, G, B, inTime):
	

	current_R = LastUpdate_R;
	current_G = LastUpdate_G;
	current_B = LastUpdate_B;

	start_R = LastUpdate_R;
	start_G = LastUpdate_G;
	start_B = LastUpdate_B;

	sleep_time = float(1.0/float(ticks_per_second))

	#print(str(R),str(G),str(B),str(inTime))

	num_ticks = int((ticks_per_second * float(inTime)))

	for x in range (0, num_ticks):
		temp_R = (float(R - start_R) * (float(x) / float(num_ticks)) + start_R)
		temp_G = (float(G - start_G) * (float(x) / float(num_ticks)) + start_G)
		temp_B = (float(B - start_B) * (float(x) / float(num_ticks)) + start_B)
		
		current_R = getSafeRGBValue(int(temp_R))
		current_G = getSafeRGBValue(int(temp_G))
		current_B = getSafeRGBValue(int(temp_B))

		#print(str(current_R), str(current_G), str(current_B))
		#print(str(delta_R), str(delta_G), str(delta_B))
		writeRGB(current_R, current_G, current_B)
		time.sleep(sleep_time)

	writeRGB(R, G, B)


def writeRGB(R, G, B):
	try:
		bashCommand = "pigs p " + r_pin + " " + str(R) + " p " + g_pin + " " + str(G) + " p " + b_pin + " " + str(B)
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		
		global LastUpdate_R
		global LastUpdate_G
		global LastUpdate_B

		LastUpdate_R = R
		LastUpdate_G = G
		LastUpdate_B = B
	except Exception:
		print("ERROR outputting to LED")



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the port
server_address = ('0.0.0.0', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
	# Wait for a connection
	print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock.accept()
	try:
        	print >>sys.stderr, 'connection from', client_address

        	# Receive the data in small chunks and retransmit it
        	while True:
            		data = connection.recv(100)
            		# print >>sys.stderr, 'received "%s"' % data
            		
			if data:
				try:
					tempJSON = json.loads(data)
					print("R: " + str(tempJSON['R']))
					print("G: " + str(tempJSON['G']))
					print("B: " + str(tempJSON['B']))
					print("TYPE: " + str(tempJSON['TYPE']))

					if('TYPE' in tempJSON):
						if(tempJSON['TYPE'] == "SET"):
							r_val = getSafeRGBValue(tempJSON['R'])
							g_val = getSafeRGBValue(tempJSON['G'])
							b_val = getSafeRGBValue(tempJSON['B'])

							writeRGB(r_val, g_val, b_val)

						elif(tempJSON['TYPE'] == "BREATHE"):
							r_val = getSafeRGBValue(tempJSON['R'])
							g_val = getSafeRGBValue(tempJSON['G'])
							b_val = getSafeRGBValue(tempJSON['B'])
							duration = tempJSON['DURATION']
							RGBBreathe(r_val, g_val, b_val, duration)

						elif(tempJSON['TYPE'] == "CHANGE"):
							r_val = getSafeRGBValue(tempJSON['R'])
							g_val = getSafeRGBValue(tempJSON['G'])
							b_val = getSafeRGBValue(tempJSON['B'])
							duration = tempJSON['DURATION']
							RGBChange(r_val, g_val, b_val, duration)


				except Exception:
					print("Bad JSON")
					traceback.print_exc()
					print("Input: " + str(data))
                	print >>sys.stderr, 'no more data from', client_address
                	break
            
    	finally:
        	# Clean up the connection
        	connection.close()



