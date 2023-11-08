#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
#You’ll have to think of someone else to invite.
# •Start with your program from Exercise 3-4. 
# Add a print() call at the end of your program stating the name of the guest who can’t make it.
# •Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# •Print a second set of invitation messages, one for each person who is still in your list.


guests = ['Yuichi Nakamura', 'Ronny Chieng', 'Soma Saito']  

name = guests[0].title()
print(name + ", please attend my dinner.")

name = guests[1].title()
print(name + ", please attend my dinner.")

name = guests[2].title()
print(name + ", please attend my dinner.")                          #Same Programs...

name = guests[2].title()
print("\nSorry, " + name + " will not be able to attend.")  

del(guests[2])
guests.insert(2, 'Minagawa Junko')                                  #Since Chongyun VA won't be joining I called out Xingqiu VA

name = guests[0].title()
print(name + ", please attend my dinner.")                          #Then its copy passte again

name = guests[1].title()
print(name + ", please attend my dinner.")

name = guests[2].title()
print(name + ", please attend my dinner.") 

