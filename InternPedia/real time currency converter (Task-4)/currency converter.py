import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        
        # Variables
        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.converted_amount_var = tk.StringVar()

        # UI Components
        amount_label = tk.Label(root, text="Amount:")
        amount_entry = tk.Entry(root, textvariable=self.amount_var, justify='right')
        
        from_currency_label = tk.Label(root, text="From Currency:")
        from_currency_combobox = ttk.Combobox(root, textvariable=self.from_currency_var)
        
        to_currency_label = tk.Label(root, text="To Currency:")
        to_currency_combobox = ttk.Combobox(root, textvariable=self.to_currency_var)
        
        convert_button = tk.Button(root, text="Convert", command=self.convert)
        
        converted_label = tk.Label(root, text="Converted Amount:")
        converted_amount_label = tk.Label(root, textvariable=self.converted_amount_var, font=('Helvetica', 14, 'bold'))

        # Grid layout
        amount_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
        amount_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        from_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        from_currency_combobox.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        to_currency_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        to_currency_combobox.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        converted_label.grid(row=4, column=0, padx=10, pady=10, sticky='e')
        converted_amount_label.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        # Initialize currencies
        self.currencies = self.fetch_currencies()
        self.from_currency_var.set(self.currencies[0])
        self.to_currency_var.set(self.currencies[1])

    def fetch_currencies(self):
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        currencies = list(data['rates'].keys())
        return currencies

    def convert(self):
        amount = self.amount_var.get()
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()

        if amount and from_currency and to_currency:
            conversion_rate = self.get_conversion_rate(from_currency, to_currency)
            converted_amount = amount * conversion_rate
            self.converted_amount_var.set(f"{converted_amount:.2f} {to_currency}")
        else:
            self.converted_amount_var.set("Invalid input")

    def get_conversion_rate(self, from_currency, to_currency):
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
        data = response.json()
        return data['rates'][to_currency]

if __name__ == "__main__":
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()
