def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    while front_is_clear():
        move()
    if right_is_clear():
        turn_right()
    elif wall_on_right() == False:
        turn_left()
        move()
    elif wall_on_right():
        turn_left()
