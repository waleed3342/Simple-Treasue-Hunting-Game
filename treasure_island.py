print("Welcome to Treasure Island.\nYour mission is to find the treasure. ")
direction = input("Your're at the cross road. Where do you want to go? \n Type  \"Left\" or \"Right\"")
if direction.upper() == "LEFT":
    print("You've come to a lake. There is an island in the middle of the lake.")
    travel = input("Type \"Wait\" to wait for a boat. Type \"Swim\" to swim across.")
    if travel.upper() == "WAIT":
        print("The Boat Has Arrived You Succesfully Reached the Island. ")
        rooms = input("There are 3 doors of room only 1 room has treasure. \nFor Door one press \"1\"\nFor Door Two press \"2\"\nFor Door Three press \"3\"")
        if rooms == "3":
            print("You found the treasure. You won the game!")
            treasure_design = r"""
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._ 
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===!/========================!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
           |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`

                            _.--.
                        _.-'_:-'|| 
                    _.-'_.-::::'|| 
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._ 
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|| 
              `>'-.!@%()@'@_%-'_.-o _.|'|| 
               ||-._'-.@.-'_.-' _.-o  |'|| 
               ||=[ '-._.-//-.-'    o |'|| 
               || '-.]=|| |'|      o  |'|| 
               ||      || |'|        _| 
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
             '-._'-.|| |' `_.-'
                    '-.||_/.-'
            """
            print(treasure_design)
        elif rooms == "1":
            print("You found a Beast. Game over!")
        elif rooms == "2":
            print("You found a Pirate. Game over!")
        else:
            print("You entered a wrong number. Game over!")
    else:
        print("You got eaten by an alligator. Game over!")
else:
    print("You fell into a hole. Game over!")
        