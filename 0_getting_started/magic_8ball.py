import random #imports random
import time #imports time
responses = ["Undoubtedly so", "Highly doubtful", "Absolutely", "Absolutely not", "Possibly so", "Maybe", "Uncertain. Try again later.", "I envy your optimism"] #list of responses the magic 8 ball can output
quit_list = ["quit", "QUIT", "Quit"] #list of all possible things the user can type to quit the loop of the magic 8 ball 
question = 1 #just setting the question variable to something before user input (im sure there's a better way to do this but i cant bother)
while question not in quit_list: #making it so this loops infinitely until the user quits it by typing in one of the items in the "quit_list"
    question = input("Hi, I'm magic 8 ball! Your personal helper friend! Ask me anything! I know everything! (Actually, I can only answer yes or no questions. I lied.) ") #sets the variable "question" as whatever the user enters as their question via responding to the initial prompt
    time.sleep(0.5)
    print("thinking...") #prints the message "thinking"
    time.sleep(0.5)
    print("Analyzing your question: " + question) #just repeats the user's questions to build suspense or whatever
    time.sleep(0.5)
    if question != 1: #just checks if the user atually input a question
        response = random.choice(responses) #randomly selects one of the items in the "responses" list and sets it as the variable "response"
        print(response) #prints the response
        responses.remove(response) #removes the choosen response from the list of responses so there are no repeats 
        time.sleep(0.5)
        question = input("Type 'Quit' to quit: ") #just tells the user to type "quit" to "quit" and then puts whatever they typed into the questions variable
        if question not in quit_list:
            question = 1 #just resets the question variable to "1" so the code actually works
        time.sleep(0.5)
