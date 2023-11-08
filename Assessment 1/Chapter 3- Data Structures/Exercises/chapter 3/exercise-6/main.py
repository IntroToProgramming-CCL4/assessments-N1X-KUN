# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# Start with your program from Exercise 3-5. 
# Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.    

# "Sir why put huge chunk of pharagraphs? Its so scary sir (;-;)" - Spiderman


guests = ['Yuichi Nakamura', 'Ronny Chieng', 'Soma Saito'] 

print ("\nInvited Guest List:", guests)
print ("\n")

for name in guests:                                                 # took inspiration from christian"s simple program but decided to stick with the long version
    print (name + ", please attend my dinner")                      # this sort of command simplifies it rather than typing the prgram individualy    

name = guests[2].title()
print("\nSorry, " + name + " will not be able to attend.")  

del(guests[2])
guests.insert(2, 'Minagawa Junko')                                  

name = guests[0].title()
print(name + ", please attend my dinner.")                         

name = guests[1].title()
print(name + ", please attend my dinner.")

name = guests[2].title()
print(name + ", please attend my dinner.") 

print("\nUnfortunately, we can only invite two people to the dinner.")            # embarrassed that I messed up my dinner plans

name = guests.pop()
print("Sorry, " + name.title() + " there is no available seat at the table.")    #new code and had slight problem because it was new

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

del(guests[0])                                                         #at first i did guest[0] then guest[1] but was wrong
del(guests[0])                                                         #and decided to play around till i got it right with [0]

print("\nUpdated Guest List:", guests)

