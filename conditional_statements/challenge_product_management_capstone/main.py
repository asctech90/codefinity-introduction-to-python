# Input variables
days_until_expiration = 5  # Example value
stock_level = 60           # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

if product_type == "Perishable":
    # Apply a 30% discount if there are 3 days or less until expiration and stock level is over 50
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
    # Apply a 20% discount if there are 4 to 6 days until expiration and stock level is over 50
    elif 4 <= days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied")
    # Apply a 10% discount if there are more than 6 days until expiration or stock level is 50 or less
    elif days_until_expiration > 6 or stock_level <= 50:
        print("10% discount applied")
else:
    print("No discount available for non-perishable items.")