# Kody Greenberg 8/11/22 name: TextBasedGame.py for: Prof. Gabe

def main():
    # Function for instructions
    def instructions():
        print('\nWelcome! Thanks for playing Kody\'s text based game!\n')
        print('Your girl is fighting Mother Nature... You need to show her love and care for her!')
        print('To do this, you must run through the house and find 8 things that make her happy or help her.')
        print(
            'But beware! She may be lurking around any corner. If you run into her without all 8 items you will be sent to the dog house and lose.')
        print('To grab an item, simply type Y for yes.\n')
        print('To start type North, South, East, or West to move.\n')
        print('Otherwise, type Exit to leave the game.\n')
        print('The ">" indicates the area you can type at.\n')

    # Function to print the current room if a player has trouble.
    def room_print(current_room, *poss_moves):
        if current_room == rooms_list[0]:
            print('Since you are in the Ballroom you can move North, South, East, or West')
        elif current_room == rooms_list[7]:
            print('Since you are in the Library you can move South, East, or West')
        elif current_room == rooms_list[1]:
            print('Since you are in the {} you can move {} or {}'.format(current_room, *poss_moves))
        elif current_room == rooms_list[3]:
            print('Since you are in the {} you can move {} or {}'.format(current_room, *poss_moves))
        elif current_room == rooms_list[5]:
            print('Since you are in the {} you can move {} or {}'.format(current_room, *poss_moves))
        elif current_room == rooms_list[2] or rooms_list[4] or rooms['Bedroom'] or rooms_list[8]:
            print('Since you are in the {} you can move {}'.format(current_room, *poss_moves))

    # Define status function
    def status(current_room, inventory):
        print('_' * 20)
        print('You are in the {}'.format(current_room))
        print('Your current inventory: {}\n'.format(inventory))

    # This dictionary links a room to other rooms according to map provided.
    rooms = {'Ballroom': {'north': 'Library', 'south': 'Basement', 'west': 'Game Room', 'east': 'Kitchen', 'item': ''},
             'Game Room': {'south': 'Lavatory', 'east': 'Ballroom', 'item': 'Potato Chips'},
             'Lavatory': {'north': 'Game Room', 'item': 'Hygiene Products'},
             'Basement': {'north': 'Ballroom', 'east': 'Wine Cellar', 'item': 'Roses'},
             'Wine Cellar': {'west': 'Basement', 'item': 'Wine'},
             'Kitchen': {'north': 'Bedroom', 'west': 'Ballroom', 'item': 'Candy'},
             'Bedroom': {'south': 'Kitchen', 'item': 'Chocolate'},
             'Library': {'south': 'Ballroom', 'east': 'Cat Room', 'west': 'PC Room', 'item': 'Handwritten Card'},
             'Cat Room': {'west': 'Library', 'item': 'Cat'},
             'PC Room': {'east': 'Library', 'item': 'Girl'}
             }

    # Inventory for the player to fill
    inventory = []
    # Rooms dictionary made into a list for quick checking of room indexes.
    rooms_list = list(rooms)
    # Starting room
    current_room = rooms_list[0]
    # Print instructions once
    instructions()
    # Loop of gameplay
    while True:

        # Get possible moves from the dict
        poss_moves = rooms[current_room].keys()

        # Print current status before getting input
        status(current_room, inventory)
        room_print(current_room, *poss_moves)

        # Get input from player
        player_cmd = input('What would you like to do? >').strip().lower()
        print('You entered:', player_cmd)

        # Directions that should be input
        directions = ['north', 'south', 'east', 'west']

        # Move rooms loop
        if player_cmd == 'exit':
            print('Thanks for playing!')
            break
        # Moving between rooms
        if player_cmd in directions:
            if player_cmd in rooms[current_room]:
                new_room = rooms[current_room][player_cmd]
                current_room = new_room
                print('\nYou have entered the {}'.format(current_room))
            else:
                print('\nPlease only enter a command that will work in your room.\n')
                # Call print room function to help guide the player where they can go.
                room_print(current_room, *poss_moves)
        else:
            print('Please only enter a command that will work in your room.')
            # Call print room function to help guide the player where they can go.
            room_print(current_room, *poss_moves)

        # If there is an item
        if rooms[current_room] == rooms['Ballroom']:
            print('Continue on, there may be more items you need to help your girl.')
        elif rooms[current_room]['item'] in inventory:
            print('Continue on, there may be more items you need to help your girl.')
        # else if to check if the inventory is full or if they run into the girl too soon.
        elif current_room == rooms_list[9] and len(inventory) >= 8:
            print('Who hoo! You get to sleep in bed tonight! Tomorrow’s another story... Good luck.')
            break
        elif current_room == rooms_list[9] and len(inventory) <= 7:
            print('OH NO! You found your girl before you had all your items and are now in the doghouse.')
            print('Try again later.')
            break
        # Append an item and hint if they find all items.
        elif rooms[current_room]['item'] != '':
            print('\nThe item located in this room is {}'.format(rooms[current_room]['item']))
            add_inv = input('\nWould you like to pick it up? Type Y for yes >').lower().strip()
            while add_inv != 'y':
                print('Please add this item! You must grab it by typing "Y"')
                add_inv = input('>').lower().strip()
            else:
                item = rooms[current_room]['item']
                inventory.append(item)
                if len(inventory) >= 8:
                    print('>'* 30, '<' * 30)
                    print('Looks like you have successfully gotten all items needed to calm your girl!')
                    print('Now find her in the PC Room far to the North and East of the Ballroom')
                    print('>' * 30, '<' * 30)


if __name__ == '__main__':
    main()
