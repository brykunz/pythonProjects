#print(r'''
#*******************************************************************************
#          |                   |                  |                     |
# _________|________________.=""_;=.______________|_____________________|_______
#|                   |  ,-"_,=""     `"=.|                  |
#|___________________|__"=._o`"-._        `"=.______________|___________________
#          |                `"=._o`"=._      _`"=._                     |
# _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
#|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
#|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
# _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
#|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
#|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
#____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
#/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
#____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
#/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
#____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
#/______/______/______/______/______/______/______/______/______/______/_____ /
#*******************************************************************************
#''')
#print("Welcome to Treasure Island.")
#print("Your mission is to find the treasure.")



location = 'clearing'

print("You're lost in the Hundred Acre Woods!\n"
      "Go find everything you need to get home.")
print("You find a Clearing after wandering around all morning.\n")

def check_location(location):
      has_key = True
      # has_honey = False
      # has_map = False
      has_mud = False
      has_rope = False
      befriend_gopher = False

      if location == 'dead':
            print("Game over!")
      elif location == 'clearing':
             print("You can see some landmarks from the Clearing:\n"
                  "Tree, River, Cave")
             location = input("Where to next? (type the location choice)\n").lower()
             check_location(location)
      elif location == 'river':
            if befriend_gopher == False:
                  print("You find the river has washed away the bridge that used to be here.")
                  location = input("Do you want to follow the river Downstream or head back to the Clearing?\n").lower()
                  check_location(location)
            else:
                  print("You find Gopher has drained the River by digging a hole to thank you. "
                        "You cross safely to the other side and continue down a path.")
                  location = 'house'
                  check_location(location)
      elif location == 'tree':
            choice_climb = input("You arrive at the Tree, and hear some buzzing from high above. Do you try and climb it?\n").lower()
            if choice_climb == 'yes':
                  if has_rope == False:
                        print("You try to climb the tree, but slip and fall to your Death.\n")
                        location = 'dead'
                        check_location(location)
                  elif has_mud == False and has_rope == True:
                        print("You use the rope to climb the tree, but the bee's sting you and you fall to your Death.\n")
                        location = 'dead'
                        check_location(location)
                  else:
                        print("You safely climb the tree and collect some Honey!\n")
                        has_honey = True
                        location = input("Do you go back down the hill to the Clearing, or travel on towards the Garden?\n").lower()
                        check_location(location)
            else:
                  location = input("Do you go back down the hill to the Clearing, or travel on towards the Garden?\n").lower()
                  check_location(location)
      elif location == 'cave':
            choice_dig = input("You arrive at the Cave. You see a mound of dirt. Do you dig it up?\n").lower()
            if choice_dig == 'yes':
                  print("You found Gopher! He thanks you for helping him out of the dirt pile. He knows of a way to help cross the river!\n")
                  befriend_gopher = True
                  location = input("Do you go back out the Cave to the Clearing, or stay in the Cave?\n").lower()
                  check_location(location)
      elif location == 'house':
            choice_house = input("You arrive at the House. Do you go inside?\n").lower()
            if choice_house == 'yes' and has_key == True:
                  print("You win!\n")
            elif choice_house == 'yes' and has_key == False:
                  print("the door is locked. Game over")
check_location(location)

   #   if location == 'garden':
    #  if location == 'downstream':
    #  if location == 'cave':