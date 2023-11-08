# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

prompt = "\nWhat pizza toppings would you like on your pizza?"
prompt += "\nAny more toppings dear customer or is it 'finito': "               # forgot "+=" is used to add a value to a variable

while True:
    topping = input(prompt)
    if topping != 'finito':                                        # "finito" is the italian for "finish" since pizza orginated in italy
        print( topping + " has been added to your pizza.")
    else:
        break 
print ("\nYour Pizza is being prepared dear customer...")
    
# Did not bother to add additional command to display every toppings of the pizza... its 2am :p 
