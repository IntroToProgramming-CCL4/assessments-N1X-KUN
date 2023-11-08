# Write a Python program which accepts the radius of a circle from the user and compute the area.

# "Knowing that pi is equal to 3.14" --> pi = 3.1415 
# "Therefore to calculate the area of the circle the formula must be" --> area = pi * (radius ^ 2) 


from math import pi

radius = float(input("Enter the Radius of the Circle: "))
area = pi * (radius ** 2)

print ("The area of the circle is: %.2f" % area)