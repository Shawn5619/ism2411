
# self assessment
# 1 My first bug was that the total got replaced
#every sale instead of adding it together and was fixed by
#changing total = sale to total = total + sale
# 2 applydiscount takes a price and a tier it checks
# the tier and returns the price after the discount and yes I think a classmate can
# easily understand what the function does if they have been tapped in
# 3 Fo AI I used gemini to help me interpret the code and find the bugs. I also used gemini
#  to help me understand the code and find the bugs. I used it to help me understand 
# the code and find the bugs but also fixing my own errors , I think Ai helped me a lot with 
#finding a place to get started while also fixing errors in my code
#Excerise 1

def calculate_tax(price, rate):
    tax = price * rate
    return tax
print("Tax on $100 at 7%: ${:.2f}".format(calculate_tax(100, 0.07)))
print("Tax on $250 at 8%: ${:.2f}".format(calculate_tax(250, 0.08)))

#Excerise 2

def apply_discount(price, tier):
    if tier == "gold":
        price = price * 0.85
    elif tier == "silver":
        price = price * 0.90
    elif tier == "bronze":
        price = price * 0.95

    return price
print("gold:   ${:.2f}".format(apply_discount(200, "gold")))
print("silver: ${:.2f}".format(apply_discount(200, "silver")))
print("bronze: ${:.2f}".format(apply_discount(200, "bronze")))
print("none:   ${:.2f}".format(apply_discount(200, "none")))

#Excerise 3

price = apply_discount(200, "gold")
print("After gold discount: ${:.2f}".format(price))
tax = calculate_tax(price, 0.07)
price = price + tax
print("After tax: ${:.2f}".format(price))

def final_price(price, tier, tax_rate):
    price = apply_discount(price, tier)
    tax = calculate_tax(price, tax_rate)
    price = price + tax
    return price
print("final_price(200, \"gold\", 0.07) = ${:.2f}".format(
    final_price(200, "gold", 0.07)
))

#excerise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print("Price: ${} | Tier: {} | Final: ${:.2f}".format(
        price, tier, total
    ))

#excerise 5

# b1= sale was replacing the total each time.
# I changed it to total = total + sale so it adds the sales together

#sales = [120, 80, 250, 175, 90]
#total = 0
#for sale in sales:
# total = total + sale
#print(f"Total: ${total}")

#B2 The for loop was missing a colon
# I added a colon after for sale in sales

#count = 0
#for sale in sales:
#  # count += 1
#print(f"Count: {count}")


# B3 The while loop was going one index too far
# I changed <= to < so it stops before reaching an invalid index

#i = 0
#while i < len(sales):
#    print(sales[i])
#  i += 1

#excerise 6

x = 100  # global var
def double_it():
    x = 999  # local var
    return x * 2

# The x inside the function is separate from the global x
print(x)
print(double_it())
print(x)