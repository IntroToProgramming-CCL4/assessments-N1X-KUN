# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#  If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#  If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#  Write one version of this program that runs the if block and another that runs the else block.

intel = {
    "question": "Captain, There are 3 colored alien ship...",              
    "alien_color": ["-green", "-yellow", "-red"],                   #created a dictionary
    "green" : "green"                                               #main answer goal to get that 5 points
    
}

print(intel["question"])

import time                                                         #added time to make it look like a video game dialogue text 

time.sleep(1)

for alien_ship in intel["alien_color"]:                             #asked user to provide command
    print(alien_ship)
    
time.sleep(1)
    
target =(input("Which colored ship do we take down: "))

if target == intel["green"]:
    print ("Green Ship Terminated")
    print("[Congrats 5 points earned!]")
else:
    print ("Ship Terminated")                                       #answer for both yellow and red
    print("[Congrats 10 points earned!]")