import tkinter as tk

LABEL_COLOR = "#25265E"
LIGHT_GRAY = "#F5F5F5"
SMALL_FONT = ("Century Gothic", 16)
LARGE_FONT = ("Century Gothic", 35, "bold")
WHITE = "#FFFFFF"
DIGIT_FONT = ("Century Gothic", 25, "bold")
OFF_WHITE ="#F8FEFF"
DEFAULT_FONT = ("Arial", 20, "bold")

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x660")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.current_expression = ""
        self.total_expression = ""
        self.display_frame = self.create_display_frame()
        self.currrent_label, self.total_label = self.create_display_label()

        self.digits = {
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            0: (4,1), ".": (4,2)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "+": "+", "-": "-"}
        self.buttons_frame = self.create_buttons_frame()

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

# ------------------------------------DISPLAY FRAME-----------------------------------------

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=220, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_label(self):
        current_label = tk.Label(self.display_frame, text=self.total_expression, bg=LIGHT_GRAY,
                                 fg=LABEL_COLOR, font=SMALL_FONT, padx=20, anchor=tk.E)
        current_label.pack(expand=True, fill="both")

        total_label = tk.Label(self.display_frame, text=self.current_expression, bg=LIGHT_GRAY,
                                 fg=LABEL_COLOR, font=LARGE_FONT, padx=20, anchor=tk.E)
        total_label.pack(expand=True, fill="both")

        return current_label, total_label
    
    def update_current_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f'{symbol}')
        self.currrent_label.configure(text= expression)
        
    def update_total_label(self):
        self.total_label.configure(text=self.current_expression[:11])
    
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_total_label()
    
# -------------------------------------BUTTONS FRAME----------------------------------------

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digits, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digits), bg = WHITE,
                               fg= LABEL_COLOR, borderwidth=0, font=DIGIT_FONT, command=lambda x=digits: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_current_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg= OFF_WHITE,
                               fg="light blue", font=DEFAULT_FONT, borderwidth=0,
                               command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1 

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg= OFF_WHITE,
                               fg="red", font=DEFAULT_FONT, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_total_label()
        self.update_current_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg= OFF_WHITE,
                               fg="green", font=DEFAULT_FONT, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_current_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_total_label()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_squareroot_button()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, 
                                fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_total_label()

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_total_label()

    def create_squareroot_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, 
                                fg=LABEL_COLOR, font=DEFAULT_FONT, borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

# ----------------------------------------CODE RUNNER-----------------------------------------

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()