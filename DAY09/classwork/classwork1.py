from turtle import*

def draw_square():
    for i in range(4):
        forward(100)
        left(90)
def kalmis_wageba(x,y):
    penup()                      #penup- შეჩერება 
    goto(0,200)
    pendown()

draw_square()

  

penup()
goto(-200,200)
pendown()

draw_square()

forward(100)
left(90)


penup()
goto(-200,0)
pendown()


draw_square()
forward(100)
left(90)



exitonclick()


