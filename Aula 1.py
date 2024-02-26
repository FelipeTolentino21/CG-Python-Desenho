import turtle as tr

"""tr.bgcolor('black')"""
tr.pensize(5)
tr.speed(200)

i = 0

for i in range (3):
    if (i == 0):
        tr.color('blue')
    elif (i == 1):
        tr.color('black')
    elif (i == 2):
        tr.color('red')
    tr.circle(50)
    tr.penup()
    tr.forward(120)
    tr.pendown()
    

tr.penup()
tr.backward(360)
tr.right(45)
tr.forward(90)
tr.left(45)
tr.pendown()

for i in range (2):
    if (i == 0):
        tr.color('yellow')
    elif (i == 1):
        tr.color('green')
    tr.circle(50)
    tr.penup()
    tr.forward(120)
    tr.pendown()

"""
sides = 6
angle = 360/sides
for i in range(sides):
    tr.forward(100)
    tr.left(angle)
"""
