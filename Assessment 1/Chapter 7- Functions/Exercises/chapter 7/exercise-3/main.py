# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print("\nI would like a " + size + " t-shirt,")
    print('That prints a message saying: ', ' " ' + message + ' " ')

make_shirt('Small sized', '[Valorant > Grass]')                            # realized that since i said (size,message) that means
make_shirt(message="Demon Slayer is MID!", size='Medium sized')            # the first text should be the size of the tshirt not 
                                                                           # the message, If i kept the message first then size it
                                                                           # will ruin the result