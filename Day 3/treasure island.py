print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
left_or_right = input("You're at crossroads. You want go 'Left' or 'Right'?\n").lower().strip()
if left_or_right != "left":
    print("You fell into a hole.\nGame Over")
swim_or_wait = input("You arrive a lake, there is a small island a short distance away. "
                     "Do you 'Wait' or 'Swim'?\n").lower().strip()
if swim_or_wait == "swim":
    print("You get in the water and start swimming.\nA huge fish attacks you and eats you.\nGame Over.")
which_door = input("A boat arrives and takes you over to the island. There is a house with 3 doors.\n Red, Yellow "
                   "and Blue. Which one do you choose?\n").strip().lower()
if which_door == "yellow":
    print("You Chose Well, as the door opens you see a treasure chest laden with gold.\nYou Win!")
elif which_door == "blue":
    print("You open the Blue door only to met by a room full horrific beasts that attack and kill you.\nGame Over.")
elif which_door == "red":
    print("You open the Red door and flames shoot out and burn you up.\nGame Over.")
else:
    print("Wrong Choice.\nGame Over.")
