# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120
total_cost = price * count

# Write your code here
#Use membership oprator in and not in.
contains_raw = "raw" in description
contains_Imported = "Imported" in description

#type() function verify
price_is_float = type(price) == float
count_is_int = type(count) == int
description_is_str = type(description) == str


#Print statement
print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)
print("Is description a string?:", description_is_str)
print ("What is the total cost of full inventory?:", total_cost)