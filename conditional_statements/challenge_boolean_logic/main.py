seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# Step 1: Overstock risk if seasonal AND stock exceeds threshold
overstock_risk = seasonal and current_stock > high_stock_threshold

# Step 2: Discount eligibility if not selling well AND not already on sale
discount_eligible = not selling_well and not on_sale

#Step 3: Decide to make a discount if either condition holds
make_discount = overstock_risk or disscount_eligible

# Step 4: Output the result
print ("Should the item be discounted?", make_discount)