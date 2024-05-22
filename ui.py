import tkinter as tk
from tkinter import ttk

class AppUI:
    def __init__(self, root, topics):
        self.root = root
        self.topics = topics

        icon = tk.PhotoImage(file='logo.png')
        root.iconphoto(True, icon)

        self.root.title("Group 1 - ĐỒ ÁN 1")
        self.root.geometry("620x400") 

        self.database_label = tk.Label(root, text="Database", font=("Time New Roman", 12))
        self.database_label.grid(row=0, column=0, padx=10, pady=10)

        self.selected_db = tk.StringVar()
        self.db_combobox = ttk.Combobox(root, textvariable=self.selected_db, font=("Time New Roman", 12), state="readonly")
        self.db_combobox['values'] = tuple(self.topics)
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

    def connect_mqtt(self):
        # Implement MQTT connection
        pass

    def update_table(self):
        # Implement table update
        pass
