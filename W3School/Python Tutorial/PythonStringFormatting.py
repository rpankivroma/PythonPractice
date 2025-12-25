"""
Python String Formatting Task: Order Summary Generator

📌 Goal
Write a Python program that prints a formatted order summary for a customer using string formatting.

🧾 Given Data
customer_name = "Alice"
order_id = 4582
item = "Wireless Mouse"
quantity = 3
price_per_item = 19.99
discount = 10  # percent

📝 Tasks

Task 1 — Basic formatting
Use the .format() method to print:
Customer Alice placed order #4582.

Task 2 — Positional placeholders
Print the following using index-based placeholders:
Item: Wireless Mouse | Quantity: 3 | Price per item: $19.99

Task 3 — Named placeholders
Use named placeholders to print:
Subtotal: $59.97
(subtotal = quantity × price_per_item)

Task 4 — Number formatting
Format the subtotal so that it always shows 2 decimal places, even if they are zeros.

Task 5 — Percentage formatting
Print the discount like this:
Discount applied: 10%

Task 6 — Final total
Calculate the final price after discount and print:
Final total: $53.97
(Use string formatting, not string concatenation.)

Task 7 — Alignment
Print a neatly aligned receipt like this:

Customer:        Alice
Order ID:        4582
Item:            Wireless Mouse
Quantity:        3
Subtotal:        $59.97
Discount:        10%
Final total:     $53.97

(Hint: use width formatting)

🎯 Requirements
Use .format() (not f-strings)
Use positional and named placeholders
Use number formatting (:.2f)
No external libraries
"""

# Answer

customer_name = "Alice"
order_id = 4582
item = "Wireless Mouse"
quantity = 3
price_per_item = 19.99
discount = 10  # percent

# ----------------------- Task 1 — Basic formatting ---------------------------

text = "Customer Alice placed order #{}"
print(text.format(order_id))

# ------------------- Task 2 — Positional placeholders ------------------------

items = "Item: {0} | Quantity: {1} | Price per item: ${2}"
print(items.format(item, quantity, price_per_item))

# -------------------- Task 3 — Named placeholders ----------------------------

print(f"Subtotal: ${quantity * price_per_item}")

# -------------------- Task 4 — Number formatting -----------------------------

print(f"Subtotal: ${quantity * price_per_item:.2f}")

# ------------------- Task 5 — Percentage formatting --------------------------

print(f"Discount applied: {discount}%")

# ---------------------- Task 6 — Final total ---------------------------------

discount_txt = "Final total: ${:.2f}"
print(discount_txt.format(quantity * price_per_item - (discount * (quantity * price_per_item))/ 100))

# --------------------------- Task 7 — Alignment ------------------------------

Alignment = f"""
Customer:        {customer_name}
Order ID:        {order_id}
Item:            {item}
Quantity:        {quantity}
Subtotal:        ${quantity * price_per_item:.2f}
Discount:        {discount}%
Final total:     ${quantity * price_per_item - (discount * (quantity * price_per_item))/ 100:.2f}
"""

print(Alignment)

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe 
"c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/PythonStringFormatting.py"
Customer Alice placed order #4582
Item: Wireless Mouse | Quantity: 3 | Price per item: $19.99
Subtotal: $59.97
Subtotal: $59.97
Discount applied: 10%
Final total: $53.97

Customer:        Alice
Order ID:        4582
Item:            Wireless Mouse
Quantity:        3
Subtotal:        $59.97
Discount:        10%
Final total:     $53.97
"""