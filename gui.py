import tkinter as tk
from calculator import *
from memory import *

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.entry = tk.Entry(root, width=25, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def get(self):
        return float(self.entry.get())

    def show(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    def create_buttons(self):
        buttons = [
            ("+", lambda: self.binary(add)), ("-", lambda: self.binary(sub)),
            ("*", lambda: self.binary(mul)), ("/", lambda: self.binary(div)),
            ("%", lambda: self.binary(mod)), ("xʸ", lambda: self.binary(power)),
            ("√", lambda: self.unary(sqrt)), ("sin", lambda: self.unary(sin)),
            ("cos", lambda: self.unary(cos)), ("floor", lambda: self.unary(floor)),
            ("ceil", lambda: self.unary(ceil)),
            ("M+", self.mem_plus), ("MR", self.mem_read), ("MC", self.mem_clear),
            ("C", self.clear)
        ]

        r, c = 1, 0
        for text, cmd in buttons:
            tk.Button(self.root, text=text, width=8, command=cmd)\
                .grid(row=r, column=c)
            c += 1
            if c == 4:
                r += 1
                c = 0

    def binary(self, func):
        a = self.get()
        self.entry.delete(0, tk.END)

        def calc():
            b = float(self.entry.get())
            self.show(func(a, b))

        self.entry.bind("<Return>", lambda e: calc())

    def unary(self, func):
        self.show(func(self.get()))

    def mem_plus(self):
        m_plus(self.get())

    def mem_read(self):
        self.show(mr())

    def mem_clear(self):
        mc()

    def clear(self):
        self.entry.delete(0, tk.END)