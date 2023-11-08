# Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

rivers = {
    'pasig river': 'philippines',                                                # just wrote 4 so that its shorter and quicker
    'ishikari River': 'japan', 
    'nile river': 'egypt',                                                       # was not sure IF it must be part of the river list
    'nakdong river': 'south korea',
    }

for river, country in rivers.items():
    print("The " + river.title() + " passes through " + country.title() + ".")   # confused at first then realize that ".items()" mut be added

print("\nRivers that were displayed in the dictionary:")
for river in rivers.keys():
    print("~ " + river.title())

print("\nCountries which the rivers can be discovered from:")
for country in rivers.values():
    print("~ " + country.title())