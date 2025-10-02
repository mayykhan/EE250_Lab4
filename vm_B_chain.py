import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket


def on_message_from_pong(client, userdata, message):
    print("B: Ping Received - ping: " + message.payload.decode())
    a = int(message.payload.decode()) + 1
    client.publish("maykhan/pong", str(a))
    print(f"B: Pong Published - pong: {a}")

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect("192.169.0.141", port=1883, keepalive=60)
    client.subscribe("maykhan/ping")
    client.on_message=on_message_from_pong
    client.message_callback_add("maykhan/pong", on_message_from_pong)
    client.loop_forever()