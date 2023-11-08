# Now that you know how to loop through a dictionary, 
# clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. 
# When you’re sure that your loop works, add five more Python terms
# to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    'loop': 'repeatedly execute a code over and over as long as the conditions are met.',
    'comment': ' python does not execute whatever command that follows after # and is used to explain or make notes.',
    'list': 'stores multiple items in a single variable.',
    'variables': 'contains the data allowing the user to interact or store values in their code.',
    'dictionary': 'stores information or data using key-value pairs.',
    'string': 'used for storing and manipulating either sequence letters or numbers ',
    'operators': 'they are symbols that execute commands applied on variables, (==) or (+) are some examples',
    'integer': 'represents a whole number without any decimal points',
    'print': 'used to display either text or values on the screen and is seen at the end of every python code',
    'float': 'used to represent numbers with decimal points or even fractions',
    }
    
for term, definition in glossary.items():
    print("\n" + term.title() + ": " + definition)
    
# only issue here is i always keep forgetting to add "," in a dictionary task