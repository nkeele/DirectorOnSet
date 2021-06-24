class Users(object):
    """Obtain user information and store it. Connect to other parts of the game to keep track of info."""

    def getUsers(input_list):

        while True:
            try:                
                n = int(input('Enter number of players: '))
                if n == 0:
                    raise ValueError
                break
            except (RuntimeError, TypeError, ValueError):
                print("\nInvalid input.")
        
        
        for i in range(0, n):
            usersIn = input(f'Enter name for player {i + 1}: ')
            input_list.append(usersIn)

        #print(f"getUsers before return: {input_list}")
        return input_list

    def displayUsers(input_list):
        print('Currently active users: ')
        if len(input_list) == 0:
            print('There are currently no active users.')
        else:
            for i in range(len(input_list)):
                print(i + 1, input_list[i])






