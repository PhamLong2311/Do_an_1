import tkinter as tk
from config import topic
from ui import AppUI
from mqtt import MQTTClient

if __name__ == "__main__":
    root = tk.Tk()
    topics = [topic]  # You can add more topics here
    app_ui = AppUI(root, topics)
    mqtt_client = MQTTClient()
    root.mainloop()
