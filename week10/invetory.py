#Lab 10 - Lists and Tuples
#Shawn Tran - Markum Reed

#Reflections
#1, I found out that lists can be changed even after you make them
# you can add and remove and sort stuff without making a whole new list
#
#2, At my job a python lists can help keep track on sales and invetory at my churro work
#.This would make it easier then doing everything by hand manually
#
# Excerise 1

inventory = ["pen","notebook", "stapler","tape","marker"]

print(inventory)
print(len(inventory))

# Excerise 2

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Excerise 3

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#Excerise 4

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Excerise 5

coordinates = (40.7128, -74.0060)

try:
    coordinates[0] = 99
except TypeError:
    print("Tuples cannot be changed, they are useful for coordinates")

print(coordinates)

#Excerie 6

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total/count

print("Total:",total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:",min(sales))

#Excerise 7
prices = [9.99,14.99,4.99,24.99,1.99]

discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original:", prices)
print("Discounted:", discounted)

#Excerise 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)
    print("High Sales:", high_sales)
    print("Count:",len(high_sales))
    print("Average:",round(sum(high_sales) / len(high_sales), 2))