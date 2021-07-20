import time
import signal

class TimerController(object):
    """Takes a user-given value of time and sets time limits based on that value."""
    
    def ask_for_time():

        while True:
            try:
                time_limit = int(input('How long (in seconds) would you like the round to last? '))
                if time_limit <= 0:
                    raise ValueError
                break
            except (ValueError, TypeError):
                print('\nInvalid Input.')

        return time_limit

    def count_time(set_time):

        while set_time > 0:
            min, sec = divmod(set_time, 60)
            timer = '{:02d}:{:02d}'.format(min, sec)
            print(timer, end = '\r')
            time.sleep(1)
            set_time -= 1
        return False

        







