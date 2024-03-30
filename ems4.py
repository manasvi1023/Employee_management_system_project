import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

# Create or connect to the SQLite database
conn = sqlite3.connect('employee_database2.db')
cursor = conn.cursor()

# Create the employee table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY,
        emp_name TEXT,
        emp_salary REAL
    )
''')
conn.commit()

# Function to add an employee record
def add_employee():
    emp_name = name_entry.get()
    emp_salary = float(salary_entry.get())
    
    cursor.execute('INSERT INTO employees (emp_name, emp_salary) VALUES (?, ?)', (emp_name, emp_salary))
    conn.commit()
    messagebox.showinfo("Success", f"Employee {emp_name} added successfully!")

# Function to delete an employee record
def delete_employee():
    emp_id = int(emp_id_entry.get())
    
    cursor.execute('DELETE FROM employees WHERE emp_id = ?', (emp_id,))
    conn.commit()
    messagebox.showinfo("Success", f"Employee ID {emp_id} deleted successfully!")

# Function to update an employee record
def update_employee():
    emp_id = int(emp_id_entry.get())
    emp_name = name_entry.get()
    emp_salary = float(salary_entry.get())
    
    cursor.execute('UPDATE employees SET emp_name=?, emp_salary=? WHERE emp_id=?', (emp_name, emp_salary, emp_id))
    conn.commit()
    messagebox.showinfo("Success", f"Employee ID {emp_id} updated successfully!")

# Function to search for an employee record
def search_employee():
    emp_id = int(emp_id_entry.get())
    
    cursor.execute('SELECT * FROM employees WHERE emp_id = ?', (emp_id,))
    row = cursor.fetchone()
    
    if row:
        name_entry.delete(0, tk.END)
        salary_entry.delete(0, tk.END)
        name_entry.insert(0, row[1])
        salary_entry.insert(0, row[2])
    else:
        messagebox.showinfo("Error", f"Employee with ID {emp_id} not found.")

# Create the GUI
root = tk.Tk()
root.title("Employee Management System")

image_path = "img 6.jpeg"  # Change this to your image path

# Load the image and create an ImageTk.PhotoImage object with resizing
new_size = (1500, 100)  # Adjust the size as needed
original_image = Image.open(image_path)
resized_image = original_image.resize(new_size)
employee_image = ImageTk.PhotoImage(resized_image)

# Create a label to display the image
image_label = tk.Label(root, image=employee_image)
image_label.grid(row=0, column=12, columnspan=10, padx=10, pady=10)


tk.Label(root, text="Employee ID:").grid(row=2, column=15, padx=20, pady=2)
tk.Label(root, text="Employee Name:").grid(row=3, column=15, padx=20, pady=2)
tk.Label(root, text="Employee Salary:").grid(row=4, column=15, padx=20, pady=2)

emp_id_entry = tk.Entry(root)
emp_id_entry.grid(row=2, column=16, columnspan=2)

name_entry = tk.Entry(root)
name_entry.grid(row=3, column=16,columnspan=2)

salary_entry = tk.Entry(root)
salary_entry.grid(row=4, column=16,columnspan=2)

add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.grid(row=10, column=12, columnspan=5, pady=8)

delete_button = tk.Button(root, text="Delete Employee", command=delete_employee)
delete_button.grid(row=10, column=13, columnspan=5, pady=8)

update_button = tk.Button(root, text="Update Employee", command=update_employee)
update_button.grid(row=10, column=14, columnspan=5, pady=8)

search_button = tk.Button(root, text="Search Employee", command=search_employee)
search_button.grid(row=10, column=15, columnspan=5, pady=8)

exit_button = tk.Button(root, text="Exit", command=exit)
exit_button.grid(row=10, column=16, columnspan=5, pady=8)



root.mainloop()

# Close the database connection when the GUI is closed
conn.close()