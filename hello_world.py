import math
import tkinter as tk
from tkinter import messagebox
#code by Jun Jie Ou Yang

#Now we test again
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def square(a):
    return a * a

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Cannot calculate square root of a negative number."

def create_calculator_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("300x400")
    window.resizable(False, False)
    window.configure(bg="#f0f0f0")

    # Variables to store input values
    num1 = tk.StringVar()
    num2 = tk.StringVar()
    result = tk.StringVar(value="Result will appear here")  # Set initial value

    def calculate(operation):
        try:
            if operation in ["square", "sqrt"]:
                n1 = float(num1.get())
                if operation == "square":
                    res = square(n1)
                    # Remove debug print, focus on GUI display
                    result.set(str(res))
                else:  # square root
                    res = square_root(n1)
                    result.set(str(res))
            else:
                n1 = float(num1.get())
                n2 = float(num2.get())
                if operation == "add":
                    res = add(n1, n2)
                    result.set(str(res))
                elif operation == "subtract":
                    res = subtract(n1, n2)
                    result.set(str(res))
                elif operation == "multiply":
                    res = multiply(n1, n2)
                    result.set(str(res))
                elif operation == "divide":
                    res = divide(n1, n2)
                    result.set(str(res))
            # Force update the window to display the result
            window.update_idletasks()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers")
    
    # Create GUI elements
    title_label = tk.Label(window, text="Calculator", font=("Arial", 18, "bold"), bg="#f0f0f0")
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    num1_label = tk.Label(window, text="First Number:", bg="#f0f0f0")
    num1_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    num1_entry = tk.Entry(window, textvariable=num1)
    num1_entry.grid(row=1, column=1, padx=10, pady=10)
    
    num2_label = tk.Label(window, text="Second Number:", bg="#f0f0f0")
    num2_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    num2_entry = tk.Entry(window, textvariable=num2)
    num2_entry.grid(row=2, column=1, padx=10, pady=10)
    
    # Create a frame for the operation buttons
    button_frame = tk.Frame(window, bg="#f0f0f0")
    button_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    # Add operation buttons  
    add_button = tk.Button(button_frame, text="Add", width=8, command=lambda: calculate("add"))
    add_button.grid(row=0, column=0, padx=5, pady=5)
    
    subtract_button = tk.Button(button_frame, text="Subtract", width=8, command=lambda: calculate("subtract"))
    subtract_button.grid(row=0, column=1, padx=5, pady=5)
    
    multiply_button = tk.Button(button_frame, text="Multiply", width=8, command=lambda: calculate("multiply"))
    multiply_button.grid(row=1, column=0, padx=5, pady=5)
    
    divide_button = tk.Button(button_frame, text="Divide", width=8, command=lambda: calculate("divide"))
    divide_button.grid(row=1, column=1, padx=5, pady=5)
    
    square_button = tk.Button(button_frame, text="Square", width=8, command=lambda: calculate("square"))
    square_button.grid(row=2, column=0, padx=5, pady=5)
    
    sqrt_button = tk.Button(button_frame, text="Sqrt", width=8, command=lambda: calculate("sqrt"))
    sqrt_button.grid(row=2, column=1, padx=5, pady=5)
    
    # Result display - make it more noticeable with different colors
    result_label = tk.Label(window, text="Result:", bg="#f0f0f0", font=("Arial", 12, "bold"))
    result_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    
    # Make the result display more visible with different colors
    result_display = tk.Label(window, textvariable=result, 
                             bg="#e6f2ff", fg="#0066cc", font=("Arial", 14, "bold"), 
                             width=20, height=2, relief="groove", bd=3, anchor="center")
    result_display.grid(row=4, column=1, padx=10, pady=10)
    
    # Clear button
    clear_button = tk.Button(window, text="Clear", width=8, 
                           command=lambda: [num1.set(""), num2.set(""), result.set("Result will appear here")])
    clear_button.grid(row=5, column=0, columnspan=2, pady=10)
    
    window.mainloop()

if __name__ == "__main__":
    create_calculator_gui()