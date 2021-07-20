from ReadFile import *
from Users import *
from TimerController import *
import threading
import signal

user_list = []
round_time = 0

#user_list = Users.getUsers(user_list)
#Users.displayUsers(user_list)
round_time = TimerController.ask_for_time()

print(f'Each round will last for {round_time} seconds.')

def timeout_handler(signal, frame):
    print('Time is up!')

if __name__ == '__main__':
    timer = threading.Thread(target=TimerController.count_time, args=(round_time,))
    display = threading.Thread(target=ReadFile.display_prompt)
    signal.signal(signal.SIGABRT, timeout_handler)

    while True:
        try:
            timer.start()
            display.start()
        except InterruptedError:
            pass
        for t in threading.enumerate():
            if t != threading.current_thread():
                t.join()









