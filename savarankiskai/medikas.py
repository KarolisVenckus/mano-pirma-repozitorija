import sqlite3
import PySimpleGUI as sg
from datetime import date


class Medicine:
    def __init__(self, name, quantity, expiration_date):
        self.name = name
        self.quantity = quantity
        self.expiration_date = expiration_date

    def is_expired(self):
        return self.expiration_date < date.today()


class MedicalStore:
    def __init__(self):
        self.connection = sqlite3.connect("medical_store.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS medicines (name TEXT, quantity INTEGER, expiration_date TEXT)"
        )
        self.connection.commit()

    def add_medicine(self, name, quantity, expiration_date):
        self.cursor.execute(
            "INSERT INTO medicines VALUES (?, ?, ?)",
            (name, quantity, expiration_date.isoformat()),
        )
        self.connection.commit()

    def search_medicine(self, name):
        self.cursor.execute("SELECT * FROM medicines WHERE name=?", (name,))
        result = self.cursor.fetchone()
        if result:
            name, quantity, expiration_date_str = result
            expiration_date = date.fromisoformat(expiration_date_str)
            medicine = Medicine(name, quantity, expiration_date)
            return medicine
        return None

    def update_quantity(self, name, new_quantity):
        medicine = self.search_medicine(name)
        if medicine:
            self.cursor.execute(
                "UPDATE medicines SET quantity=? WHERE name=?", (new_quantity, name)
            )
            self.connection.commit()
            print(f"Quantity of {medicine.name} updated to {new_quantity}.")
        else:
            print("Medicine not found.")

    def remove_medicine(self, name):
        medicine = self.search_medicine(name)
        if medicine:
            self.cursor.execute("DELETE FROM medicines WHERE name=?", (name,))
            self.connection.commit()
            print(f"{medicine.name} removed from the stock.")
        else:
            print("Medicine not found.")

    def display_stock(self):
        self.cursor.execute("SELECT * FROM medicines")
        result = self.cursor.fetchall()
        if result:
            print("Medicine Stock:")
            for row in result:
                name, quantity, expiration_date_str = row
                expiration_date = date.fromisoformat(expiration_date_str)
                medicine = Medicine(name, quantity, expiration_date)
                status = "Expired" if medicine.is_expired() else "Valid"
                print(f"{medicine.name}: {medicine.quantity} ({status})")
        else:
            print("No medicines in stock.")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


# PySimpleGUI menu layout
layout = [
    [sg.Text("Medicine Name"), sg.InputText(key="-MEDICINE-")],
    [sg.Text("Quantity"), sg.InputText(key="-QUANTITY-")],
    [sg.Text("Expiration Date"), sg.InputText(key="-EXPIRATION-")],
    [sg.Button("Add Medicine"), sg.Button("Update Quantity"), sg.Button("Remove Medicine")],
    [sg.Button("Display Stock"), sg.Button("Exit")],
]

# Create the window
window = sg.Window("Medical Store Management", layout)

# Create the MedicalStore object
medical_store = MedicalStore()

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Add Medicine":
        medicine = values["-MEDICINE-"]
        quantity = int(values["-QUANTITY-"])
        expiration_date = date.fromisoformat(values["-EXPIRATION-"])
        medical_store.add_medicine(medicine, quantity, expiration_date)
        sg.popup(f"{medicine} added to the stock.")
    elif event == "Update Quantity":
        medicine = values["-MEDICINE-"]
        quantity = int(values["-QUANTITY-"])
        medical_store.update_quantity(medicine, quantity)
    elif event == "Remove Medicine":
        medicine = values["-MEDICINE-"]
        medical_store.remove_medicine(medicine)
    elif event == "Display Stock":
        medical_store.display_stock()

# Close the MedicalStore connection and the window
medical_store.close_connection()
window.close()