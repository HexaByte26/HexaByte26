import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # self.font_family = "JetBrains Mono"

        # self.title = tk.Label(self, text="Sign Up", font=(self.font_family, 25))
        # self.title.grid(columnspan=2, row=0, column=0)

        # self.email_entry = tk.Entry(self)
        # self.email_entry.grid(row=1, column=1, padx=10)

        # self.email_label = tk.Label(self, text="Email:", font=(self.font_family, 15))
        # self.email_label.grid(row=1, column=0)

        # self.password_entry = tk.Entry(self)
        # self.password_entry.grid(row=2, column=1, padx=10)

        # self.password_label = tk.Label(self, text="Password:", font=(self.font_family, 15))
        # self.password_label.grid(row=2, column=0)

        # self.sign_up_button = tk.Button(self, text="Sign Up", font=(self.font_family, 10), width=15)
        # self.sign_up_button.grid(columnspan=2, row=3, column=0)


class Frame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.font_family = "JetBrains Mono"

        self.title = tk.Label(self, text="Sign Up", font=(self.font_family, 20))
        self.title.grid(columnspan=2, row=0, column=0)

        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=1, column=1, padx=10)

        self.email_label = tk.Label(self, text="Email:", font=(self.font_family, 12))
        self.email_label.grid(row=1, column=0)

        self.password_entry = tk.Entry(self)
        self.password_entry.grid(row=2, column=1, padx=10)

        self.password_label = tk.Label(self, text="Password:", font=(self.font_family, 12))
        self.password_label.grid(row=2, column=0)

        self.sign_up_button = tk.Button(self, text="Sign Up", font=(self.font_family, 10), width=10)
        self.sign_up_button.grid(row=3, column=0, columnspan=2)

        self.pack(padx=5, pady=5)


app = App()
frame = Frame(app)
app.mainloop()