import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Define a string variable to store the user input
input_text = tk.StringVar()

# Create a display entry widget to show input and results
input_field = tk.Entry(root, textvariable=input_text, font=('Arial', 18), bd=8, insertwidth=2, width=14, borderwidth=4)
input_field.grid(row=0, column=0, columnspan=4)

# Function to update input text whenever a button is clicked
def button_click(item):
    current = input_text.get()
    input_text.set(current + str(item))

# Function to clear the display
def button_clear():
    input_text.set("")

# Function to evaluate the expression entered
def button_equal():
    try:
        result = str(eval(input_text.get()))  # Evaluate the expression
        input_text.set(result)  # Display result
    except:
        input_text.set("Error")  # Handle any errors

# Create the button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18),
                           command=button_equal)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18),
                           command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Add the clear button
clear_button = tk.Button(root, text='C', padx=20, pady=20, bd=8, fg="black", font=('Arial', 18),
                         command=button_clear)
clear_button.grid(row=4, column=2)

# Run the application
root.mainloop()
