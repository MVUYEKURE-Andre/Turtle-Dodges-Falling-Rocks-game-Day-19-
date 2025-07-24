from turtle import Turtle
import random
color=["green", "red", "blue","yellow","purple","chocolate"]
location_turtle=[-50,-80, 80,-90,-110,-150,-200,110,200,180,150,100,50]
player_go_distance=10
class Rock():
    def __init__(self):
        super().__init__()
        self.all_rock=[]
        self.random_rocks()

    def random_rocks(self):
        chance=random.randint(1,6)
        if chance==1:
            new_player=Turtle(shape="circle")
            new_player.right(90)
            new_player.color(random.choice(color))
            new_player.penup()
            y_position=random.choice(location_turtle)
            new_player.goto(y_position,260)
            self.all_rock.append(new_player)
    def player_move(self):
        for player in self.all_rock:
            player.forward(player_go_distance)

    # def game_over(self):


