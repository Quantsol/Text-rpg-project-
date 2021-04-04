


def menu():

    print(" welcome to the first version of Spectra , a text based RPG game ")

    Start_menu = input(str("what would you like to do : Start or Exit? "))

    if Start_menu == "start":
        print("Game start")
        return "doors"
    else:
        print("goodbye")

def start():

    print("you wake up in a bare concrete room with no memory of how you got there."
          "in front of you is a door with a sign that says : 'welcome to spectra! try and survive!"
          )

    door_1 = input(str("would you like to open the door? (yes/no)"))

    if door_1 == "yes":
        print("you open the door and this thing actually works ")
    else:
        print("wtf just say yes or no")


menu()

if menu() == "doors":
    start()












