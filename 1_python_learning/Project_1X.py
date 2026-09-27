import time # imports time
import keyboard #imports keyboard so we can detect keystrokes

#----------------------------------
# CHARACTER SETUP STUFF
#----------------------------------
name = input("Enter a name for your character: ") #asks user to input whatever they want to call the character
health = 100 #sets player health to be at 100 at the start
damage = 5 #how much damage the player takes (for the suffocation/drowning)
alive = True #keeps track of whether the player is alive
inventory = {} #inventory (starts empty)
inventory_space = 10 #maximum number of items the player can carry

# Keeps track of which direction the player originally chose.
# This prevents them from taking the same path twice.
first_direction = "" #keeps track of which direction the player originally chose so they don't take the same path twice

#----------------------------------
#FUNCTIONS FOR INPUT STUFF
#----------------------------------
def bahhh(prompt, valid_choices):
    while True: #makes it loop until the user inputs something valid that works

        choice = input(prompt).strip().lower() #takes the input and removes spaces and converts to lowercase 

        if choice in valid_choices: #checks if the input is valid
            return choice # if valid, sends the answer back

        print("Please enter a valid input.") #runs if the input is not valid

def yes_or_no(prompt):

    return bahhh(
        prompt + " (yes/no): ",
        ["yes", "no"]
    ) #this makes sure the player can only answer yes or no

#----------------------------------
#INVENTORY STUFF
#----------------------------------
def pick_up(item):
    global inventory_space
    if inventory_space > 0: #checks to make sure the player has enough inventory space
        if item in inventory: # Checks whether the item is already in the inventory.
            inventory[item] += 1 # Adds one to the number of that item.
        else:
            inventory[item] = 1  # Adds the new item to the inventory dictionary.
        inventory_space -= 1 # Removes one available inventory space.
        print("You picked up the", item + ".") # Tells the player that the item was successfully picked up.
        print("Inventory space remaining:", inventory_space) # Shows the player how much space they have left.

        return True # Returns True so the rest of the program knows that the item was successfully picked up.
    else:
        print(
            "Your inventory is full. "
            "You cannot pick up the " + item + "."
        ) # Runs when the player has no inventory space left.
        return False # Returns False because the item was not picked up.

def show_inventory():
    if len(inventory) == 0: # Checks whether the inventory contains zero items.
        print("\nYour inventory is empty.") # Tells the player that they have nothing.
    else:
        print("\n--- INVENTORY ---")
        for item in inventory: # Goes through every item currently in the inventory.
            print(item + ":", inventory[item]) # Prints the item name and how many the player has.
    print("Inventory space remaining:", inventory_space, "/ 10") # Shows how many inventory spaces remain.

def use_inventory_item():
    show_inventory() # Displays the player's inventory before they choose an item.
    if len(inventory) == 0: # Checks whether the inventory is empty.
        print("There is nothing to use.") # Tells the player that there is nothing to use.
        return "" #return nothing
    while True: # Keeps asking until the player enters a valid item.
        item = input(
            "\nEnter the item you want to use: "
        ).strip().lower() # Asks the player which item they want to use.
        if item in inventory: # Checks whether the item exists in the inventory dictionary.
            return item # Returns the valid item.
        print("Please enter a valid input.") # Runs if the player entered an item they do not own.
#----------------------------------
#SUFFOCATION
#----------------------------------

def suffocation(current_health, damage_amount, player_name):
    current_health -= damage_amount #removes damage from health
    if current_health < 0:
        current_health = 0 #prevents negative health
    print("\nYou are suffocating!") #tells player they are suffocating
    print(player_name + " takes", damage_amount, "damage.") #Tells player how much damage they took
    print(
        player_name +
        "'s current health is:",
        current_health
    ) #prints health after taking damage
    if current_health <= 0: #checks if the health has reached zero
        alive = False #tells game that player dead
        print("\n" + player_name + " is dead.") #tells user player is dead
    else:
        alive = True #they still livin
    return current_health, alive #updates health

#----------------------------------
#WATER ESCAPE THINGIE
#----------------------------------
def escape_water():
    print("\nYou dive underwater!") #tells player they in water
    print("SPAM E TO RESURFACE!") #tells how to escape
    required_presses = 10 #needs ten presses
    presses = 0
    time_limit = 5 #time-limit
    start_time = time.time() #records starting time
    while presses < required_presses: #checks for presses until ten
        elapsed_time = time.time() - start_time #checks time passed
        if elapsed_time >= time_limit: #stops after 5 seconds
            break
        if keyboard.is_pressed("e"): #checks if E is being pressed
            presses += 1 #adds to num of E
            print(
                "E presses:",
                presses,
                "/",
                required_presses
            ) #displays presses
            time.sleep(0.1) #waits briefly
            while keyboard.is_pressed("e"):
                time.sleep(0.01)
        time.sleep(0.01)
    if presses >= required_presses:
        print("\nYou managed to reach the surface!")
        return True
    else:
        print("\nYou were too slow!")
        return False

#----------------------------------
#FIRST AREA
#----------------------------------
def starting_cave():
    global first_direction
    print("\nYou wake up inside a small section of a cave.")
    print("Your head hurts, and you have no idea how you got here.")
    print("\nThere are two paths leading away from the cave.")
    if first_direction == "":
        print("\n1. Take the left path")
        print("2. Take the right path")
        print("3. Check inventory")
        choice = bahhh(
            "\nWhat do you do? ",
            ["1", "2", "3"]
        )
        if choice == "3":
            show_inventory()
            starting_cave()
            return
        elif choice == "1":
            first_direction = "left"
            flooded_tunnel()
        elif choice == "2":
            first_direction = "right"
            locked_door_cave()
    else:
        print("\nYou recognize this place.")
        if first_direction == "left":
            print("You have already explored the left path.")
            print("The only unexplored path is the right path.")
            print("\n1. Take the right path")
            print("2. Check inventory")
            choice = bahhh(
                "\nWhat do you do? ",
                ["1", "2"]
            )
            if choice == "2":
                show_inventory()
                starting_cave()
                return
            locked_door_cave()
        else:
            print("You have already explored the right path.")
            print("The only unexplored path is the left path.")
            print("\n1. Take the left path")
            print("2. Check inventory")
            choice = bahhh(
                "\nWhat do you do? ",
                ["1", "2"]
            )
            if choice == "2":
                show_inventory()
                starting_cave()
                return
            flooded_tunnel()

#----------------------------------
#FLOODED TUNNEL
#----------------------------------
def flooded_tunnel():
    global health
    global alive
    print("\nYou enter a narrow tunnel.")
    print("Water covers the floor of the cave.")
    print("The water is dark enough that you cannot see the bottom.")
    print("\n1. Search underwater")
    print("2. Swim on the surface")
    print("3. Leave the room")
    print("4. Check inventory")
    choice = bahhh(
        "\nWhat do you do? ",
        ["1", "2", "3", "4"]
    )
#----------------------------------
#SEARCHING WATER THING
#----------------------------------
    if choice == "1":
        print("\nYou take a deep breath and dive underwater.")
        print("Your hands search through the muddy bottom.")
        print("Something hard touches your fingers.")
        print("You pull out an old key.")
        pickup_choice = yes_or_no(
            "Do you want to pick up the key?"
        )
        if pickup_choice == "yes":
            pick_up("key")
        else:
            print("You leave the key where you found it.")
        print(
            "\nYou suddenly realize how long "
            "you have been underwater."
        )
        escaped = escape_water()
        if escaped:
            print("\nYou are almost at the surface!")
            for i in range(2):
                if not alive:
                    break
                health, alive = suffocation(
                    health,
                    damage,
                    name
                )
                time.sleep(0.5)
        else:
            while alive:
                health, alive = suffocation(
                    health,
                    damage,
                    name
                )
                time.sleep(0.5)
        if not alive:
            return
        print("\nYou gasp for air and grab the edge of the tunnel.")
#----------------------------------
#SWIMMING
#----------------------------------
    elif choice == "2":
        print(
            "\nYou stay above the water "
            "and carefully swim across."
        )
        print("You manage to keep your head above the surface.")
        print("You reach the other side safely.")

#----------------------------------
#LEAVE
#----------------------------------
    elif choice == "3":
        print("\nYou decide not to risk the water.")
        print("You return to the previous cave.")
        starting_cave()
        return
#----------------------------------
#INVENT CHECK
#----------------------------------
    elif choice == "4":
        show_inventory()
        flooded_tunnel()
        return
#----------------------------------
#AFTER LEAVE WATER
#----------------------------------
    print("\nYou are safely out of immediate danger.")
    print("\n1. Start swimming")
    print("2. Leave the room")
    print("3. Check inventory")
    choice = bahhh(
        "\nWhat do you do? ",
        ["1", "2", "3"]
    )
    if choice == "1":
        print(
            "\nYou start to swim across the "
            "flooded tunnel."
        )
        print("The tunnel becomes deeper and darker.")
        print("Eventually, your feet touch solid ground.")
        skeleton_chamber()
    elif choice == "2":
        print("\nYou decide to leave the flooded tunnel.")
        starting_cave()
    elif choice == "3":
        show_inventory()
        flooded_tunnel_after_crossing()
#----------------------------------
#AFTER SWIMMING FOR BIT
#----------------------------------
def flooded_tunnel_after_crossing():
    print("\nYou are still in the flooded tunnel.")
    print("\n1. Swim across the rest of the tunnel")
    print("2. Leave the room")
    print("3. Check inventory")
    choice = bahhh(
        "\nWhat do you do? ",
        ["1", "2", "3"]
    )
    if choice == "1":
        print("\nYou swim across the flooded tunnel.")
        print("You safely reach the other side.")
        skeleton_chamber()
    elif choice == "2":
        print("\nYou leave the flooded tunnel.")
        starting_cave()
    else:
        show_inventory()
        flooded_tunnel_after_crossing()
#----------------------------------
# SKELETON CHAMBER
#----------------------------------
def skeleton_chamber():
    print("\nYou enter a massive chamber.")
    print("The ceiling disappears into darkness above you.")
    print("Near the center of the chamber is a dead skeleton.")
    print("The skeleton is holding an old book.")
    print("\n1. Pick up the book")
    print("2. Explore the rest of the room")
    print("3. Check inventory")
    choice = bahhh(
        "\nWhat do you do? ",
        ["1", "2", "3"]
    )
    if choice == "1":
        pickup_choice = yes_or_no(
            "Do you want to pick up the book?"
        )
        if pickup_choice == "yes":
            pick_up("book")
        else:
            print(
                "You leave the book in the skeleton's hands."
            )
        print("\n1. Explore the rest of the room")
        print("2. Leave the room")
        print("3. Check inventory")
        choice = bahhh(
            "\nWhat do you do? ",
            ["1", "2", "3"]
        )
        if choice == "1":
            trap_door()
        elif choice == "2":
            flooded_tunnel_return()
        else:
            show_inventory()
            skeleton_chamber()
    elif choice == "2":
        trap_door()
    elif choice == "3":
        show_inventory()
        skeleton_chamber()
#----------------------------------
# TRAP DOOR
#------------------------------------
def trap_door():
    print(
        "\nYou explore the rest of the massive chamber."
    )
    print(
        "In the far corner, hidden beneath some rocks,"
    )
    print("you discover a trap door.")
    print("\n1. Go down the trap door")
    print("2. Leave the room")
    print("3. Check inventory")
    choice = bahhh(
        "\nWhat do you do? ",
        ["1", "2", "3"]
    )
    if choice == "1":
        prisoner_cell()
    elif choice == "2":
        print("\nYou decide not to open the trap door.")
        flooded_tunnel_return()
    else:
        show_inventory()
        trap_door()
#----------------------------------
# PRISONER CELL
#----------------------------------
def prisoner_cell():
    print("\n" + "=" * 50)
    print("THE PRISONER'S CELL")
    print("=" * 50)
    print("\nYou climb down into a dark chamber.")
    print(
        "At the far end is a prisoner trapped inside a cell."
    )
    print("He looks weak and exhausted.")
    print("\n1. Talk to the prisoner")
    print("2. Search your inventory")
    print("3. Leave the room")
    choice = bahhh(
        "\nWhat do you do? ",
        ["1", "2", "3"]
    )
    if choice == "1":
        print("\nThe prisoner looks at you.")
        print(
            '"Please, help me. I am starving. '
            'I\'ve been down here for weeks. '
            'If you help me, I can lead you out of this cave '
            'before you meet the same fate as me."'
        )
        print("\n1. Leave")
        print("2. Search your inventory")
        choice = bahhh(
            "\nWhat do you do? ",
            ["1", "2"]
        )
        if choice == "1":
            print("\nYou decide to leave the prisoner behind.")
            prisoner_cell_leave()
        else:
            use_item_for_prisoner()
    elif choice == "2":
        use_item_for_prisoner()
    else:
        prisoner_cell_leave()
#----------------------------------
#WASTE KEY
#----------------------------------

def use_item_for_prisoner():
    item = use_inventory_item()
    if item == "key":
        print("\nYou hold the key up to the prisoner's cell.")
        print("The lock clicks.")
        print("The cell door opens.")
        inventory["key"] -= 1
        global inventory_space
        inventory_space += 1
        if inventory["key"] == 0:
            del inventory["key"]
        print("\nThe prisoner steps out of the cell.")
        print('"Thank you."')
        print('"Follow me."')
        prisoner_choice()
    else:
        print("\nThat item cannot help the prisoner.")
        print("\n1. Try another item")
        print("2. Leave the room")
        choice = bahhh(
            "\nWhat do you do? ",
            ["1", "2"]
        )
        if choice == "1":
            use_item_for_prisoner()
        else:
            prisoner_cell_leave()
#----------------------------------
# PRISONER
#----------------------------------
def prisoner_choice():
    print("\n1. Follow the prisoner")
    print("2. Decline his offer")
    print("3. Check inventory")
    choice = bahhh(
        "\nWhat do you do? ",
        ["1", "2", "3"]
    )
    if choice == "1":
        print("\nYou decide to follow the prisoner.")
        print("You climb up the ladder after him.")
        print(
            "You return to the chamber "
            "with the dead skeleton."
        )
        print(
            "Together, you swim across the flooded tunnel."
        )
        print(
            "You make it safely back to the cave "
            "where you woke up."
        )
        starting_cave()
    elif choice == "2":
        print("\nYou decline the prisoner's offer.")
        print("The prisoner nods and leaves on his own.")
        print("\n1. Leave the room")
        choice = bahhh(
            "\nWhat do you do? ",
            ["1"]
        )
        if choice == "1":
            flooded_tunnel_return()
    else:
        show_inventory()
        prisoner_choice()

def prisoner_cell_leave():
    print("\nYou leave the prisoner behind.")
    print("You climb back up to the massive chamber.")
    flooded_tunnel_return()
def flooded_tunnel_return():
    print("\nYou return to the massive chamber.")
    print("The flooded tunnel is the only way back.")
    print("You carefully swim back through the tunnel.")
    print(
        "You make it safely to the cave "
        "where you first woke up."
    )
    starting_cave()
#----------------------------------
# LOCKED DOOR CAVE
#----------------------------------
def locked_door_cave():
    print("\n" + "=" * 50)
    print("THE LOCKED DOOR")
    print("=" * 50)
    print(
        "\nYou follow the path into a small cave opening."
    )
    print(
        "At the end of the cave is a large wooden door."
    )
    print("The door has a heavy lock on it.")
    print("\n1. Try opening the door")
    print("2. Leave the room")
    print("3. Check inventory")
    choice = bahhh(
        "\nWhat do you do? ",
        ["1", "2", "3"]
    )
    if choice == "1":
        print("\nYou grab the door handle and pull.")
        print("The door is locked.")
        print("You cannot open it.")
        locked_door_cave()
    elif choice == "2":
        print("\nYou leave the locked door behind.")
        starting_cave()
    elif choice == "3":
        show_inventory()
        item = use_inventory_item()
        if item == "key":
            print("\nYou insert the key into the lock.")
            print("The lock clicks.")
            print("\nYou escaped.")
            return
        else:
            print("\nThat item cannot unlock the door.")
            locked_door_cave()

#----------------------------------
#GAME START
#----------------------------------
print("\nWelcome to the cave, " + name + ".")
starting_cave()
