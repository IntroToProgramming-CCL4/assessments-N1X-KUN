# A girl heads to a computer shop to buy some USB sticks: Budget = £50 / USB = £6

# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
# You will to use the arithmetic operators to complete this exercise.

print ('Girl said,"How many USB sticks can I buy?"')
print ('Seller said, "How much do you have?"')
print ('Girl said, "I have £50" ')
print ('----------------------------------------------')
Budget = 50
USB = 6

Purchased = Budget // USB
Change = Budget % USB

print ("\nThe girl can buy up to",Purchased,"USB sticks")
print ("\nLeaving the girl with",Change,'pounds left...')  # I wanted to result "2£" but gets "2 £" instead so I changed it to 'pounds'


# "I started it first with a conversation between the seller and the girl and ended it with the required information"