import random
from items import *


def default_options(health, sanity, coins, equipped):
    if health > 0:
        print("\nHealth:", health, "\nSanity:", sanity, "\nCoins:", coins, "\nEquipped:", equipped)
        print("[1] Walk Forward\n[2] Items\n[3] Unequip")

        return int(input())
    else:
        print("You have no health left!")
        print("You died...")
        print("GAME OVER")
        return "gameover"


def perform_event(event, meters, blackout, health, sanity, coins, slot1, slot2, slot3, equipped):
    cost = 0
    subchoice = 0
    attack_damage = item_damage[item_index_numbers.index(equipped)] + 5

    print("\n\n]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[")
    print("\n\nMETERS LEFT:", meters)
    if event == 1 or meters == 100:
        print("\nYou are now outside the school gates. Your house is about 100 meters away.")

    # tier 1 events (normal)
    if event == 2:  # default nothing happens
        if blackout:
            print("\nDarkness, all around...")
        else:
            print("\nThe street lights flicker...")
    if event == 3:  # drunkard encounter
        print("\nA drunkard approaches you...")
        print("Drunkard: *mumbles*")
        print("Drunkard: heyyyyy therre kid, got summ coins?")
        cost = random.randint(1, 5)

        while subchoice != 1 and subchoice != 3:
            print("[1] Give the drunkard", cost, "coins")
            print("[2] Talk to the drunkard")
            print("[3] Ignore the drunkard")
            subchoice = int(input())
            if subchoice == 1:
                print("You pay", cost, "to the drunkard.")
                print("Drunkard: tanks lil buddyy!")
                print("The drunkard walks away...")
                coins -= cost
            if subchoice == 2:
                x = random.randint(1, 3)
                if x == 1:
                    print("Drunkard: im goin home afterr drinkin 5 bottles of beerr andd i dont got any coins on me. "
                          "would yaa\nsparre summ change?")
                elif x == 2:
                    print("Drunkard: did y'know thad it wooud taze 'round ten-thousann normal balloons d' lift upp "
                          "d' average person?")
                elif x == 3:
                    print("Drunkard: hejayhf ierh ekareh beerrrr... erjkgsn give coins...")
            if subchoice == 3:
                x = random.randint(1, 5)
                if x == 1:
                    print("Drunkard: aww das tew baad...")
                    print("The drunkard walks away...")
                if x == 2 or x == 3:
                    print("The drunkard throws his bottle at you!")
                    print("You take 4 damage!")
                    print("The drunkard runs away...")
                    health -= 4
                if x == 4 or x == 5:
                    print("The drunkard throws his bottle at you!")
                    print("But it missed")
                    print("The drunkard runs away...")
                    print("You obtained Glass Shards!")
                    temporary_inv = obtain_item(5, slot1, slot2, slot3)
                    slot1 = temporary_inv[0]
                    slot2 = temporary_inv[1]
                    slot3 = temporary_inv[2]

    if event == 4:
        dog_hp = random.randint(8, 15)
        print("You are attacked by a wild dog!")
        print("The dog growls at you...")
        while subchoice != 1 and subchoice != 2:
            print("What will you do?")
            print("[1] Attack the dog")
            print("[2] Run away")
            subchoice = int(input())
        if subchoice == 1:
            while health > 0 and dog_hp > 0:
                if health <= 0:
                    print("You ran out of health and died!")
                else:
                    print("You attacked the wild dog and deal", attack_damage, "damage!")
                    dog_hp -= attack_damage
                if dog_hp <= 0 < health:
                    print("The wild dog died.")
                    x = random.randint(5,10)
                    print("You earned", x, "coins!")
                    coins += x
                elif health > 0:
                    y = random.randint(3,10)
                    print("The wild dog attacks and deals", y, "damage to you!")
                    health -= y
                    print("You have", health, "health left!")
                input("\nPress Enter to proceed: ")
        if subchoice == 2:
            x = random.randint(1,3)
            if x == 1:
                y = random.randint(3, 7)
                print("The wild dog bites you and deals", y, "damage!")
                health -= y
            if health <= 0:
                print("You ran out of health and died!")
            else:
                print("You ran away from the wild dog.")

    return [health, sanity, coins, slot1, slot2, slot3, equipped]
