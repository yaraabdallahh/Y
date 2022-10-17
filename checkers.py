"""
Progamme: Checkers
By: Yara, Alissar
"""

import turtle



ROWS =20

COLUMNS =20

PIXEL_SIZE =30



turtle.speed(0)

turtle.up()

turtle.goto(-300,300)

def grid():

    for i in range(ROWS):

        turtle.down()

        for j in range (COLUMNS):

            #conditional statement to select color

            if (i+j) % 2:

                turtle.fillcolor("black")

            else:

                turtle.fillcolor("red")

            turtle.begin_fill()

            for k in range(4):

                turtle.forward(PIXEL_SIZE)

                turtle.right(90)

            turtle.end_fill()

            turtle.forward(PIXEL_SIZE) #PIXEL_SIZE

        turtle.up()

        turtle.goto(-300, turtle.ycor()-PIXEL_SIZE)

grid()

turtle.done()