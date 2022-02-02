import turtle

wn = turtle.Screen()
wn.title('Tuomon pinkiponki')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Tulos
score_a = 0
score_b = 0



#sivuosa A
sivuosa_a = turtle.Turtle()
sivuosa_a.speed(0)
sivuosa_a.shape("square")
sivuosa_a.color('blue')
sivuosa_a.shapesize(stretch_wid=5, stretch_len=1)
sivuosa_a.penup()
sivuosa_a.goto(-350, 0)
#sivuosa B
sivuosa_b = turtle.Turtle()
sivuosa_b.speed(0)
sivuosa_b.shape("square")
sivuosa_b.color('red')
sivuosa_b.shapesize(stretch_wid=5, stretch_len=1)
sivuosa_b.penup()
sivuosa_b.goto(350, 0)
#Pallo A
pallo = turtle.Turtle()
pallo.speed(0)
pallo.color('white')
pallo.shape('circle')
pallo.penup()
pallo.goto(0, 0)
pallo.dx = 0.2
pallo.dy = 0.2

# Kynä

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))



#liikkumis funktio ylös a 
def sivuosa_a_ylös():
    y = sivuosa_a.ycor()
    y += 20
    sivuosa_a.sety(y)

#liikkumis funktio alas a
def sivuosa_a_alas():
    y = sivuosa_a.ycor()
    y -= 20
    sivuosa_a.sety(y)

#liikkumis funktio ylös b
def sivuosa_b_ylös():
    y = sivuosa_b.ycor()
    y += 20
    sivuosa_b.sety(y)

#liikkumis funktio alas b
def sivuosa_b_alas():
    y = sivuosa_b.ycor()
    y -= 20
    sivuosa_b.sety(y)

# liikkumiset
wn.listen()
wn.onkeypress(sivuosa_a_ylös, "w")
wn.onkeypress(sivuosa_a_alas, "s")
wn.onkeypress(sivuosa_b_ylös, "e")
wn.onkeypress(sivuosa_b_alas, "d")


#Perus peli looppi
while True:
    wn.update()

    #pallo liike

    pallo.setx(pallo.xcor() + pallo.dx)
    pallo.sety(pallo.ycor() + pallo.dy)

    #reunat


    if pallo.ycor() > 290:
        pallo.sety(290)
        pallo.dy *= -1

    if pallo.ycor() < -290:
        pallo.sety(-290)
        pallo.dy *= -1

    if pallo.xcor() > 390:
        pallo.goto(0, 0)
        pallo.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if pallo.xcor() < -390:
        pallo.goto(0, 0)
        pallo.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Sivuosa törmäys oikea
    if (pallo.xcor() > 340 and pallo.xcor() < 350) and (pallo.ycor()) < sivuosa_b.ycor() + 40 and pallo.ycor() > sivuosa_b.ycor() -50:
        pallo.setx(340)
        pallo.dx *= -1

    # Sivuosa törmäys vasen
    if (pallo.xcor() < -340 and pallo.xcor() > -350) and (pallo.ycor()) < sivuosa_a.ycor() + 40 and pallo.ycor() > sivuosa_a.ycor() -50:
        pallo.setx(-340)
        pallo.dx *= -1