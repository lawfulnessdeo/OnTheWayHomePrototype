import random
from events import *

print("       ▐ ▄     ▄▄▄▄▄ ▄ .▄▄▄▄ .    ▄▄▌ ▐ ▄▌ ▄▄▄· ▄· ▄▌     ▄ .▄      • ▌ ▄ ·. ▄▄▄ .")
print("▪     •█▌▐█    •██  ██▪▐█▀▄.▀·    ██· █▌▐█▐█ ▀█▐█▪██▌    ██▪▐█▪     ·██ ▐███▪▀▄.▀·")
print(" ▄█▀▄ ▐█▐▐▌     ▐█.▪██▀▐█▐▀▀▪▄    ██▪▐█▐▐▌▄█▀▀█▐█▌▐█▪    ██▀▐█ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄")
print("▐█▌.▐▌██▐█▌     ▐█▌·██▌▐▀▐█▄▄▌    ▐█▌██▐█▌▐█ ▪▐▌▐█▀·.    ██▌▐▀▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌")
print(" ▀█▄▀▪▀▀ █▪     ▀▀▀ ▀▀▀ · ▀▀▀      ▀▀▀▀ ▀▪ ▀  ▀  ▀ •     ▀▀▀ · ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀ ")

print(
    "\nAfter long day at school, you can finally go home. As you go outside, you are greeted with the cold darkness "
    "of the night.")
print("With no one to pick you up, you only have one choice: Walk Home\n")

print("[1] Walk Forward\n[2] Stay at School")

choice = int(input())
health = 100
sanity = 100
meters = 100
inventory = ["Knife", "Juice Box", "Pack of Chips"]
equipped = ""

coins = 20
blackout = False

if choice == 2:
    # Ending 1
    print("\nENDING 1 of N")
    print(
        "You chose stay at school for the rest of the night. The morning arrives and you were made fun of for "
        "spending the night at school.")
    print("Maybe you should try again?")

if choice == 1:
    # The game starts
    # event 1 is always the start
    while meters > 0 and choice != "gameover":
        choice = 0
        event_random = random.randint(2, 4)
        stat_updates = perform_event(event_random, meters, blackout, health, sanity, coins, inventory[0], inventory[1],
                                     inventory[2], equipped)
        health = stat_updates[0]
        sanity = stat_updates[1]
        coins = stat_updates[2]
        inventory = [stat_updates[3], stat_updates[4], stat_updates[5]]
        equipped = stat_updates[6]

        while choice != 1 and choice != "gameover":
            choice = default_options(health, sanity, coins, equipped)
            if choice == 2:
                temporary_inv1 = open_inventory(inventory[0], inventory[1], inventory[2], health, sanity, equipped)
                inventory[0] = temporary_inv1[0]
                inventory[1] = temporary_inv1[1]
                inventory[2] = temporary_inv1[2]
                health = temporary_inv1[3]
                sanity = temporary_inv1[4]
                equipped = temporary_inv1[5]
            if choice == 3:
                if equipped != "":
                    temporary_inv2 = obtain_item(item_index_numbers.index(equipped), inventory[0], inventory[1],
                                                 inventory[2])
                    inventory[0] = temporary_inv2[0]
                    inventory[1] = temporary_inv2[1]
                    inventory[2] = temporary_inv2[2]
                    equipped = ""
                else:
                    print("Nothing to unequip!")
        meters -= 1
