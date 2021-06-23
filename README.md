# DirectorOnSet README
Director on Set is a Python project originally concepted by my SO. I decided to turn this into a project to add to my portfolio because, well, I needed one, and because I thought it was a very cool idea to have this accessible and usable either by me when I act in plays in my free time, or for others who know about it to use for improv/acting tools.

As completion gets closer and closer, I will update this README with more information on classes and their functions, general documentation for using the code, etc.

For now, it is all pretty basic, this is what I have:

DirectorOnSet:
  This is the main class of the project. So far it is making calls to the other classes, as well as managing parameters being used by other classes, such as user_list that holds the users for the current session.
  
Randomizer:
  This class will randomize whatever is needed for the game. So far <b>randomizePrompt</b> will generate a random number based on an int value passed into the function, and return that value.
  
ReadFile:
   This class will read the file that stores the prompts to be given to the players. <b>readPrompt</b> will open the file, count the number of lines in the file (prompts are organized by line on the prompt list .txt file), call for a random number based on that count, then the returned int will be the line number indicating which prompt to show.
   
Users:
  This class will take in a list (created in the main class) of strings to store the users playing the game. This gets sent back to the main class so that it can be used for other functions.
  
TimerController:
  This class controls the timer used while the players are given prompts. Users enter a preferred time to work through prompts, and their round will end when the timer reaches zero.
  
  <b>Note 6/23/21:</b> The functions in the ReadFile class will change so that one function opens the file, calls another function of the same class to count and retrieve a random prompt, display (x) number within the time limit, then return to the function that opened the file to then close the file.</br>
  <b>Append:</b> Also, create a list of ints to carry each random number given from the Randomizer class so that each new random number is unique and not a repeat of a previous prompt. As the list of prompts gets longer, I can also add a list to store which prompts have been used so that in each session, the same prompt never comes up a second time.
