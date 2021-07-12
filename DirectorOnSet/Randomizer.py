##from random import seed
from random import randint

class Randomizer(object):
    """This class will generate a random number within specific ranges to send to classes needing a random number."""

    def randomize_prompt_line(count):
        print("randomizePrompt count = ", count)
        for _ in range(count):
            value = randint(0, count)
            
        if value == 0:
            return 0
        else:
            print(f'Returning {value}')
            return value
    def randomize_users(input_list):
        count = 0
        for i in input_list:
            if i:
                count += 1

        for _ in range(count):
            value = randint(0, count)

        if value == 0:
            return 0
        else:
            return value

