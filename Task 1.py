print("Stop! Who would cross the Bridge of Death \n Must answer me these questions three, 'ere the other side he see.")

Might = input("\nWhat is your name?: ")    # Ask the user name. Any name, but the King (Arthur) is allowed to pass without any further questions.
if Might.capitalize() == "Arthur":
    print("My liege! You may pass!" )

else:
    Killer = input("What is your quest?: ") #The Grail (any response with "grail" in it is acceptable).

    if "Grail"in Killer.capitalize():
        print("Only those who seek the Grail may pass.")

    else:
        Bang = input("What is your favourite colour?: ")  # Any colour that begins with the same letter as the Knight's name. (The Bridge-Keeper does not check that the answer actually is a colour.).
        print("You may pass!" if Might[0].capitalize() == Bang[0].capitalize() else "Incorrect! You must now face the Gorge of Eternal Peril.")