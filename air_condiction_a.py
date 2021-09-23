import os
import serial
import paho.mqtt.client as mqtt
import json
import time

broker_ip = "10.20.0.19"
broker_port = 1883

s = serial.Serial("/dev/ttyS0", 57600) 

network_status = 0

while (not network_status):
    try:
        client = mqtt.Client()
        client.connect(broker_ip, broker_port)
        network_status = 1
    except:
        pass

#f = os.popen('ifconfig br-lan | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # AP model
f = os.popen('ifconfig apcli0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') # Station model  
inet_addr = f.read()

while(True):
    data = s.readline()
    if (len(data.split("\r")) > 0):
        mcu_data = data.split("\r")[0]
        mqtt_data = json.loads(mcu_data)
        mqtt_data["ip"] = inet_addr.split("\n")[0]
        try:
            client.publish("air_condiction/A", json.dumps(mqtt_data))
        except:
            pass
        print(json.dumps(mqtt_data))