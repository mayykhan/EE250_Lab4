import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

def on_message_from_ping(client, userdata, message):
    print("A: Pong Received - pong: " + message.payload.decode())
    a = int(message.payload.decode()) + 1
    client.publish("maykhan/ping", str(a))
    print("A: Ping Published - ping: {a}")

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect("192.168.xx.xx", port=1883, keepalive=60)
    client.subscribe("maykhan/pong")
    client.message_callback_add("maykhan/ping", on_message_from_ping)
    client.publish("maykhan/ping", "67")
    print("A: Ping Published - ping: 67")

    client.loop_forver()