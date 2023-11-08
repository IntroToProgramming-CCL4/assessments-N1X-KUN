# A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; if they are between 3 and 12, 
# the ticket is $10; and if they are over age 12, the ticket is $15. 
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket

print ("Box Seenima is offering discounts for the offical release of the Fnaf Movie!")
print ("~Kids under 3 watches for free!~")

prompt = "\nHow old are you?"
prompt += "\nEnter 'that is all' when you are finished: "              #similar to previews task

while True:
    age = input(prompt)
    if age == 'that is all':
        break
    age = int(age)

    if age < 3:                                                       #if,elif, ad else is added
        print("  Congrats you watch for free!")
    elif age < 13:
        print("  Your ticket cost only $10.")
    else:
        print("  Your ticket is $15.")