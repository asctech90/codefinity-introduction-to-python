# Define individual grocery items as lists containing details

meat = ["Ham", 3.99, 50, "Sliced"] #Item name, price, quantity, type
cheese = ["Cheddar", 5.49, 100, "Sharp"] #Item name, price, quantity, type
condiment = ["Mustard", 1.99, 75, "Spicy"] #Item name, price, quantity, type

# Create the main grocery list that contains these items.
deli_dept = [meat, cheese, condiment]

#Update the stock quantity and restock item by adding if condition. 
if meat[0] == "Ham" and meat[2] < 100:
    meat[2] = 100

#Add new seasonal meat list.

seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
deli_dept.remove(condiment)
deli_dept.sort()

print ("Initial Deli List:", deli_dept)
print ("Updated Deli List:", deli_dept)