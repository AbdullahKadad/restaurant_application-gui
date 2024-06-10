import tkinter as tk
from tkinter import messagebox
# this is for commit 

# Function to display the order summary and calculate total price
def show_order_summary():
    pizza_qty = int(pizza_qty_var.get())
    pizza_size = pizza_size_var.get()
    burger_qty = int(burger_qty_var.get())
    burger_size = burger_size_var.get()
    soft_drinks_qty = int(soft_drinks_qty_var.get())
    order_type = order_type_var.get()
    extra_cheese = "Yes" if extra_cheese_var.get() else "No"
    extra_ketchup = "Yes" if extra_ketchup_var.get() else "No"

    # Pricing logic
    prices = {
        "Pizza": {"Small": 5, "Medium": 7, "Large": 10},
        "Burger": {"Classic": 5, "Big": 7},
        "Soft Drink": 2,
        "Extra Cheese": 1,
        "Extra Ketchup": 1
    }

    pizza_price = pizza_qty * prices["Pizza"][pizza_size]
    burger_price = burger_qty * prices["Burger"][burger_size]
    soft_drinks_price = soft_drinks_qty * prices["Soft Drink"]
    extra_cheese_price = extra_cheese_var.get() * prices["Extra Cheese"]
    extra_ketchup_price = extra_ketchup_var.get() * prices["Extra Ketchup"]

    total_price = pizza_price + burger_price + soft_drinks_price + extra_cheese_price + extra_ketchup_price

    summary = (
        f"Order Summary:\n"
        f"Pizza - Quantity: {pizza_qty}, Size: {pizza_size}\n"
        f"Burger - Quantity: {burger_qty}, Size: {burger_size}\n"
        f"Soft Drinks - Quantity: {soft_drinks_qty}\n"
        f"Order Type: {order_type}\n"
        f"Extra Cheese: {extra_cheese}\n"
        f"Extra Ketchup: {extra_ketchup}\n\n"
        f"Total Price: ${total_price}"
    )

    messagebox.showinfo("Order Summary", summary)

# Validation function to allow only numeric input
def validate_numeric_input(value_if_allowed):
    if value_if_allowed.isdigit() or value_if_allowed == "":
        return True
    else:
        return False

# Create the main window
root = tk.Tk()
root.title("Restaurant Menu")

# Variables to store user inputs
pizza_qty_var = tk.StringVar(value="1")
pizza_size_var = tk.StringVar(value="Small")
burger_qty_var = tk.StringVar(value="1")
burger_size_var = tk.StringVar(value="Classic")
soft_drinks_qty_var = tk.StringVar(value="1")
order_type_var = tk.StringVar(value="Takeaway")
extra_cheese_var = tk.BooleanVar()
extra_ketchup_var = tk.BooleanVar()

# Create a validation command for numeric input
vcmd = (root.register(validate_numeric_input), '%P')

# Create and place the form entries
tk.Label(root, text="Pizza Quantity:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=pizza_qty_var, validate="key", validatecommand=vcmd).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Pizza Size:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.OptionMenu(root, pizza_size_var, "Small", "Medium", "Large").grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Burger Quantity:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=burger_qty_var, validate="key", validatecommand=vcmd).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Burger Size:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
tk.OptionMenu(root, burger_size_var, "Classic", "Big").grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Soft Drinks Quantity:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=soft_drinks_qty_var, validate="key", validatecommand=vcmd).grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Order Type:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Takeaway", variable=order_type_var, value="Takeaway").grid(row=6, column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Dine in", variable=order_type_var, value="Dine in").grid(row=6, column=2, padx=10, pady=5, sticky="w")

tk.Label(root, text="Extras:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Extra Cheese", variable=extra_cheese_var).grid(row=7, column=1, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Extra Ketchup", variable=extra_ketchup_var).grid(row=7, column=2, padx=10, pady=5, sticky="w")

# Order Summary button
tk.Button(root, text="Order Summary", command=show_order_summary).grid(row=8, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
