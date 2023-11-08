# Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country = 'the Philippines'):
    description = "\nThe " + city.title() + " is in " + country.title() + "." # added \n to let it look neater
    print(description)

describe_city('Bacolod City')
describe_city('Naruto City', 'the Japan')                                     # yes that is a city
describe_city('Iloilo City')

   