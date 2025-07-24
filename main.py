# Turtle Dodges Falling Rocks

# 1.create screen
# 2. creating turtle player
# 3. make player move in left and in the right
# 4. creating randomly generated rocks from top
# 5. moving rock from top to bottom
# 6. detecting the collision between the rock and the player
# 7.creating the score to keep records
# 8. after 10 second score+=1

from turtle import Screen
import time
from player import Player
from rock import Rock
screen=Screen()
screen.setup(width=600,height=600)
screen.title("WELCOME TO Turtle Dodges Falling Rocks")
screen.tracer(0)

rock=Rock()
player=Player()

screen.listen()
screen.onkey(player.go_right,"Right")
screen.onkey(player.go_left,"Left")


is_game_on=True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    rock.random_rocks()
    rock.player_move()
    # detecting collision with rocks
    for rock_detect in rock.all_rock:
        if rock_detect.distance(player)<=20:
            is_game_on=False
            print("you hit the wall")




screen.exitonclick()
