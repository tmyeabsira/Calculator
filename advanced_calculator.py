import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Advanced Calculator")

#default font
default_font = ('Arial', 15)


# Entry widget for displaying the input and output
entry = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define a dictionary of allowed functions and constants
allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
allowed_names.update({
    'pi': math.pi,
    'e': math.e,
    'sqrt': math.sqrt,
    'abs': abs,
    'round': round,
    'log': math.log10,  # Base-10 logarithm
    'ln': math.log,     # Natural logarithm
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan
})

# Function to safely evaluate the mathematical expression
def safe_eval(expr):
    code = compile(expr, "<string>", "eval")
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"Use of '{name}' not allowed")
    return eval(code, {"__builtins__": {}}, allowed_names)

# Function to handle button clicks
def button_click(item):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(item))

# Function to clear the entry field
def button_clear():
    entry.delete(0, tk.END)

# Function to calculate the expression
def button_equal():
    expr = entry.get()
    try:
        result = safe_eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create number buttons
buttons_numbers = []
for i in range(10):
    button = tk.Button(root, text=str(i), padx=20, pady=20,
                       command=lambda x=i: button_click(str(x)), font=default_font)
    buttons_numbers.append(button)


# Operator buttons
button_add = tk.Button(root, text='+', padx=20, pady=20, command=lambda: button_click('+'), font=default_font)
button_subtract = tk.Button(root, text='-', padx=22, pady=20, command=lambda: button_click('-'), font=default_font)
button_multiply = tk.Button(root, text='*', padx=22, pady=20, command=lambda: button_click('*'), font=default_font)
button_divide = tk.Button(root, text='/', padx=22, pady=20, command=lambda: button_click('/'), font=default_font)
button_decimal = tk.Button(root, text='.', padx=22, pady=20, command=lambda: button_click('.'), font=('Arial', 20))
button_open_paren = tk.Button(root, text='(', padx=22, pady=20, command=lambda: button_click('('), font=default_font)
button_close_paren = tk.Button(root, text=')', padx=22, pady=20, command=lambda: button_click(')'), font=default_font)

# Function buttons
button_sin = tk.Button(root, text='sin', padx=16, pady=20, command=lambda: button_click('sin('), font=default_font)
button_cos = tk.Button(root, text='cos', padx=16, pady=20, command=lambda: button_click('cos('), font=default_font)
button_tan = tk.Button(root, text='tan', padx=16, pady=20, command=lambda: button_click('tan('), font=default_font)
button_log = tk.Button(root, text='log', padx=16, pady=20, command=lambda: button_click('log('), font=default_font)
button_ln = tk.Button(root, text='ln', padx=20, pady=20, command=lambda: button_click('ln('), font=default_font)
button_sqrt = tk.Button(root, text='√', padx=22, pady=20, command=lambda: button_click('sqrt('), font=default_font)
button_pi = tk.Button(root, text='π', padx=22, pady=20, command=lambda: button_click('pi'), font=default_font)
button_e = tk.Button(root, text='e', padx=24, pady=20, command=lambda: button_click('e'), font=default_font)

# Clear and equal buttons
button_clear = tk.Button(root, text='C', padx=20, pady=20, command=button_clear, font=default_font)
button_equal = tk.Button(root, text='=', padx=20, pady=20, command=button_equal, font=default_font)


# Position the buttons on the grid
# buttons = [
#     [buttons_numbers[7], buttons_numbers[8], buttons_numbers[9], button_divide, button_sin],
#     [buttons_numbers[4], buttons_numbers[5], buttons_numbers[6], button_multiply, button_cos],
#     [buttons_numbers[1], buttons_numbers[2], buttons_numbers[3], button_subtract, button_tan],
#     [buttons_numbers[0], button_decimal, button_open_paren, button_close_paren, button_add],
#     [button_log, button_ln, button_sqrt, button_pi, button_e],
#     [button_clear, button_equal]
# ]

buttons = [
    [button_clear, button_sqrt],
    [button_open_paren, button_close_paren, button_sin, button_cos, button_tan],
    [buttons_numbers[7], buttons_numbers[8], buttons_numbers[9], button_pi, button_e],
    [buttons_numbers[4], buttons_numbers[5], buttons_numbers[6], button_log, button_ln],
    [buttons_numbers[1], buttons_numbers[2], buttons_numbers[3], button_multiply, button_divide],
    [button_equal, buttons_numbers[0], button_decimal, button_add, button_subtract]
]

for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        btn.grid(row=i+1, column=j, sticky='nsew')

# Configure the grid to make buttons expand evenly
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
