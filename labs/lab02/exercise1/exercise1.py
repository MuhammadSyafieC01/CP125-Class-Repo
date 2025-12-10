# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    # TODO: Implement this function
    # Calculate round trip cost and checks if within budget
    fuel = (one_way_km *2) / km_per_liter
    price = fuel * price_per_liter
    if budget >= price:
        return True
    else:
        return False


# Test your code here
print("Testing Road Trip Budgeter...")
print(is_budget_sufficient(100,1,1,100))
