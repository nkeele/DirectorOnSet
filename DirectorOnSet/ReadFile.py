from Randomizer import *

class ReadFile(object):
    """This class will read the text file of prompts to display during the game."""    

    #change this to open the file, call another
    #function to generate the prompt, then
    #end this with closing the file. 
    def readPrompt():
        Counter = 0
        f = open('TestPrompts.txt', 'r')
        prompt_list = f.readlines()
        for i in prompt_list:
            if i:
                Counter += 1

        #print("readPrompt Counter = ", Counter)
        prompt_line = Randomizer.randomizePrompt(Counter - 1)
        #print("readPrompt prompt_line = ", prompt_line)
        print(prompt_list[prompt_line])
        close('TestPrompts.txt')










