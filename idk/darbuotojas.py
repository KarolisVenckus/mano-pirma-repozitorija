import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import sys
import os
import shutil

# Create the Tkinter window
window = tk.Tk()
window.title("Employee Management System")
window.geometry("400x500")

# Connect to the SQLite database
conn = sqlite3.connect('darbuotojai.db')
cursor = conn.cursor()

# Function for creating an employee
def create_employee():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    birth_date = entry_birth_date.get()
    position = entry_position.get()
    salary = entry_salary.get()
    hired_date = datetime.now().date()

    cursor.execute('''
        INSERT INTO employees (first_name, last_name, birth_date, position, salary, hired_date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, birth_date, position, salary, hired_date))
    conn.commit()
    messagebox.showinfo("Success", "Employee successfully created!")
    refresh_employee_list()

# Function for deleting an employee
def delete_employee():
    selected_employee = listbox_employees.get(listbox_employees.curselection())
    employee_id = selected_employee.split(" - ")[0]

    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this employee?")
    if confirm:
        cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
        conn.commit()
        messagebox.showinfo("Success", "Employee successfully deleted!")
        refresh_employee_list()

# Function for updating an employee's information
def update_employee():
    selected_employee = listbox_employees.get(listbox_employees.curselection())
    employee_id = selected_employee.split(" - ")[0]

    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    birth_date = entry_birth_date.get()
    position = entry_position.get()
    salary = entry_salary.get()

    cursor.execute('''
        UPDATE employees SET first_name = ?, last_name = ?, birth_date = ?, position = ?, salary = ?
        WHERE id = ?
    ''', (first_name, last_name, birth_date, position, salary, employee_id))
    conn.commit()
    messagebox.showinfo("Success", "Employee successfully updated!")
    refresh_employee_list()

# Function to load employee data
def load_employee_data(event):
    selected_employee = listbox_employees.get(listbox_employees.curselection())
    employee_id = selected_employee.split(" - ")[0]

    cursor.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
    employee = cursor.fetchone()

    entry_first_name.delete(0, tk.END)
    entry_first_name.insert(tk.END, employee[1])
    entry_last_name.delete(0, tk.END)
    entry_last_name.insert(tk.END, employee[2])
    entry_birth_date.delete(0, tk.END)
    entry_birth_date.insert(tk.END, employee[3])
    entry_position.delete(0, tk.END)
    entry_position.insert(tk.END, employee[4])
    entry_salary.delete(0, tk.END)
    entry_salary.insert(tk.END, employee[5])

# Function to refresh the listbox with all the employees
def refresh_employee_list():
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    listbox_employees.delete(0, tk.END)
    for employee in employees:
        listbox_employees.insert(tk.END, f"{employee[0]} - {employee[1]} {employee[2]}")

# Create labels and entry fields
label_first_name = tk.Label(window, text="First Name:")
label_first_name.pack()
entry_first_name = tk.Entry(window)
entry_first_name.pack()

label_last_name = tk.Label(window, text="Last Name:")
label_last_name.pack()
entry_last_name = tk.Entry(window)
entry_last_name.pack()

label_birth_date = tk.Label(window, text="Birth Date (YYYY-MM-DD):")
label_birth_date.pack()
entry_birth_date = tk.Entry(window)
entry_birth_date.pack()

label_position = tk.Label(window, text="Position:")
label_position.pack()
entry_position = tk.Entry(window)
entry_position.pack()

label_salary = tk.Label(window, text="Salary:")
label_salary.pack()
entry_salary = tk.Entry(window)
entry_salary.pack()

# Create buttons
button_create = tk.Button(window, text="Create", command=create_employee)
button_create.pack()

button_update = tk.Button(window, text="Update", command=update_employee)
button_update.pack()

button_delete = tk.Button(window, text="Delete", command=delete_employee)
button_delete.pack()

# Create the listbox to display employees
listbox_employees = tk.Listbox(window)
listbox_employees.pack()

listbox_employees.bind("<<ListboxSelect>>", load_employee_data)

# Update the listbox with all employees
refresh_employee_list()

# Function for creating the executable file
def create_executable():
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        current_path = sys._MEIPASS
        script_file = sys.executable
    else:
        # Running as script
        current_path = os.path.dirname(os.path.abspath(__file__))
        script_file = __file__

    executable_file_path = os.path.join(current_path, 'darbuotojas.exe')
    
    # Remove any previous executable file
    if os.path.exists(executable_file_path):
        os.remove(executable_file_path)

    os.system(f'pyinstaller --onefile "{script_file}"')
    
    # Move the executable to the current directory
    shutil.move(os.path.join(current_path, 'dist', 'darbuotojas.exe'), executable_file_path)
    
    # Remove build and dist directories
    shutil.rmtree(os.path.join(current_path, 'build'))
    shutil.rmtree(os.path.join(current_path, 'dist'))

    messagebox.showinfo("Success", "Executable created successfully!")

# Create the button to create the executable
button_create_exe = tk.Button(window, text="Create Executable", command=create_executable)
button_create_exe.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()