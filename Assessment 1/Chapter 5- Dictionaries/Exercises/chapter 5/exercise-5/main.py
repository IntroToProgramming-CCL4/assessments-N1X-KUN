# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list and as you do, 
# print everything you know about each pet

pets = []                                             # had to make an empty list 

pet = {
    'animal': 'Cat',
    'name': 'Neko',
    'owner': 'Mika',
    'weight':'4.3kg',
    'eats': 'Wet Cat Foods',
}
pets.append(pet)                                     # needed to add "append" to enable addition to the dictionary

pet = {
    'animal': 'Dog',
    'name': 'Rawrf',
    'owner': 'Cole',
    'weight': '9.2kg',
    'eats': 'Offal',
}
pets.append(pet)

pet = {
    'animal': 'Fish',
    'name': 'Bloop',                                # goofy pet name
    'owner': 'Juliana',
    'weight': "0.5kg",
    'eats': 'Fish Foods',
}
pets.append(pet)

pet = {
    'animal': 'Parrot',
    'name': 'Prit',                                 # his house must be very noisy to have a parrot
    'owner': 'Angelo',
    'weight': '1.6kg',
    'eats': 'Seeds',
}
pets.append(pet)

for pet in pets:
    print("\nHeres what I know about " + pet['name'].title() + " the " + pet['animal'].title() + ":")
    for key, value in pet.items():                                                                       # took trial and error until concluding with "for key, value in"
        print("\t" + key + ": " + str(value))  