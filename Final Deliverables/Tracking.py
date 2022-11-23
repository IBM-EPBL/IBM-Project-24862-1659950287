import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

organization = "w8ybgn"
deviceType = "NodeMCU"
deviceId = "12345"
authMethod = "token"
authToken = "12345678"
   
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
        name="Child"
        #latitude,longitude=10.937132,76.956266 #inarea
        latitude,longitude=10.838132,76.956266 #outarea
        data = { 'name' : name, 'lat': latitude ,'lon': longitude }
        #print data
        def myOnPublishCallback():
            print ("Published Latitude = ",latitude,"Longitude = ",longitude,"to IBM Watson")

        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(10)
        
deviceCli.disconnect()
