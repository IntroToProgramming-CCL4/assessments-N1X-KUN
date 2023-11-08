# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['pastrami','Spicy Italian','pastrami', 'Subway Melt', 'Tuna', 'Subway Club','Steak and Cheese','pastrami']  
finished_sandwiches = []

print("Our appologies dear customer...Our Pastrami are out of stock today.")   # no more budget for these 
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')                         # ".remove" the occurance of the name "pastrami" from the list
print("\n")

while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()                                               
    print("The " + preparing_sandwich + " sandwich is being prepared...")
    finished_sandwiches.append(preparing_sandwich)
    
print ("\n***************************************")                                           
print ("\nNOW SERVING:")

for sandwich in finished_sandwiches:
    print("Order for " + sandwich + " sandwich is ready...")  # just copy paste... 