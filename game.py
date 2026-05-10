import random
#set gamestate
game_state = True
#player location
player_location = "bedroom"
#Adding tools
tools = {"bedroom": "flashlight", "kitchen": "key"}
inventory = []
#Adding locations
locations = ["bedroom", "kitchen", "living room"]
def main():

    start_game()
    if not game_state:
        return
    print_story()
    while game_state:
        #location printing
        #check for items 
        #pickup if there
        # where to?
        
        if not game_state:
            break
        print_location()
        move_player()
        if not game_state:
            break
        game_end()

def start_game():
    global game_state
    game_menu = input("\n\tThe Abondoned House\n\n\tStart\n\tQuit\n\n").title()
    if game_menu == "Quit":
        print("\nQuitting....")
        game_state = False
    else:
        print("\nLoading...")

def print_story():
    print('''\nIt's midnight, I am driving on a narrow road in the middle of a forest; Oh shit
I just hit something. (opens the car door and steps out looks behind, but sees
no one confused as he turns back to get into his car) Ahhh..... (Get hits by 
someone in the head and becomes unconcious After a while...) Where am I??(Wakes up in a room)
, I have to get out of here!")''')
    return

def print_location():
    global player_location
    print(f"\nI'm in the {player_location}")

def move_player():
    global player_location
    while True:
        go = input("\nWhere would you like to go?\nbedroom\nkitchen\nliving room\n\n ")
        if go not in locations:
            print("Invalid location please choose from the list")
        if player_location == go:
            print(f"Already in {player_location}")
        else:
            player_location = go
            print_location()
            beast()
            if not game_state:
                break
            check_up()
            break
        

def beast():
    global player_location
    global game_state
    beast_location = random.choice(locations)
    if beast_location == player_location:
        print("you are Dead")
        retry_input = input("Would you like to play again?(yes/no) ")
        if retry_input != "yes":
            game_state = False
        player_location = "bedroom"
    else:
        print("growlssss.........The beast is nearby")
        
def check_up():
    global player_location
    if player_location in tools:
        pick_up()
    else:
        print("There is nothing useful here!")
        
def pick_up():
    pick = input(f"Would you like to pickup {tools[player_location]}?(yes/no)? ")
    if pick =="yes":
        print("Picking up...")
        inventory.append(tools.pop(player_location))
        print(f"inventory updated: {inventory}")
    

def game_end():
    global player_location
    global game_state
    if "flashlight"in inventory and "key" in inventory and player_location == "living room":
        print("I am finally out of this house!")
        game_state = False
    else:
        print("I am missing one more thing!")
        

main()