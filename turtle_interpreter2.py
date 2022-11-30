'''
Hannah Soria
Professor Wolfe
CS151 fall 2021
Project 9 Shapes and Mosaics
'''

import turtle
import lsystem2 

class TurtleInterpreter:
    turt = turtle.Turtle()
    turtle.hideturtle()
    '''screen'''
    screen = turtle.Screen()
    def __init__(self, width=800, height=800, bgColor='white'):

        self.screen.setup(width = 800, height = 1000)
        self.screen.bgcolor('white')

    def setColor(self, c):
        TurtleInterpreter.turt.pencolor(c)
        TurtleInterpreter.turt.fillcolor(c)
        
    def setWidth(self, w):
        TurtleInterpreter.turt.width(w)

    def goto(self, x, y, heading = None):
        TurtleInterpreter.turt.penup()
        TurtleInterpreter.turt.goto(x,y)
        TurtleInterpreter.turt.pendown()
        if heading != None:
            TurtleInterpreter.turt.setheading(heading)

    def getScreenWidth(self):
        return self.screen.window_width()

    def getScreenHeight(self):
        return self.screen.window_height()

    def getScreen(self):
        return self.screen

 

    turtle.tracer(0)

        
    '''TurtleInterpreter constructor.
    Creates instance variables for a Turtle object and a Screen object with a particular window
    `width`, `height`, and background color `bgColor`.
    '''
    # Create a Turtle object, set it as an instance variable

    # Create a Screen object, set it as an instance variable.
    # Set the screen's height, width, and color based on the parameters

    # Turn the screen's tracer off.


    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        TurtleInterpreter.turt.hideturtle()
        self.screen.update()

        # Close the window when users presses the 'q' key
        self.screen.onkey(turtle.bye, 'q')

        # Listen for the q button press event
        self.screen.listen()

        # Have the turtle listen for a click
        self.screen.exitonclick()



    def drawString(self, lsysString, distance, angle):
        posList = []
        headList = []
        saveList = []
        for char in lsysString:
            if char == "F":
                TurtleInterpreter.turt.forward(distance)
            if char == "+":
                TurtleInterpreter.turt.left(angle)
            if char == "-":
                TurtleInterpreter.turt.right(angle)
            if char == "[":
                posList.insert(0,TurtleInterpreter.turt.position())
                headList.insert(0, TurtleInterpreter.turt.heading())
            if char == "]":
                position = posList.pop(0)
                self.goto(position[0], position[1], headList.pop(0))
            if char == "<":
                saveList.append(TurtleInterpreter.turt.color()[0])
            if char == ">":
                c = saveList.pop(-1)
                TurtleInterpreter.turt.pencolor(c)
            if char == "g":
                TurtleInterpreter.turt.pencolor(0.15, 0.5, 0.2)
            if char == "y":
                TurtleInterpreter.turt.pencolor(0.8, 0.8, 0.3)
            if char == "r":
                TurtleInterpreter.turt.pencolor(0.7, 0.2, 0.3)
            if char == "L":
                TurtleInterpreter.turt.circle(distance/2, 180)
                TurtleInterpreter.turt.left(90)
                TurtleInterpreter.turt.forward(distance/1)
            if char == "B":
                TurtleInterpreter.turt.circle(distance/4)
            if char == '{':
                TurtleInterpreter.turt.begin_fill()
            if char == '}':
                TurtleInterpreter.turt.end_fill()



                '''Interpret each character in an L-system string as a turtle command.

    Here is the starting L-system alphabet:
        F is forward by a certain distance
        + is left by an angle
        - is right by an angleh

    Parameters:
    -----------
    lsysString: str. The L-system string with characters that will be interpreted as drawing
        commands.
    distance: distance to travel with F command.
    angle: turning angle (in deg) for each right/left command.
    '''

    # Walk through the lsysString character-by-character and
    # have the turtle object (instance variable) carry out the
    # appropriate commands

    # Call the update method on the screen object to make sure
    # everything drawn shows up at the very end of the method
    # (remember: you turned off animations in the constructor)