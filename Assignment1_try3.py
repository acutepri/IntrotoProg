import turtle

def drawcrown():
    """
    Draw turtle shaped turtles with increasing in numbers in a circle
    :return: none
    """
    # Initialise the number of turtles stamp in the beginning
    num_turtle = 6
    # Initialise the increasing count of turtle terra
    terra_count = 7
    # Initialise the distance of terra from the center of the circle
    terra_distance = 25
    terra.penup()  # Picks up the turtle
    terra.pencolor("black")  # Sets the outline of terra to black

    # The 4 colours of the turtle
    for colour in ["red", "yellow", "light green", "orange"]:
        terra.fillcolor(colour)
        terra.begin_fill()
        # Print out the turtles starting with 6 turtles and ending with 24 turtles
        for size in range(num_turtle):
            terra.begin_fill()
            terra.forward(terra_distance)
            terra.stamp()
            terra.forward(-terra_distance)
            terra.right(360 / num_turtle)
        terra.end_fill()
        terra.fillcolor("yellow")
        # Formula to increase the number of turtles
        num_turtle = num_turtle + terra_count
        terra_count = terra_count - 1
        # Moves the turtle forward after each circle finishes
        terra_distance = terra_distance + 25

def drawstem():
    """
    Draw a rectangular stem
    :return: None
    """
    tess.penup()
    tess.goto(-50, -120)  # Initialise tess's position
    tess.pendown()
    tess.fillcolor("green")  # Initialise tess's fillcolor
    tess.begin_fill()
    # Loop to draw a rectangular stem
    for stem_sides in range(2):
        tess.forward(100)
        tess.right(90)
        tess.forward(300)
        tess.right(90)
    tess.end_fill()

def drawpetals(colour_select):
    """
    Draw out 12 rectangular petals 4 times with 4 different colours
    :param colour_select: Select a colour from the 4 colours listed
    :return: none
    """
    # Initialise the rectangle length and width
    rec_length = 200
    rec_width = 37.5
    # Draw 12 rectangular petals
    for i in range(12):
        tito.up()
        tito.forward(100)
        tito.pendown()
        tito.fillcolor(colour_select)  # Select colours from the string colours
        tito.begin_fill()
        # Draw 1 rectangle
        for n in range(2):
            tito.forward(rec_length)
            tito.left(90)
            tito.forward(rec_width)
            tito.left(90)
        tito.end_fill()
        tito.penup()  # Picks up the turtle
        tito.goto(0, 0)  # Go to starting position of the circle
        tito.left(30)  # turns 30 degree (360/12)


# Initialise the turtle screen
wn = turtle.Screen()
wn.setup(width=1920, height=1080, startx=0, starty=0)  # setting the width/length of the screen
wn.bgcolor("white")
tito = turtle.Turtle()  # Create a turtle called tito
terra = turtle.Turtle()  # Create a turtle called terra
tess = turtle.Turtle()
tito.pensize(1)  # Sets tito pensize to 1
tito.speed(10)  # Increase tito's speed
terra.shape("turtle")  # Set terra's shape to "turtle"

angle = 0  # Initialise starting angle

colours = ["light green", "orange", "red", "yellow"]  # String to store the petal colours
total_colours = len(colours)  # Length of the string colours

# Draw the crown of the flower
drawcrown()

# Draw the stem of the flower
drawstem()

# Draw the flower petals
for num in range(4):
    tito.setheading(0)  # Set the turtle heading to face North
    tito.up()
    tito.left(angle)  # Turns the turtle by 0 degree first
    tito.down()
    drawpetals(colours[num%total_colours])  # Cycle thru the colours
    angle = angle + 7.5  # Turns the turtle by 7.5 degree


wn.exitonclick()