import turtle

ROWS = 20

COLUMNS = 20    

PIXEL_SIZE = 30



def grid():

    turtle.speed(0)

    turtle.up()

    turtle.goto(-300,300)

    for i in range(ROWS):

        turtle.down()

        for j in range (COLUMNS):

            draw_green_pixel()

            draw_red_pixel()

            draw_black_pixel()

            draw_yellow_pixel()

            draw_orange_pixel()                       

            draw_yellowgreen_pixel()

            draw_sienna_pixel()

            draw_tan_pixel()

            draw_darkgray_pixel()




def newRow():

    turtle.right(90)

    turtle.forward(30)

    turtle.right(90)                

    turtle.forward(600)

    turtle.left(180)

    

  

                

turtle.up()

#turtle.goto(-300, turtle.ycor()-PIXEL_SIZE)

turtle.goto(-300,300)







def draw():

    turtle.speed(0)                      

    turtle.tracer(False)

    turtle.up()

    

    with open(input("Enter the drawing: "), "r") as file:

        ic = file.read().splitlines() #split each line inside of the drawing file into an array which the code reads as individual inputs

        for row in ic:

            for c in row:            

                if c =="0":

                    draw_black_pixel()

                if c == "1":

                    draw_white_pixel()

                if c == "2":

                    draw_red_pixel()

                if c == "3":

                    draw_yellow_pixel()

                if c == "4":

                    draw_orange_pixel()

                if c == '5':

                    draw_green_pixel()

                if c == "6":

                    draw_yellowgreen_pixel()

                if c == "7":

                    draw_sienna_pixel()

                if c == "8":

                    draw_tan_pixel()

                if c == "9":

                    draw_gray_pixel()

                if c == "A":

                    draw_darkgray_pixel()     #assigning a number to each color

            

            newRow() 









def draw_white_pixel():

    turtle.fillcolor("white")    



    turtle.begin_fill()

    for k in range(4):

        turtle.forward(PIXEL_SIZE)    

        turtle.right(90)

            

    turtle.forward(PIXEL_SIZE) #PIXEL_SIZE

    turtle.end_fill()



def draw_green_pixel():

    turtle.fillcolor("green")



    turtle.begin_fill()

    for k in range(4):

        turtle.forward(PIXEL_SIZE)

        turtle.right(90)

            

    turtle.forward(PIXEL_SIZE) #PIXEL_SIZE

    turtle.end_fill()



def draw_red_pixel():

    turtle.fillcolor("red")



    turtle.begin_fill()

    for k in range(4):

        turtle.forward(PIXEL_SIZE)

        turtle.right(90)

            

    turtle.forward(PIXEL_SIZE) #PIXEL_SIZE

    turtle.end_fill()



def draw_black_pixel():

    turtle.fillcolor("black")



    turtle.begin_fill()

    for k in range(4):

        turtle.forward(PIXEL_SIZE)

        turtle.right(90)

            

    turtle.forward(PIXEL_SIZE) #PIXEL_SIZE

    turtle.end_fill()



def draw_yellow_pixel():

    turtle.fillcolor("yellow")



    turtle.begin_fill()

    for k in range(4):

        turtle.forward(PIXEL_SIZE)

        turtle.right(90)

            

    turtle.forward(PIXEL_SIZE) #PIXEL_SIZE

    turtle.end_fill()



def draw_orange_pixel():

    turtle.fillcolor("orange")



    turtle.begin_fill()

    for k in range(4):

        turtle.forward(PIXEL_SIZE)

        turtle.right(90)

            

    turtle.forward(PIXEL_SIZE) #PIXEL_SIZE

    turtle.end_fill()



def draw_yellowgreen_pixel():

    turtle.fillcolor("yellowgreen")



    turtle.begin_fill()

    for k in range(4):

        turtle.forward(PIXEL_SIZE)

        turtle.right(90)

            

    turtle.forward(PIXEL_SIZE) #PIXEL_SIZE

    turtle.end_fill()



def draw_sienna_pixel():

    turtle.fillcolor("sienna")



    turtle.begin_fill()

    for k in range(4):

        turtle.forward(PIXEL_SIZE)

        turtle.right(90)

            

    turtle.forward(PIXEL_SIZE) #PIXEL_SIZE

    turtle.end_fill()



def draw_tan_pixel():

    turtle.fillcolor("tan")



    turtle.begin_fill()

    for k in range(4):

        turtle.forward(PIXEL_SIZE)

        turtle.right(90)

            

    turtle.forward(PIXEL_SIZE) #PIXEL_SIZE

    turtle.end_fill()



def draw_gray_pixel():

    turtle.fillcolor("gray")



    turtle.begin_fill()

    for k in range(4):

        turtle.forward(PIXEL_SIZE)

        turtle.right(90)

            

    turtle.forward(PIXEL_SIZE) #PIXEL_SIZE

    turtle.end_fill()



def draw_darkgray_pixel():

    turtle.fillcolor("darkgreen")



    turtle.begin_fill()

    for k in range(4):

        turtle.forward(PIXEL_SIZE)

        turtle.right(90)

            

    turtle.forward(PIXEL_SIZE) #PIXEL_SIZE





#^^ functions to draw each color when input



turtle.end_fill()





draw()





input("END:")

turtle.down()



