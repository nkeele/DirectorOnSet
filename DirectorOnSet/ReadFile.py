from Randomizer import *
from TimerController import *
import queue

class ReadFile(object):
    """This class will read the text file of prompts to display during the game."""    


    def read_prompt():
        f = open('TestPrompts.txt', 'r')
        ReadFile.cycle_prompts(f)
        f.close()

    def cycle_prompts(f):
        Counter = 0
        prompt_list = f.readlines()
        for i in prompt_list:
            if i:
                Counter += 1

        
        #print("readPrompt Counter = ", Counter)
        prompt_line = Randomizer.randomize_prompt_line(Counter - 1)
        #print("readPrompt prompt_line = ", prompt_line)
        print(prompt_list[prompt_line])   
        
        #Enter the list to the queue at random, but only placing one of 
        #each prompts. Don't double on them. List for numbers, do a check, re roll if
        #number is in the list?












