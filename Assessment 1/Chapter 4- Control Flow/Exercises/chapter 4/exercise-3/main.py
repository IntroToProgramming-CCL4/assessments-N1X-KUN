# Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed for the appropriate color alien.

intel = {
    "question": "Captain, There are 3 colored alien ship...",
    "alien_color": ["-green", "-yellow", "-red"],
    "green" : "green",                                           #HAD TROUBLE WITH THIS AND ANGELO SOLVED WITH THE CONCLUSION OF ME FORGETTING TO ADD "," AFTER GREEN
    "yellow": "yellow"                                           #added as another option answer... HAD TROUBLE ALOT OF TIME WITH THIS
    
}

print(intel["question"])

import time

time.sleep(1)

for alien_ship in intel["alien_color"]:
    print(alien_ship)
    
time.sleep(1)
    
target =(input("Which colored ship do we take down: "))

if target == intel["green"]:
    print ("Green Ship Terminated")
    print("[Congrats 5 points earned!]")
elif target == intel["yellow"]:                                 #elif addition
    print ("Yellow Ship Terminated")
    print ("[Congrats 10 points earned")
else:
    print ("Red Ship Terminated")
    print("[Congrats 15 points earned!]")