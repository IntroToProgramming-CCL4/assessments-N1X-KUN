# Write a Python program to display the current date and time.
# below displays the current time and year, I had a bit trouble with the "str" and gotten help from my classmates :]

import datetime

time = datetime.datetime.now()
 
print ("The date of today is...")
print (time.strftime("%d /%m / %y"))
print ("It is currently...")
print (time.strftime("%H / %M / %S"))
