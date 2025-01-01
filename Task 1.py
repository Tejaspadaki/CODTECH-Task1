import tkinter as tk
from tkinter import messagebox

class GUICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        # Input field
        self.input_field = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
        self.input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20)

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        # Creating and placing buttons dynamically
        row_val, col_val = 1, 0
        for text in button_texts:
            if text == "=":
                button = tk.Button(
                    self.root, text=text, font=("Arial", 20), bg="lightgreen", command=self.calculate
                )
            elif text == "C":
                button = tk.Button(
                    self.root, text=text, font=("Arial", 20), bg="red", fg="white", command=self.clear_input
                )
            else:
                button = tk.Button(
                    self.root, text=text, font=("Arial", 20), command=lambda t=text: self.append_to_input(t)
                )

            button.grid(row=row_val, column=col_val, padx=10, pady=10, ipadx=20, ipady=20)

            col_val += 1
            if col_val > 3:  # Move to the next row after 4 columns
                col_val = 0
                row_val += 1

    def append_to_input(self, value):
        """Append a value (button click) to the input field."""
        self.input_field.insert(tk.END, value)

    def clear_input(self):
        """Clear the input field."""
        self.input_field.delete(0, tk.END)

    def calculate(self):
        """Evaluate the expression in the input field."""
        try:
            expression = self.input_field.get()
            result = eval(expression)  # Evaluate the mathematical expression
            self.clear_input()
            self.input_field.insert(0, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = GUICalculator(root)
    root.mainloop()
