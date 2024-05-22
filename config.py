
import random
broker = 'broker.emqx.io'
port = 1883
topic = 'v1/devices/me/telemetry'
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'phamlong'
password = 'Longkm123'