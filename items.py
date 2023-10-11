# list of items + index numbers

item_index_numbers = ["", "Stick", "Rock", "Juice Box", "Pack of Chips", "Glass Shards", "Knife", "MedKit", "Pills"]
item_healing = [0, 0, 0, 10, 15, 0, 0, 50, 0]
item_sanity = [0, 0, 0, 2, 3, 0, 0, 10, 50]
item_damage = [0, 6, 0, 0, 0, 0, 20, 0, 0]
item_sold_price = [0, 10, 10, 15, 15, 30, 20, 25, 15]
item_bought_price = [0, 2, 2, 20, 20, 10, 35, 45, 35]


def open_inventory(slot1, slot2, slot3, health, sanity, equipped):
    choice = 0
    while choice != 4:
        print("Inventory:")
        print("[1]", slot1)
        print("[2]", slot2)
        print("[3]", slot3)
        print("[4] Exit")
        choice = int(input())
        used = False
        if choice == 1:
            if slot1 != "":
                if item_healing[item_index_numbers.index(slot1)] > 0:
                    print("Healed", item_healing[item_index_numbers.index(slot1)], "health.")
                    health += item_healing[item_index_numbers.index(slot1)]
                    used = True
                if item_sanity[item_index_numbers.index(slot1)] > 0:
                    print("Recovered", item_sanity[item_index_numbers.index(slot1)], "sanity.")
                    sanity += item_sanity[item_index_numbers.index(slot1)]
                    used = True
                if item_damage[item_index_numbers.index(slot1)] > 0 and equipped == "":
                    print("Equipped", slot1)
                    equipped = slot1
                    used = True
                if used:
                    slot1 = ""
        if choice == 2:
            if slot2 != "":
                if item_healing[item_index_numbers.index(slot2)] > 0:
                    print("Healed", item_healing[item_index_numbers.index(slot2)], "health.")
                    health += item_healing[item_index_numbers.index(slot2)]
                    used = True
                if item_sanity[item_index_numbers.index(slot2)] > 0:
                    print("Recovered", item_sanity[item_index_numbers.index(slot2)], "sanity.")
                    sanity += item_sanity[item_index_numbers.index(slot2)]
                    used = True
                if item_damage[item_index_numbers.index(slot2)] > 0 and equipped == "":
                    print("Equipped", slot2)
                    equipped = slot2
                    used = True
                if used:
                    slot2 = ""
        if choice == 3:
            if slot3 != "":
                if item_healing[item_index_numbers.index(slot3)] > 0:
                    print("Healed", item_healing[item_index_numbers.index(slot3)], "health.")
                    health += item_healing[item_index_numbers.index(slot3)]
                    used = True
                if item_sanity[item_index_numbers.index(slot3)] > 0:
                    print("Recovered", item_sanity[item_index_numbers.index(slot3)], "sanity.")
                    sanity += item_sanity[item_index_numbers.index(slot3)]
                    used = True
                if item_damage[item_index_numbers.index(slot3)] > 0 and equipped == "":
                    print("Equipped", slot3)
                    equipped = slot3
                    used = True
                if used:
                    slot3 = ""
    return [slot1, slot2, slot3, health, sanity, equipped]


def obtain_item(item, slot1, slot2, slot3):
    if slot1 == "":
        slot1 = item_index_numbers[item]
    elif slot2 == "":
        slot2 = item_index_numbers[item]
    elif slot3 == "":
        slot3 = item_index_numbers[item]
    else:
        choice = 0
        while choice != 1 and choice != 2:
            print("\nYou do not have enough space in your inventory. Would you like to drop an item?")
            print("[1] Yes\n[2] No")
            choice = int(input())
        if choice == 1:
            choice = 0
            while choice != 1 and choice != 2 and choice != 3:
                print("\nChoose which item to drop to make room for " + item_index_numbers[item] + ":")
                print("\nInventory:")
                print("[1]", slot1)
                print("[2]", slot2)
                print("[3]", slot3)
                choice = int(input())
            if choice == 1:
                print(slot1, "was dropped")
                slot1 = item_index_numbers[item]
            elif choice == 2:
                print(slot2, "was dropped")
                slot2 = item_index_numbers[item]
            elif choice == 3:
                print(slot3, "was dropped")
                slot3 = item_index_numbers[item]
        elif choice == 2:
            print(item_index_numbers[item], "was dropped")

    return [slot1, slot2, slot3]
