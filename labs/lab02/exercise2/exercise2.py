# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    tent = math.ceil ( participants / tent_capacity )
    price = (tent * tent_price) + (meal_price * participants)
    return price

# Test your code here
print("Testing Camping Logistics...")
