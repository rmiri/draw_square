import turtle #to make things draw in python

def draw_square():
    window = turtle.Screen()
    window.bgcolor('blue')

    tur = turtle.Turtle()
    for _ in range(4):
        tur.forward(100)
        tur.right(90)
   

    window.exitonclick()

draw_square()