import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

from bmi import calculate_bmi, get_category
from validation import validate
from Database import save_record,get_all_records,get_bmi_data


def start_app():

    # ---------------- Create Window ----------------
    window = tk.Tk()
    window.title("BMI Calculator")
    window.geometry("500x700")
    window.resizable(False, False)

    window.configure(bg="#EAF6FF")

    # ---------------- Functions ----------------

    def calculate():

        weight = weight_entry.get()
        height = height_entry.get()

        valid, message = validate(weight, height)

        if not valid:
            messagebox.showerror("Input Error", message)
            return

        weight = float(weight)
        height = float(height)

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        bmi_label.config(text=f"BMI : {bmi}")
        category_label.config(text=f"Category : {category}")

    def reset():

        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        weight_entry.delete(0, tk.END)
        height_entry.delete(0, tk.END)

        gender.set("")

        bmi_label.config(text="BMI : ")
        category_label.config(text="Category : ")

    def save():

        name = name_entry.get()
        age = age_entry.get()
        gender_value = gender.get()

        weight = weight_entry.get()
        height = height_entry.get()

        valid, message = validate(weight, height)

        if not valid:
            messagebox.showerror("Input Error", message)
            return

        bmi = calculate_bmi(float(weight), float(height))
        category = get_category(bmi)

        save_record(
            name,
            age,
            gender_value,
            float(weight),
            float(height),
            bmi,
            category
        )

        messagebox.showinfo(
            "Success",
            "Record Saved Successfully!"
        )
    def view_history():

     history_window = tk.Toplevel(window)
     history_window.title("BMI History")
     history_window.geometry("900x400")

     from tkinter import ttk

     columns = (
        "ID",
        "Name",
        "Age",
        "Gender",
        "Weight",
        "Height",
        "BMI",
        "Category"
    )

     tree = ttk.Treeview(
        history_window,
        columns=columns,
        show="headings"
    )

     for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=100)

     records = get_all_records()

     for row in records:
        tree.insert("", tk.END, values=row)

     tree.pack(fill="both", expand=True)
    def show_graph():

     data = get_bmi_data()

     if not data:
        messagebox.showinfo(
            "No Data",
            "No records found!"
        )
        return

     names = []
     bmi_values = []

     for name, bmi in data:
        names.append(name)
        bmi_values.append(bmi)

     plt.figure(figsize=(8, 5))
     plt.bar(names, bmi_values)

     plt.title("BMI Records")
     plt.xlabel("Name")
     plt.ylabel("BMI")

     plt.show()
    # ---------------- Title ----------------

    tk.Label(
     window,
     text="BMI Calculator",
     font=("Arial", 22, "bold"),
     bg="#EAF6FF",
     fg="#003366",
     ).pack(pady=20)

    # ---------------- Name ----------------

    tk.Label(
        window,
        text="Name",
        font=("Arial", 12),
        bg="#EAF6FF",
     ).pack()

    name_entry = tk.Entry(window, width=35)
    name_entry.pack(pady=5)

    # ---------------- Age ----------------

    tk.Label(
        window,
        text="Age",
        font=("Arial", 12),
        bg="#EAF6FF",
    ).pack()

    age_entry = tk.Entry(window, width=35)
    age_entry.pack(pady=5)

    # ---------------- Gender ----------------

    tk.Label(
        window,
        text="Gender",
        font=("Arial", 12),
        bg="#EAF6FF"
    ).pack()

    gender = tk.StringVar(value="")

    tk.Radiobutton(
        window,
        text="Male",
        variable=gender,
        value="Male"
        
    ).pack()

    tk.Radiobutton(
        window,
        text="Female",
        variable=gender,
        value="Female"
    ).pack()

    # ---------------- Weight ----------------

    tk.Label(
        window,
        text="Weight (kg)",
        font=("Arial", 12),
        bg="#EAF6FF"
    ).pack()

    weight_entry = tk.Entry(window, width=35)
    weight_entry.pack(pady=5)

    # ---------------- Height ----------------

    tk.Label(
        window,
        text="Height (m)",
        font=("Arial", 12),
        bg="#EAF6FF"
    ).pack()

    height_entry = tk.Entry(window, width=35)
    height_entry.pack(pady=5)

    # ---------------- Buttons ----------------

    tk.Button(
        window,
        text="Calculate",
        width=20,
        command=calculate,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 10, "bold"),   
    ).pack(pady=5)

    tk.Button(
        window,
        text="Reset",
        width=20,
        command=reset,
        bg="#FF9800",
        fg="white",
        font=("Arial", 10, "bold")    
    ).pack(pady=5)

    tk.Button(
        window,
        text="Save",
        width=20,
        command=save,
        bg="#2196F3",
        fg="white",
        font=("Arial", 10, "bold") 
        
    ).pack(pady=5)

    tk.Button(
        window,
        text="View History",
        width=20,
        command=view_history,
        bg="#E5718A",
        fg="white"
    ).pack(pady=5)

    tk.Button(
        window,
        text="Show Graph",
        width=20,
        command=show_graph,
        bg="#98E2B5",

    ).pack(pady=5)

    tk.Button(
        window,
        text="Exit",
        width=20,
        command=window.destroy,
        bg="#ECBE93"
    ).pack(pady=5)

    # ---------------- Result ----------------

    bmi_label = tk.Label(
      window,
      text="BMI : ",
      font=("Arial", 14, "bold"),
      fg="blue",
      bg="#EAF6FF"
)
    bmi_label.pack(pady=10)

    category_label = tk.Label(
        window,
        text="Category : ",
        font=("Arial", 12, "bold"),
        fg="green"
    )
    category_label.pack()

    # ---------------- Run ----------------

    window.mainloop()