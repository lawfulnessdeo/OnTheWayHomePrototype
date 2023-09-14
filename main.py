from events import *

print("       ▐ ▄     ▄▄▄▄▄ ▄ .▄▄▄▄ .    ▄▄▌ ▐ ▄▌ ▄▄▄· ▄· ▄▌     ▄ .▄      • ▌ ▄ ·. ▄▄▄ .")
print("▪     •█▌▐█    •██  ██▪▐█▀▄.▀·    ██· █▌▐█▐█ ▀█▐█▪██▌    ██▪▐█▪     ·██ ▐███▪▀▄.▀·")
print(" ▄█▀▄ ▐█▐▐▌     ▐█.▪██▀▐█▐▀▀▪▄    ██▪▐█▐▐▌▄█▀▀█▐█▌▐█▪    ██▀▐█ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄")
print("▐█▌.▐▌██▐█▌     ▐█▌·██▌▐▀▐█▄▄▌    ▐█▌██▐█▌▐█ ▪▐▌▐█▀·.    ██▌▐▀▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌")
print(" ▀█▄▀▪▀▀ █▪     ▀▀▀ ▀▀▀ · ▀▀▀      ▀▀▀▀ ▀▪ ▀  ▀  ▀ •     ▀▀▀ · ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀ ")

print("\nAfter long day at school, you can finally go home. As you go outside, you are greeted with the cold darkness of the night.")
print("With no one to pick you up, you only have one choice: Walk Home\n")

print("[1] Walk Forward\n[2] Stay at School")

choice = int(input())
health = 100
sanity = 100
meters = 0

if choice == 2:
    #Ending 1
    print("\nENDING 1 of N")
    print("You chose stay at school for the rest of the night. The morning arrives and you were made fun of for spending the night at school.")
    print("Maybe you should try again?")

if choice == 1:
    #The game starts
    #event 1 is always the start
    meters += 1
    perform_event(1, meters)
    default_options(health, sanity)
    
