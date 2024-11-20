#!/usr/bin/env python3

# Initialize dictionary 
test_dict = {'gfg' : 6, 'is' : 4, 'for' : 2, 'CS' : 10} 
# printing original dictionary 
print("The original dictionary : ", test_dict) 
# Convert dictionary to list of tuples
items = list(test_dict.items())
print("items : ", items)
# Split the list of tuples in half
first_half = items[:len(items)//2]
print("first_half : ", first_half)
second_half = items[len(items)//2:]
# Create two separate dictionaries
first_half_dict = dict(first_half)
second_half_dict = dict(second_half)
# Printing result 
print("The first half of dictionary : ", first_half_dict) 
print("The second half of dictionary : ", second_half_dict)