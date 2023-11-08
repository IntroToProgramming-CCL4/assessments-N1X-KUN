# Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['Spicy Italian', 'Subway Melt', 'Tuna', 'Subway Club','Steak and Cheese']   # subway menus
finished_sandwiches = []

while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()                                               
    print("The " + preparing_sandwich + " sandwich is being prepared...")
    finished_sandwiches.append(preparing_sandwich)
    
print ("\n***************************************")                                            # made it look like a waiting list
print ("\nNOW SERVING:")

for sandwich in finished_sandwiches:
    print("Order for " + sandwich + " sandwich is ready...")