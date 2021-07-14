from Randomizer import *
from TimerController import *
import queue

class ReadFile(object):
    """This class will read the text file of prompts to display during the game."""    

    def display_prompt():
        f = open('TestPrompts.txt', 'r')
        prompt_list = f.readlines()
        f.close()
        counter = len(prompt_list)
        print(counter)
        try:
            while prompt_list and counter != 0: #and stop_check == False
                    prompt_line = Randomizer.randomize_prompt_line(counter - 1)
                    print(prompt_list.pop(prompt_line))
                    counter -= 1
                    input("Press Enter for next prompt\n")
        except Exception as e:
                print(e)

        

       
        #Enter the list to the queue at random, but only placing one of 
        #each prompts. Don't double on them. List for numbers, do a check, re roll if
        #number is in the list?

        #pull the prompts
        #count how many prompts there are
        #generate a random number and pop the prompt at that index. 
            #if the same number is generated later, it will indicate a value different than what was used before.












