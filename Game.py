

Player_alive = True
Victory = False

def menu():

    print(" welcome to the first version of Spectra , a text based RPG game ")

    Start_menu = input(str("what would you like to do : Start or Exit? "))

    if Start_menu == "start":
        print("Game start")
    else:
        print("goodbye")

def start():

    print("you wake up in a bare concrete room with no memory of how you got there."
          "in front of you is a door with a sign that says : 'welcome to spectra! try and survive!"
          )

    Start_input = input(str("would you like to open the door? (yes/no)")).strip()

    if Start_input == "yes":
        print("you open the door and this thing actually works ")
    else:
        print("just say yes or no")



def Door_1():

    print("You walk through a door into another room , there are two buttons on the wall "
          "one says 'Live' , and the other says 'die' , which do you pick? " )

    answer = input(str("choose live or die")).strip()

    if answer == "live":
        print("Yay you live ")
        Victory == True

    else:
        print(" You die ")











