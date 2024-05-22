# # python3.8

# import random

# from paho.mqtt import client as mqtt_client


# broker = 'broker.emqx.io'
# port = 1883
# topic = 'v1/devices/me/telemetry'
# # generate client ID with pub prefix randomly
# client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'phamlong'
# password = 'Longkm123'


# def connect_mqtt() -> mqtt_client:
#     def on_connect(client, userdata, flags, rc):
#         if rc == 0:
#             print("Connected to MQTT Broker!")
#         else:
#             print("Failed to connect, return code %d\n", rc)

#     client = mqtt_client.Client(client_id)
#     # client.tls_set(ca_certs='./server-ca.crt')
#     client.username_pw_set(username, password)
#     client.on_connect = on_connect
#     client.connect(broker, port)
#     return client


# def subscribe(client: mqtt_client):
#     def on_message(client, userdata, msg):
#         print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

#     client.subscribe(topic)
#     client.on_message = on_message


# def run():
#     client = connect_mqtt()
#     subscribe(client)
#     client.loop_forever()


# if __name__ == '__main__':
#     run()

import tkinter as tk
from tkinter import ttk
from paho.mqtt import client as mqtt_client
import random
from datetime import datetime  # Thêm import này

broker = 'broker.emqx.io'
port = 1883

class AppUI:
    def __init__(self, root):
        self.root = root
        icon = tk.PhotoImage(file='logo.png')
        root.iconphoto(True, icon)

        self.root.title("Group 1 - ĐỒ ÁN 1")
        self.root.geometry("620x400") 

        self.database_label = tk.Label(root, text="Database", font=("Time New Roman", 12))
        self.database_label.grid(row=0, column=0, padx=10, pady=10)

        self.selected_db = tk.StringVar()
        self.db_combobox = ttk.Combobox(root, textvariable=self.selected_db, font=("Time New Roman", 12), state="readonly")
        self.db_combobox['values'] = ('v1/devices/me/telemetry',)
        self.db_combobox.grid(row=0, column=1, padx=10, pady=10)

        self.connect_button = tk.Button(root, text="Connect",font=("Time New Roman", 14), command=self.connect_mqtt)
        self.connect_button.grid(row=0, column=2, padx=10, pady=10)

        self.data_tree = ttk.Treeview(root, columns=("Time", "Protocols", "Value"), show="headings", height=15)
        self.data_tree.heading("Time", text="Time",anchor=tk.CENTER)
        self.data_tree.heading("Protocols", text="Protocols",anchor=tk.CENTER)
        self.data_tree.heading("Value", text="Value",anchor=tk.CENTER)
        self.data_tree.column("Time", width=200)
        self.data_tree.column("Protocols", width=200)
        self.data_tree.column("Value", width=200)
        self.data_tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # List to store inserted items
        self.inserted_items = []

        # MQTT variables
        self.client_id = f'python-mqtt-{random.randint(0, 100)}'
        self.username = 'phamlong'
        self.password = 'Longkm123'
        self.topic = 'v1/devices/me/telemetry'
        self.client = None

    def connect_mqtt(self):
        self.client = mqtt_client.Client(self.client_id)
        self.client.username_pw_set(self.username, self.password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker, port)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            self.client.subscribe(self.topic)
        else:
            print(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        # Lấy thời gian hiện tại
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        protocol = "MQTT"
        self.inserted_items.append((current_time, protocol, payload))
        self.update_table()

    def update_table(self):
        # Xóa các mục trước đó
        for item in self.data_tree.get_children():
            self.data_tree.delete(item)
        # Chèn các mục mới
        for item in self.inserted_items:
            self.data_tree.insert("", "end", values=item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppUI(root)
    root.mainloop()
