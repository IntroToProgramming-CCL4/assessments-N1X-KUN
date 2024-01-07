import random                                         #an inportant import as it handles the probabilities and picks characters to be obtained randomly
import time                                           #mainly used for an animation-like and making the program eye catching for the user experience
import os                                             #mainly used for the "clear_screen" feature where it wont stack the information in a single page
from collections import defaultdict                   #it is basically a counter that starts as 0 and adds +1 every time a similar rarity is obtained, used for my receipt

characters = {
    "Basic": ["Midoriya Izuku", "Maka Albarn", "Edward Elric", "Natsu Dragneel", "Alucard", "Ichigo Kurosaki", "Ash & Pikachu"], #7 characters
    "Rare": ["Pegasus Seiya", "Meliodas", "Tanjiro Kamado", "Gon Freecss", "Koro-sensei", "Rimuru Tempest", "Ken Kaneki"],       #7 characters
    "Epic": ["Naruto Uzumaki", "Spike Spiegel", "Giorno Giovanna", "Mob Kageyama", "Muzan Kibutsuji", "Anos Voldigoad"],         #6 characters
    "Legendary": ["Monkey D. Luffy", "Light Yagami", "Ainz Ooal Gown", "Chainsaw-Man", "Eren Yeager", "Son Goku"],               #6 characters
    "Special": ["Saitama", "Jotaro Kujo", "Satoru Gojo", "Yoriichi Tsugikuni", "Kusuo Saiki"]                                    #5 characters
} 
#created 5 classes and ranked them accordingly to my interest, the better the class the fewer the characters so that it would feel unique or hard to obtain

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  #used to clear the screen for a tidy display, cls is to wipe the current screen and nt & clear is there to tell if the computer is windows or not

def special_message_animation():
    print("\nAmongus... You are very sussy, Baka! ඞ")           #just a funny little joke for students because these are the jokes nowadays 
    time.sleep(1)
    print("Let's see what you get from the legendary roll...")
    time.sleep(2)                                                #longer display so it has the dramatic pause
    clear_screen()

def getuser_name():
    while True:
        print ()                                                 #this basically creates a space
        user_name = input("Please enter your name or type 'a' for (͠≖ ͜ʖ͠≖)👌 anonymous: ")
        if user_name.lower() == 'a' or user_name.isalpha():      #checks if the user typed letter a or an alphabet letter 
            return user_name.capitalize()
        else:
            print("Invalid input. (ง︡'-'︠)ง Please enter a valid name or 'a' for anonymous.")   #will only accept either the letter 'a' or any alphabetic letters

def get_user_occupation():
    while True:
        user_occupation = input("\nPlease enter your current occupation (working / unemployed / student): ").lower()  #converts any capital letters to its lowercase form
        if user_occupation in ['working', 'unemployed', 'student']:  #what the system expects to be entered 
            return user_occupation
        else:
            print("\nInvalid input. (ง︡'-'︠)ง Please enter 'working', 'unemployed', or 'student' only.")

def title_screen(user_name):
    clear_screen()
    print("*" + "*"*50 + "*")                                        #the profesional and shorter version... i learned this from sir so thanks!
    print("*  Welcome   to   the   Shonen    Gacha   Machine  *")
    print("****************************************************")    #the simpler but longer version... i kept both to demonstrate that there are two ways to do it
    print("\nCome try your luck and see if the Gods of Fortune are") #\n used for newline or basically a space
    print("on your side today. Roll for a chance to get your\nfavorite characters from your favorite anime series!\n")
    print("Go big and to get better characters!")
    print("Gambling addicts? Try our Random Rolls and obtain\nunique characters which you won't get in any other")
    print("categories...\n")
    if user_name == 'A':
        print("                 ▬▬ι═══════ﺤ Good luck, Dear Player~")    #print the default text if user types "a"
    else:
        print(f"                 ▬▬ι═══════ﺤ Good luck, {user_name}~")   #print whatever the user has entered as their name
    print("\n==========================")

def welcome_screen(occupation):     #(occupation) is being a function being defined and it alters the welcome screen according to the user selection
    print("Select your Rolls:")
    print(f"1. Basic Roll - {9 if occupation == 'student' else 10}Dhs")         #if student it changes the default payment to a new payment
    print(f"2. Rare Roll - {19 if occupation == 'student' else 20}Dhs")
    print(f"3. Epic Roll - {49 if occupation == 'student' else 50}Dhs")
    print(f"4. Legendary Roll - {69 if occupation == 'student' else 70}Dhs")
    if occupation != 'unemployed':                                              #this checks if the chosen occupation is not equal to "unemployed"
        print(f"5. Random Roll - {99 if occupation == 'student' else 100}Dhs")  #if its true then this will not be displayed but if its false then this will be shown
    print("==========================")

def get_user_choice(occupation):
    while True:                                                                   #initiate an infinite loop that will not stop until a valid answer is provided
        try:                                                                      #"try" is used to execute the program but if there is an error it jumps straight to "except"
            if occupation == 'unemployed':
                choice = int(input("\nSelect your roll (1-4): "))                 #will display this if user typed "unemployed"
            else:
                choice = int(input("\nSelect your roll (1-5): "))                 #will display this if user did not type "unemployed"
            if occupation == 'unemployed' and choice == 5:                        ##checks if the entered input is within 1-5 and if unemployed then makes sure 5 not an option
                print("Invalid choice. Please enter a number between 1 and 4.")
            elif 1 <= choice <= 5:                                                
                return choice                                                     #this checks if the choice is valid and ends the function
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:                                                        #value error is said to detect if the user inputs something that cannot be converted to an integer
            print("Invalid input. Please enter a number.")                        #in short: it the one that checks if the user did not perform the required task and asks again to do it

def calculate_probability(rarity, special_roll=False):
    probabilities = {                                    #chances to obtain characters: 
        "Basic": [80, 15, 4, 1],                         #80% basic, 15% rare, 4% epic, 1% legendary 
        "Rare": [15, 75, 9, 1],                          #15% basic, 80% rare, 9% epic, 1% legendary
        "Epic": [20, 35, 30, 15],                        #20% basic, 35% rare, 30% epic, 15% legendary
        "Legendary": [20, 20, 10, 50],                   #20% basic, 20% rare, 10% epic, 50% legendary
        "Special": [20, 20, 20, 20, 20]                  #20% basic, 20% rare, 20% epic, 20% legendary, 20% special
    }                                                    

    if special_roll:                    #"weights" are said to be numerical values that analyzes the chances of each elements from the rarity to be picked from
        return random.choices(["Basic", "Rare", "Epic", "Legendary", "Special"], weights=probabilities[rarity])[0] #takes only the first only item from the list 
    else:
        return random.choices(["Basic", "Rare", "Epic", "Legendary"], weights=probabilities[rarity])[0] #returns to this options of rarities to be chosen from without "Special"

def roll_gacha(cost, roll_type, wallet, total_money_inserted, characters_obtained, user_name):
    obtained_characters = []

    if cost == 69:                           #a condition that if the cost is equal to 69 Dhs then it prints a "special message"
        special_message_animation()

    print("Rolling the Shonen Gacha Pop...")

    for i in range(10):                      #commands to do it 10 times, basically 10 rolls per one purchase
        rarity_obtained = calculate_probability(roll_type, special_roll=(roll_type == "Special"))  #selcts a random rarity based on the probability
        character_list = characters[rarity_obtained]
        obtained_character = random.choice(character_list)                                         #puts the chosen rarity in the basket "obtained characters"
        obtained_characters.append((obtained_character, rarity_obtained))

    clear_screen()                           #for a clean and neat display
    print("Congratulations! You have obtained:")

    for character, rarity in obtained_characters:
        print(f"- {character}. Rarity: {rarity}")
        time.sleep(0.5)                      #prints each character individually with 0.5 delay 

    print("\nRemaining Money:", wallet - cost, "Dhs")                                                        #prints the remaining money after the 10 rolls
    return wallet - cost, total_money_inserted + cost, obtained_characters + characters_obtained, user_name 
       # ^this line shows: the remaining change in wallet, total money inserted into the machine, all of the obtained characters from the start to the end of the program, and the user's name

def roll_animation(roll_num, character, rarity, wallet):
    print(f"Rolling the Shonen Gacha Pop...")
    time.sleep(0.5)                                        #to give that "rolling moment" as the user awaits what character they obtain
    clear_screen()                                         #clears screen after finishes the 10 rolls
    print(f"Congratulations! You obtained {character}.")
    print(f"Rarity: {rarity}")
    if roll_num == 10:                                     #checks if it has rolled 10 times 
        print(f"Remaining Money: {wallet}Dhs")
    time.sleep(1)                                          #another animation-like 

def display_receipt(wallet, total_money_inserted, obtained_characters, roll_counts, user_name, occupation):
    def print_with_delay(text, delay=1):                   #this basically is used for additional of visual effects
        for char in text:                                  #scans each character and performs each command for each one          
            print(char, end='', flush=True)
            time.sleep(1)                                  #1 second delay for that neat interactions

    clear_screen()
    print("\nGacha Receipt:")                  
    print(f"Customer Name: {user_name}")                        #prints whatever the user has typed as their username
    print(f"Occupation: {occupation.capitalize()}")             #prints the user occupation in capitalization 
    print(f"Total Money Inserted: {total_money_inserted}Dhs")   #prints overall total money inserted into the machine
    print(f"Remaining Money: {wallet}Dhs")                      #prints the remaining change the user is left with
    print(f"Date: {time.strftime('%d-%m-%Y')}")                 #prints the current date - month - year 
    print(f"Time: {time.strftime('%H:%M:%S')}")                 #prints the current hour - minutes - seconds
    print(f"\nNumber of times user rolled: {len(roll_counts)}") #displays the total amount of times the user has rolled

    roll_types = {1: "Basic", 2: "Rare", 3: "Epic", 4: "Legendary", 5: "Special"} #this simply tells the system the numeric value for each rarity rolls

    for roll, count in sorted(roll_counts.items()):             #checks the roll type and number of times the user rolled for that particular rarity
        cost = {1: 9 if occupation == 'student' else 10, 2: 19 if occupation == 'student' else 20, 3: 49 if occupation == 'student' else 50, 4: 69 if occupation == 'student' else 70, 5: 99 if occupation == 'student' else 100}[roll]
        # ^this line changes the prices of the rarities rolls if the user inputed occupation is "student", it is my way of saying 'student-discount'
        roll_type = roll_types[roll]                            #checks what kind of numeric value represents a certain rarity                 
        print(f"{count}x {roll_type} - [{count * cost}Dhs]")    #prints how many times the user has rolled a particular rarity, what type of rarity it is and its cost for it

    print("\nCharacters obtained:")

    rarity_counts = defaultdict(int)                            #uses the "defaultdict" to play as the counter for each rarity and character obtained
    for character, rarity in obtained_characters:               
        rarity_counts[(character, rarity)] += 1                 #basically adds 1 into the counter everytime the same character and its rarity is obtained 

    rarity_order = ["Basic", "Rare", "Epic", "Legendary", "Special"]  #arranges in order from least popular to most popular-kind

    current_rarity = None                                        #this keeps track of the rarities being processed 

    for rarity in rarity_order:                                            #goes through each rarity in a specific order "rarity_order"        
        for (character, rarity_type), count in rarity_counts.items():      #goes through each item from the dictionary
            if rarity_type == rarity:                                      #
                if current_rarity != rarity:
                    if current_rarity is not None:
                        print()                                             #add a new line for the new rarity
                    current_rarity = rarity

                print(f"- Rarity: {rarity_type} {character}. ({count}x)")
                time.sleep(0.1)                                             #a slight delay for each character

    print("\nYour characters have been registered. Please claim them by the cashier corner...\n")   #I have added an ASCII ART in the receipt so it 
                                                                                                    #can have a bit appeal to the users eyes and
    print(" ⠐⣄⠀⠀⠀⠀⠈⠳⣽⣄⠀⠀⠀⠈⢢⠀⣫⣷⠂⠀⢳⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⣰⠃⠀⢀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢀⠀")     #not feel bore with the usual print receipt
    print("⠀⠈⠳⣄⠀⠀⠀⠀⠈⢮⣦⠀⢀⡠⠞⠋⣁⡼⢧⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠱⣆⠈⢧⡀⠀⠀⢀⠀⠀⠀⠀⠀⢀⠐⠁⠀")
    print("⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠹⣿⢋⣠⠴⠛⠁⠀⠈⢧⠀⠘⣇⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⡘⠀⢠⠏⠀⠀⠈⢳⡀⠙⣆⣰⠃⠀⠀⠀⠀⠠⠃⠀⠀⠀")
    print("⣄⠀⠀⢀⠀⠈⠳⣄⠀⠀⠀⠚⢻⡀⠀⠀⠀⠀⠀⢈⣷⣶⣿⣶⣿⣷⣶⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣅⣀⡞⠀⠀⠀⠀⠀⠙⢦⡜⢧⡀⠀⠀⠀⠊⠀⠀⠀⡠⠾")
    print("⠈⠓⢆⡀⠙⢦⡀⠈⠳⣄⠀⠀⠀⠙⢦⡀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣛⣿⣷⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣶⣦⡄⠀⣠⠞⠛⠀⠓⢀⠞⠀⠀⠀⢀⠘⠁⠀")
    print("⡄⠀⠀⠙⠦⣄⠙⠢⠀⠈⠳⣄⠀⠀⠈⠳⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣿⣿⣟⣽⣷⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣷⡴⠃⠀⠀⢀⡔⠃⠀⠀⢀⠀⠀⠀⠀⢀")
    print("⠉⠳⢦⡀⠀⠈⠳⢤⡈⠀⠀⠈⠳⣄⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣻⣾⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⡴⠉⠀⢀⣠⠄⠁⠀⠀⠠⡀⠀")
    print("⠀⠀⠀⠙⠳⢄⡀⠀⠙⠢⣀⠀⢀⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡴⠋⠀⢀⡠⠟⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⢤⣀⠀⠀⠀⠉⢲⣤⣤⣼⣶⣿⣿⣿⢟⣭⣾⣿⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣿⣿⣿⣿⣼⣿⣿⣿⣿⣄⢀⡴⠊⠀⢀⠄⠀⠀⠀⠀⠀⠀⣠")
    print("⠀⠀⠈⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣿⣿⣿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⡿⠃⠀⠸⣿⣿⣿⣏⣿⣿⣿⣿⣿⡆⠀⠀⠀⠁⠀⠀⠀⢀⡠⠖⠋⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⣿⣿⣿⣿⣿⣿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢡⣿⣿⡿⠋⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⢀⣀⠄⠊⠁⠀⠀⠀⠀")
    print("⠠⢄⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢿⣿⣿⣿⡿⠋⠀⢸⣿⠋⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣤⣤⣀⣀⡄⠀⠀⠀")
    print("⠀⠀⠀⠈⠀⠂⢀⣀⣴⣾⣿⣿⣿⣿⣿⢧⣿⣿⢟⣫⣿⣿⣿⣿⣿⡿⠋⢸⣿⣿⣟⣁⣀⠀⢟⣰⠀⠀⠀⣄⣄⣀⣤⠤⠴⣿⣿⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀")
    print("⠀⠀⠠⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣻⣵⣿⣿⣿⣿⣿⣿⠋⠀⠀⣾⡿⠁⠤⣬⡍⠛⢯⠟⠀⠀⠀⠈⠁⠠⠤⠄⠀⢸⣟⠀⢻⣿⣿⣿⣿⡟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠈⠉⠙⠛⠿⠿⠿⠿⠿⢿⣿⣥⣾⣿⣿⣟⣾⡿⣿⣿⣯⢠⡴⠶⠿⠿⢿⠿⠷⠦⠀⠀⠀⠀⠀⠀⠀⣴⡶⣿⣛⠛⠛⠻⠶⢸⣿⡟⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀ ⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⡀⠀⠀⣾⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣷⠀⠀⠀⣼⣯⣷⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀")
    print("⠤⠄⠀ ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⣿⣿⣿⣇⠀⠀⠻⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⡿⠟⠀⠀⠀⣿⣿⣧⡟⠛⠛⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀")
    print("⠒⠒⠒⠒⠒⠒⠰⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣾⣿⣿⣿⠿⣒⣶⡶⠿⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠯⠭⠏⢠⡇⠹⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⡿⠟⣿⠘⢾⣿⣿⡟⢿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣸⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠖⠛⠛⠋⠉⠀⠀⢈⣧⡀⠻⣿⡷⣄⠻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠚⢿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀ ⠀⠀⣶⣤⣠⠴⠆⠀⠀⢀⣴⣿⡿⣿⣶⣽⣃⣀⠁⠘⠇⠀⠀⠀⠀⠀⠀⠀⣠⠴⠒⠶⢄⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠙⠿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣀⡠⠤⠀⠒⠉⠁⠈⠻⣿⣿⣿⣿⣶⣶⣿⣿⣿⣳⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⢰⡿⠒⠆⠀⢹⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⠀⠀⠉⠓⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⢢⣄⣀⣀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣳⣿⡿⣟⡏⣼⣿⢧⡉⠳⢦⣀⠀⠀⠀⠀⠘⠗⠒⠒⠲⠾⠀⠀⠀⢀⣠⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁")
    print("⠀⣀⠠⠌⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣛⣫⣵⣾⣿⢹⣷⣿⠀⠙⠲⢤⣈⠙⠲⠤⣄⣀⣀⠀⠀⠀⣀⣠⠴⣾⣿⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠉⠀⠀⠀⠀⠀⠀⠈⠉⠛⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠈⣧⣄⡀⠀⠈⠉⠓⠒⠒⠭⠭⢽⠓⠛⠋⠁⢠⣿⣿⣿⣿⣿⣷⣶⣤⣤⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣹⠀⠀⠀⣿⣿⣿⣷⣶⣦⣤⣀⣀⠀⠀⢻⠀⠀⣴⣶⣿⠈⠻⢿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠓⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠐⡠⠾⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⠟⠁⠀⡟⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢸⠀⢸⣿⣿⣿⠀⠀⠱⣌⠻⢄⡠⡀⠀⠀⠀⠀⠀⠀⠙⠢⡀⠀⠀⠀⠀⠀⠀⠀")      #Im sure there must be another way to do this
    print("⠠⠒⠀⠄⠂⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⡟⠋⠀⠀⢠⠃⠀⠀⠀⠀⣿⣿⣿⡿⣿⣿⣿⣿⡇⠀⢸⠀⣸⡿⣻⣽⣧⠀⠀⠈⢆⠀⠛⣞⢦⡀⠀⢄⠀⠀⢀⡀⠈⠀⠀⠀⠀⠀⠀⠀")      #neatly but I felt lazy and wanted the code lines 
    print("⠐⠈⠀⠀⠀⠀⣰⣿⣿⣿⣿⢷⣿⣿⠏⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠈⢣⠀⠈⢳⡳⡄⠀⠳⢤⡀⢹⡀⡀⠀⠀⠀⠀⠀⠈")      #to be as long as possible so make it seem there
    print("⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣾⣿⠃⠀⠀⠀⡀⠀⠸⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠙⢻⣿⣿⣿⣿⣿⡆⠀⠀⠀⢷⠀⠀⢹⡈⢧⡀⠈⢳⡄⢳⡀⠀⠀⠀⠀⠀⠄")      #is alot of work... but really i do not know how
    print("⠀⠀⣰⣾⣿⣿⣿⣿⠟⠋⣽⣿⠃⠀⠀⠀⠐⠀⠀⣇⠂⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⢹⣿⣧⣄⢀⣼⣿⣿⡿⠿⠿⠿⡀⠀⠀⠈⣧⠀⠀⢻⡀⠳⣄⠀⢳⡀⢳⡀⠀⠀⠀⠀⠀")
    print("⠐⠛⠛⠉⣠⠞⠁⠀⠀⣿⡻⠃⠀ ⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣿⣿⣿⣿⡆⠐⠒⠒⣷⠀⠀⠠⠘⡆⠀⠀⢷⠀⠈⢦⡀⢳⠐⢧⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠘⠁⠀⠀⠀⣰⢿⠟⣆⡠⠀⠀⠀⢠⠟⠁⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡄⠀⠀⢳⣽⡄⠀⢈⢧⠀⠀⠱⣔⣄⠈⠳⡄⠀⠀⠀")      #it was also late already as i was working this
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣼⡷⠋⢀⡜⢳⡀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢆⠀⠀⢳⣷⠀⠘⢿⣆⠀⠀⠘⢮⣢⡀⠈⠀⠀⠀")
    print("⠀⠀⠀⠀⡀⣠⣺⠟⠁⣴⠋⠀⠀⠙⣶⠃⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⡜⡆⠀⠈⢫⠀⠀⠘⣿⡄⠀⠀⠈⠻⣕⠄⠀⠀⠀                  ")

    print("\nThanks for playing! Come test your luck again!")                                                                

def run():                                 #the main control loop of the entire program
    obtained_characters = []                              
    wallet = 0                             #make sure it starts with 0 first
    total_money_inserted = 0
    roll_counts = {}
    user_name = getuser_name()
    occupation = get_user_occupation()
    # ^mainly keeps tracks of user's choice

    while True:                               #basically infinite loop as it continues to execute until it has reached to an end or terminated task 
        title_screen(user_name)
        welcome_screen(occupation)
        print(f"Current Money: {wallet}Dhs")
        choice = get_user_choice(occupation)  #this entire part just displays the user's information of purchase 

        cost = {1: 9 if occupation == 'student' else 10, 2: 19 if occupation == 'student' else 20, 3: 49 if occupation == 'student' else 50, 4: 69 if occupation == 'student' else 70, 5: 99 if occupation == 'student' else 100}[choice]
        # ^this does the same and just verifies if the chosen occupation is "student" if it is it will ask for its discounted version not the original price
        
        while wallet < cost:                     #this is a loop to continue asking the user to enter money if it is less than the cost 
            remaining_amount = cost - wallet     #calculates the pending amount of money needed to be payed still
            try:
                inserted_amount = int(input(f"Insert money ({remaining_amount}Dhs or more): "))  #displays how much is missing 
                if inserted_amount < 0 or inserted_amount % 1 != 0:                              #checks if entered number is negative or decimals
                    print("Sorry, we do not accept negative inputs or decimal numbers. Please insert proper currency.") #prints error
                    continue                      #this basically just execute the task and move on, it does not loop back to the ^previous codes, 
                wallet += inserted_amount         #basically adds the current inserted money to the user's wallet 
            except ValueError:                    #identifies/checks if the user did not enter a whole number or a non-integer
                print("Sorry, we do not accept non-integer inputs. Please insert proper currency.") 
                continue                          #again just continues and does not go back 
            if wallet < cost:                     #checks if the wallet is still not enough to pay for the cost of a roll
                print(f"Insufficient funds. Please insert {cost - wallet}Dhs or more.")

        roll_counts.setdefault(choice, 0)         #acts as a counter and starts of 0 if the user has JUST chosen that roll
        roll_counts[choice] += 1                  #it then adds +1 for everytime the user rolls that same roll again, basically a counter

        wallet, total_money_inserted, obtained_characters, user_name = roll_gacha(cost, "Special" if choice == 5 else "Basic" if choice == 1 else "Rare" if choice == 2 else "Epic" if choice == 3 else "Legendary", wallet, total_money_inserted, obtained_characters, user_name)
          # ^basically updates on the new information being given, the characters recently obtained, the total money inserted so far, etc.
        
        while True:                              #infinite loop basically untill the task is executed
            roll_again = input("\nWould you like to insert more money to roll again? (y/n): ").lower()
            if roll_again == 'n':                #a condition if the user has decided NOT to roll again
                display_receipt(wallet, total_money_inserted, obtained_characters, roll_counts, user_name, occupation) #prints the full receipt
                return
            elif roll_again == 'y':              #a condition if the user has decided to roll again
                title_screen(user_name)
                welcome_screen(occupation)       #displays the same... meaning the menu and and welcome page again
                print(f"Current Money: {wallet}Dhs")  
                choice = get_user_choice(occupation)
                cost = {1: 9 if occupation == 'student' else 10, 2: 19 if occupation == 'student' else 20, 3: 49 if occupation == 'student' else 50, 4: 69 if occupation == 'student' else 70, 5: 99 if occupation == 'student' else 100}[choice]
                while wallet < cost:
                    remaining_amount = cost - wallet  #checks if there is enough money in the wallet to cover the required payment/cost 
                    try:                              #does the same thing, if there an issue it skip straight to "except"                                                           
                        inserted_amount = int(input(f"Insert money ({remaining_amount}Dhs or more): "))   
                        if inserted_amount < 0 or inserted_amount % 1 != 0:                                   #same explanation about checking non-integer
                            print("Sorry, we do not accept negative inputs or decimal numbers. Please insert proper currency.")
                            continue
                        wallet += inserted_amount
                    except ValueError:                 #identifies/checks if the user did not enter a whole number or a non-integer
                        print("Sorry, we do not accept non-integer inputs. Please insert proper currency.")
                        continue                       #skips the rest of it and starts over again if there are errors
                    if wallet < cost:
                        print(f"Insufficient funds. Please insert {cost - wallet}Dhs or more.")
                roll_counts.setdefault(choice, 0)
                roll_counts[choice] += 1
                wallet, total_money_inserted, obtained_characters, user_name = roll_gacha(cost, "Special" if choice == 5 else "Basic" if choice == 1 else "Rare" if choice == 2 else "Epic" if choice == 3 else "Legendary", wallet, total_money_inserted, obtained_characters, user_name)
        # ^this is just basically repeated, its to create that determination for the user to test their luck, just like everyone's everyday gacha addiction
        # i implemented 3 occupations here with a reason for the changes: student naturally asks for student student discount and i applied 1dhs off because its funny :p      
        # working is normal gacha machine, has normal price and all the options and unemployed does not have "Random Rolls" because its the most expensive roll and since they don't have work, they should'nt spend alott

run()  
