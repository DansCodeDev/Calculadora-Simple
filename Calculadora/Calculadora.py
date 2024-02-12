import tkinter as tk
import math

class CalculadoraCientifica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.configure(background='#f0f0f0')
        
        self.entry = tk.Entry(self, width=50, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.create_buttons()

        self.bind("<Return>", self.calcular)

        self.error = False

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 1, 4), ('(', 2, 4), (')', 3, 4), ('^', 4, 4),
            ('sqrt', 5, 0), ('pi', 5, 1)
        ]

        for (text, row, column) in buttons:
            self.create_button(text, row, column)

    def create_button(self, text, row, column):
        button = tk.Button(self, text=text, width=8, height=3, font=('Arial', 14),
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)
        
        if text.isdigit() or text == '.':
            button.configure(bg='#e0e0e0')
        elif text in ['=', 'C', '(', ')', '^', 'sqrt', 'pi']:
            button.configure(bg='#f0f0f0')
        else:
            button.configure(bg='#d9d9d9')

    def on_button_click(self, char):
        if self.error:
            self.entry.delete(0, tk.END)
            self.error = False
        
        if char == '=':
            self.calcular()
        elif char == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, char)

    def calcular(self, event=None):
        try:
            expresion = self.entry.get()
            resultado = eval(expresion)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, resultado)
            self.error = False
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            self.error = True

def main():
    app = CalculadoraCientifica()
    app.mainloop()

if __name__ == "__main__":
    main()
