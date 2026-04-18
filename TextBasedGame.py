#Denard Green 4/26
current_room = "Scullery"
required_items = ["Flask", "Satchel", "Sword", "Wand","tome","Boots"]
inventory = []
rooms = {
    #dictionary of rooms, room paths, and items in rooms
    "Scullery":    {"North": "Throne Room",
		            "East": "Storage"
                   },
    "Storage":     {"West":  "Scullery",
                    "item": "Flask"
                   },
    "Throne Room": {"East":  "Armory",
                    "North": "Bedroom",
                    "South": "Scullery",
                    "West": "Torture Room",
                    "item": "Satchel"
                   },
    "Armory":      {"West": "Throne Room",
                    "item": "Sword"
                   },
    "Library":     {"West": "Bedroom",
                    "item": "Wand"
                   },
    "Bedroom":     {"South": "Throne Room",
                    "East": "Library",
                    "item": "Boots"
                   },
    "Torture Room":{"East": "Throne Room",
                    "item": "Tome"
                   },
    "Cellar":      {"South": "Armory",
                    "item": "Shadow Creature"}
                   }
def instructions():
     print(''' 
     Collect all 6 items in the dungeon before conquering the Shadow Creature.
     Tread his lair too early at your own peril.
''')
def controls():
    print('''   
                Commands
               -----------
                Get[item]
       Go[North, East, South, West]
    ''')
def status():
    print("---------------------")
    print(f"current room is {current_room}")
    print(f"inventory:{inventory}")
    print("---------------------")
    if "item" in rooms[current_room] and rooms[current_room]["item"]:
        print(f"You spot a {rooms[current_room]["item"]} in the room")
    print("---------------------")
def clear():
    print("\n" * 50)
#initiate core game loop
while True:
    clear()
    instructions()
    controls()
    status()
    #recieve player input
    action = input(">").strip().title()
    action = action.split(" ", 1)
    #item pickup
    if action[0] == "Get":
        if action[1] == rooms[current_room]["item"]:
            print(f"{action[1]} has been added to your inventory.")
            inventory.append(rooms[current_room]["item"])
            del rooms[current_room]["item"]
        else:
            print(f"no {action[1]} is located in this room, try exploring more.")
    # a path for user to exit game
    elif action[0] == "Exit":
        current_room = "Exit"
        print("thank you for playing my game")
        break
    # move player to the room in the chosen direction
    elif action[0] ==  "Go":
        if action[1] in rooms[current_room]:
            current_room = rooms[current_room][action[1]]
            print(f"You are now in the {current_room}")
        else:
            print("You can't go there! Try entering a different direction!")
    #win condition: collect all items before confronting boss
    if all(item in inventory for item in required_items) and current_room == "Cellar":
        print("You use your collected power to slay the Shadow Creature Congratulations!!")
    #lose condition: enter boss room before collecting all items
    elif "item" in rooms[current_room] and rooms[current_room]["item"] == "Shadow Creature":
        print("The Creature devours you and your party")
        print("GAME OVER")
        break










