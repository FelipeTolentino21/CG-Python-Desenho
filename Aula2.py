import turtle as tr

tr.bgcolor(235/255, 255/255, 254/255)

tr.speed(15)

tr.pensize(5)

# CHÃO
tr.goto(-1000,0)
tr.color(0/255,110/255,22/255)

tr.begin_fill()
tr.forward(2000)
tr.right(90)
tr.forward(2000)
tr.right(90)
tr.forward(2000)
tr.right(90)
tr.forward(2000)
tr.right(90)
tr.end_fill()


# CASA
tr.goto(0,0)

tr.color(99/255, 82/255, 60/255)

tr.begin_fill()

tr.forward(200)
tr.left(90)
tr.forward(200)
tr.left(90)
tr.forward(200)
tr.left(90)
tr.forward(200)

tr.color(186/255, 148/255, 99/255)

tr.end_fill()

# VOLTA
tr.penup()
tr.backward(200)
tr.left(180)
tr.pendown()

# TELHADO
tr.color(158/255, 0/255, 0/255)

tr.begin_fill()

tr.right(30)
tr.forward(200)
tr.right(120)
tr.forward(200)
tr.right(120)
tr.forward(200)

tr.color(181/255, 47/255, 47/255)

tr.end_fill()

# VOLTA PRA PORTA
tr.penup()
tr.goto(0,0)
tr.right(180)
tr.forward(75)
tr.left(90)
tr.pendown()

# PORTA
tr.color(82/255, 60/255, 27/255)

tr.begin_fill()

tr.forward(90)
tr.right(90)
tr.forward(50)
tr.right(90)
tr.forward(90)
tr.right(90)
tr.forward(50)

tr.color(140/255, 112/255, 76/255)

tr.end_fill()

# JANELA 2
tr.penup()
tr.goto(15,110)
tr.left(180)
tr.pendown()

tr.color(82/255, 60/255, 27/255)

tr.begin_fill()

tr.forward(50)
tr.left(90)
tr.forward(50)
tr.left(90)
tr.forward(50)
tr.left(90)
tr.forward(50)

tr.color(212/255, 255/255, 254/255)

tr.end_fill()

# JANELA 2
tr.penup()
tr.goto(135,110)
tr.left(180)
tr.pendown()
tr.right(90)

tr.color(82/255, 60/255, 27/255)

tr.begin_fill()

tr.forward(50)
tr.left(90)
tr.forward(50)
tr.left(90)
tr.forward(50)
tr.left(90)
tr.forward(50)

tr.color(212/255, 255/255, 254/255)

tr.end_fill()

# CRUZ DA JANELA 2
tr.color(82/255, 60/255, 27/255)

tr.left(90)
tr.forward(25)
tr.left(90)
tr.forward(50)
tr.penup()
tr.goto(135,110)
tr.pendown()
tr.forward(25)
tr.right(90)
tr.forward(50)

# CRUZ DA JANELA 1
tr.penup()
tr.goto(15,110)
tr.pendown()
tr.forward(25)
tr.left(90)
tr.forward(50)
tr.penup()
tr.goto(15,110)
tr.pendown()
tr.forward(25)
tr.right(90)
tr.forward(50)

# MAÇANETA
tr.penup()
tr.goto(115,50)
tr.color(235/255, 235/255, 59/255)
tr.pendown()
tr.circle(1)

# CHAMINÉ
tr.color(158/255, 0/255, 0/255)

tr.penup()
tr.goto(200,200)
tr.left(120)
tr.forward(50)
tr.right(30)
tr.pendown()

tr.begin_fill()

tr.forward(100)
tr.left(90)
tr.forward(35)
tr.left(90)
tr.forward(35)

tr.color(181/255, 47/255, 47/255)

tr.end_fill()

tr.speed(2)

# VOLTA 2
tr.color("gray")
tr.penup()
tr.backward(35)
tr.left(90)
tr.forward(17.5)
tr.left(90)
tr.forward(30)
tr.right(90)
tr.pendown()
tr.begin_fill()
tr.circle(10)
tr.end_fill()
tr.penup()
tr.left(45)
tr.forward(10)
tr.right(45)
tr.pendown()
tr.begin_fill()
tr.circle(10)
tr.end_fill()
