import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create input fields and result label
entry_field1 = tk.Entry(window)
entry_field2 = tk.Entry(window)
result_label = tk.Label(window, text="")

# Create arithmetic operation buttons
add_button = tk.Button(window, text="+", command=lambda: calculate("add"))
subtract_button = tk.Button(window, text="-", command=lambda: calculate("subtract"))
multiply_button = tk.Button(window, text="*", command=lambda: calculate("multiply"))
divide_button = tk.Button(window, text="/", command=lambda: calculate("divide"))

# Create function to perform calculation
def calculate(operation):
    num1 = float(entry_field1.get())
    num2 = float(entry_field2.get())

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2

    result_label.config(text=f"Result: {result}")

# Place input fields, buttons, and result label on the window
entry_field1.grid(row=0, column=0)
entry_field2.grid(row=0, column=1)
add_button.grid(row=1, column=0)
subtract_button.grid(row=1, column=1)
multiply_button.grid(row=2, column=0)
divide_button.grid(row=2, column=1)
result_label.grid(row=3, columnspan=2)

# Run the Tkinter event loop
window.mainloop()