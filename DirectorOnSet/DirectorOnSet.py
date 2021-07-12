from ReadFile import *
from Users import *
from TimerController import *
import threading

user_list = []
round_time = 0

#user_list = Users.getUsers(user_list)
#Users.displayUsers(user_list)
round_time = TimerController.ask_for_time()

print(f'Each round will last for {round_time} seconds.')

if __name__ == '__main__':
    timer = threading.Thread(target=TimerController.count_time, args=(round_time,))
    display = threading.Thread(target=ReadFile.read_prompt)

    timer.start()
    display.start()
    
    if timer.join():
        display.join()








