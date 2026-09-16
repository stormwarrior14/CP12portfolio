import time #imports time
name = input("Enter a name for your character: ") #sets the variable "name" to the user's input
health = 100.0 #sets the player's health to 100
inventory_space = 10 #sets the maximum inventory space to 10
inventory = [] #creates a list called "inventory" that the player can store items in later by appending it into the list
alive = True #sets "alive" to be True at the start of the game
damage = 5 #sets the default damage value without any multipliers to be 5
while alive == True: #makes it so the code loops while "alive" is set to be True
    def suffocation(suff, air): #the suffocation functions
        global health, alive #brings the global variables "health" and "alive" into the function
        while air <= suff: #makes it so the code loops while the value of "air" is less than the value of "suff"
            while alive == True: #makes it so the code loops while "alive" is True
                health = health - damage #subtracts the "damage" value from "health" and makes that the new health value
                suff = suff - air #subtracts the "air" value from the "suff" value and makes that the new suff value
                time.sleep(0.5) #makes the code wait 0.5
                if health <= 0: #makes the code below only runs if the health is less than or equal to zero
                    alive = False #makes it so the "alive" is False
                    print(name + " is dead") #prints the playername and then "is dead"
                else: #makes it so that the code below only runs if the conditions for the if statement above is not met
                    alive = True #keeps alive as True
                    print(name + "'s current health is: " + str(health)) #prints the name of the player and the player's health
    suffocation(10, 4) #calls the suffocation functions with the "suff" value set to 10 and "air" value set to 4

