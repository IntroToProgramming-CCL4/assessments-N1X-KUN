# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. 
# You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.    

glossary = {
    'loop': 'repeatedly execute a code over and over as long as the conditions are met.',
    'comment': ' python does not execute whatever command that follows after # and is used to explain or make notes.',
    'list': 'stores multiple items in a single variable.',
    'variables': 'contains the data allowing the user to interact or store values in their code.',
    'dictionary': "stores information or data using key-value pairs.",
    }

word = 'variables'
print("\n" + word.title() + ": " + glossary[word])    # maily copy and paste with just changes on which ones I want to explain

word = 'comment'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'loop'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])