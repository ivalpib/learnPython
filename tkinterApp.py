# import tkinter as tk
# from tkinter import messagebox

# def addbtn():

#     pass 

# def find_sum():
#     num1 = entry1.get()
#     num2 = entry1.get()
#     operator = operator_entry.get()
#     operator
#     if num1.isdigit() and num2.isdigit():
#         result = int(num1) + int(num2)
#         messagebox.showinfo("Result", f"sum: {result}")
#     else:
#         messagebox.showerror("Error","Enter valid numbers")
# root = tk.Tk()
# root.title("TKinter App")
# root.geometry("300x300")
# entry1 = tk.Entry(root)
# entry1.pack(pady=5)
# # entry2 = tk.Entry(root)
# # entry2.pack(pady=5)

# button = tk.Button(root, text="+", command=addbtn)
# button.pack(pady=5)

# button = tk.Button(root, text="Calculate", command=find_sum)
# button.pack(pady=5)

# root.mainloop()

import tkinter as tk

def addbtn():
    num1 = entry.get()
    

def calculate():
    expression = entry.get()
    try:
        # Evaluate the expression using eval (ensure it's safe in your context)
        result = eval(expression)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text="Error: " + str(e))

root = tk.Tk()

entry = tk.Entry(root)
entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=5)

add_button = tk.Button(root, text="+", command=addbtn)
add_button.pack(pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

root.mainloop()
