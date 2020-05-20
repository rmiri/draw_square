import turtle #to make things draw in python

def draw_square():
    window = turtle.Screen()
    window.bgcolor('blue')

    tur = turtle.Turtle()
    tur.shape('turtle')
    tur.color('white','green')
    # tur.speed(2)
    for i in range(36):
        for _ in range(4):
            tur.forward(150)
            tur.right(90)
        tur.right(10+i)
   

    window.exitonclick()

draw_square()