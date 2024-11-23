import random
import turtle

from sterren_module import *

kleuren = ("red", "orange", "yellow", "lime green", "orchid", "magenta", "dodger blue", "crimson", "chocolate", "navy", "salmon", "green yellow", "teal", "cyan", "aquamarine", "hot pink", "firebrick", "royal blue", "wheat")

for i in range(1000):

    random_x = random.randint(-500, 500)
    random_y = random.randint(-400, 400)
    random_color = random.choice(kleuren)

    teken_ster(random_x,random_y,random_color)

turtle.exitonclick()