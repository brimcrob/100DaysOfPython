def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    # start jump

    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

    # end jump


# number_of_hurdles = 6
# while number_of_hurdles > 0:
#    jump()
#    number_of_hurdles -=1
#   print(number_of_hurdles)

while not at_goal():
    print(at_goal())
    if front_is_clear() == True:
        print(front_is_clear())
        while not wall_in_front():
            print(wall_in_front())
            move()
    else:
        jump()
