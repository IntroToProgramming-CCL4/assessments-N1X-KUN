# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size = 'Large', message = 'I Love Python.'):                # minor changes but maily copy 'n paste
    print("\nI would like a " + size + " t-shirt,")
    print('That prints a message saying: ', ' " ' + message + ' " ')
    
make_shirt ()
make_shirt(size = 'Small')                           
make_shirt('Medium', 'Python is better than learning Javascript')          # in my opinion... 