import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket
a = 0
def on_message(client, userdata, message):
    print("Pong Callback - pong: " + int(message.payload.decode()))
    a = int(message.payload.decode()) + 1
    client.publish("maykhan/ping", str(a))

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect("192.168.xx.xx", port=1883, keepalive=60)
    client.subscribe("maykhan/pong")
    client.publish("maykhan/ping", "67")
    client.loop_forver()