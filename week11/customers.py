#customers.py
# Shawn Tran
#Lab 11 Customer Dictionary & Lookup

# Reflection1
# Use the .get() if something doesnt exit since
# it would give a default value instead of an error having
# and use brackets if it does exist and needs a value to put in
# Reflection 2
# The pattern reminds me of info being organized in excel
# and adding numbers together. Python is a lot better because
# like you said in class it can go throug stuff automatically and calculate
# as opposed to going through every cell so manually


print("-- Exercise 1 ---")
customer = {
    "name": "Alice", #key value
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("-- Exercise 2 ---")
customer['phone'] = '555-5555' # adding a new key value pair to the dictionary
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["name"]
print(customer)

print(customer.get("ytd_spend", 0))

print("-- Exercise 3 ---")
print(customer.get("email", "no email on file"))

#try:
 #   print(customer["email"])
#except KeyError as error:
#    print("Key error caught", error)

print("-- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

    print("-- Excerise 5 ---")
tier_disounts = {"bronze": 0, 
 "silver": 0.05,
 "gold": 0.10,
 "platinum": 0.15
 }

purchase = 200
discount_rate = tier_disounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier:{customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: {final_price:.2f}")

print("-- Excercise 6 ---")
customers = [
    {"name": "Bob","tier": "silver", "ytd_spend": 3200},
    {"name": "Carol","tier": "gold", "ytd_spend": 8750},
    {"name": "David","tier": "bronze", "ytd_spend": 450},
]

#--- Exercise 7: nested catalog ---
print ("-- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}
for name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {name} only {details['stock']} left")

print("--- Exercise 8 ---")

transactions = [
    {"region":"South", "amount": 300},
    {"region":"North", "amount": 150},
    {"region":"South", "amount": 200},
]

sales_by_region = {}

for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]:.2f}")