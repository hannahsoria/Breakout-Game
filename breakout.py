'''Hannah Soria
CS151 Fall 2021
Professor Wolfe
Project11: Game
'''

import turtle
import turtle_interpreter2 as ti

class Game:
    def __init__(self, screenWidth = 800, screenHeight = 800):
        '''This init function has been modified to actually be the start screen. here the start screen is shown with a title and instructions. When the space bar is pressed the game starts'''
        self.title2 = turtle.Turtle()
        self.title2.hideturtle()
        self.title2.penup()
        self.terp = ti.TurtleInterpreter()
        self.terp.turt.hideturtle()
        self.terp.turt.penup()
        self.title = turtle.Turtle()
        self.title.hideturtle()
        self.title.penup()
        self.screen = self.terp.getScreen()
        self.screen.screensize(screenWidth, screenHeight, "brown4")
        self.screen.title("WELCOME")
        self.title.color('white')
        self.title.goto(0, 50)
        self.title.write("BREAKOUT", True, "center", ('Impact', 170, "bold"))
        self.title.goto(0, -150)
        self.title.write("Instructions: Press the left and right arrow to \nstop the ball from leaving the screen. Break all the Blocks. \nYou score a point per broken block. Your score will quickly \nflash when each point is scored. After the blocks are all broken follow \ninstructions to go to the next level. DO NOT do instructions early or you will \nmiss points. Press Space to Start!", True, "center", ('Impact', 25, "bold"))
        self.setUpEvents()

    def startGame(self, screenWidth = 800, screenHeight = 800):
        '''This function is the first level of the game. In this function the blocks are created to the screen and the paddle is created then the ball begins moving
        The ball bounces off walls and blocks and the paddle. The paddle moves with left and right arrow key presses.'''
        self.terp = ti.TurtleInterpreter()
        self.title.clear()
        self.title2.clear()
        self.screen.screensize(screenWidth, screenHeight, "DarkSlateBlue")
        self.screen.title("BREAKOUT")
        self.title4 = turtle.Turtle()
        self.title4.hideturtle()
        self.title4.penup()
        self.title4.goto(0,350)
        self.title4.color('black')
        self.title4.write("LEVEL 1", True, "center", ('Impact', 40, "bold"))
        self.title4.goto(0,-370)
        self.title4.color('black')
        self.title4.write("Press 2 to Advance to level 2 once all the blocks are gone", True, "center", ('Impact', 30, "bold"))
        self.player = self.makePlayer()
        self.distance = 10
        self.blocks = self.makeBlocks(-305,300, 4, 1)
        self.ball = self.makeBall()
        self.move = self.moveBall()
        self.collision = 30
        self.scoreStart = 0
        self.setUpEvents()
        if len(self.blocks) == 0:
            self.title3 = turtle.Turtle()
            self.title3.write("Press 2 to play Level", True, "center", ('Impact', 60, "bold"))
        

    def levelTwo(self, screenWidth = 800, screenHeight = 800):
        '''This is the secind level of the game. In the level 8 new blocks are drawn to the screen. The walls , collisions, and paddle is used the same as level 1.'''
        self.terp = ti.TurtleInterpreter()
        self.screen.screensize(screenWidth, screenHeight, "DarkSalmon")
        self.screen.title("BREAKOUT LEVEL 2")
        self.title4.clear()
        self.title.goto(0,300)
        self.title.write("LEVEL 2", True, "center", ('Impact', 40, "bold"))
        self.blocks = self.makeBlocks(-300, 200, 4, 2)
        self.distance = 10
        self.collision = 30
        self.setUpEvents()
    

    def gameOver(self, screenWidth = 800, screenHeight = 800):
        '''This function is the screen that is shown when the ball exits the bottom of the screen. On this screen you are shown intructions to
        rerun the game. When the return key is clicked you are taken back to level one. The total score is also displayed'''
        turtle.clearscreen()
        self.terp = ti.TurtleInterpreter()
        self.terp.turt.hideturtle()
        self.terp.turt.penup()
        self.setUpEvents()
        self.screen = self.terp.getScreen()
        self.screen.screensize(screenWidth, screenHeight, "black")
        self.screen.title("GAME OVER")
        self.title2.goto(0, 100)
        self.title2.color('CadetBlue')
        self.title2.write("GAME OVER", True, "center", ('Impact', 100, "bold"))
        self.title2.goto(0,0)
        self.title2.write(" Want to play again? Press Return key", True, "center", ('Impact', 40, "bold"))
        self.title2.goto(0,-100)
        self.title2.write('FINAL SCORE:' + str(self.scoreStart), True, "center", ('Impact', 30, "bold"))
        print('gameover') 

    def play(self):
        '''This function keeps the game running wihtout closing the window'''
        self.screen.tracer(True)
        self.screen.listen()
        self.screen.mainloop()

    def setUpEvents(self):
        '''this function defines key presses and what they do/where they go. This function also checks the collisions every 50 milliseconds'''
        self.screen.onkeypress(self.moveRight, "Right")
        self.screen.onkeypress(self.moveLeft, "Left")
        self.screen.onkeypress(self.startGame, "space")
        self.screen.onkeypress(self.levelTwo, "2")
        self.screen.onkeypress(self.startGame, "Return")

        self.screen.ontimer(self.checkCollisions1, 50)
        
    def placePlayer(self, turt):
        '''This function places the player onto the screen'''
        turt.goto(0, -300)

    def makePlayer(self):
        '''This function creates the player which is a long black rectangle'''
        player = turtle.Turtle()
        player.penup()
        player.turtlesize(1,4)
        self.placePlayer(player)
        player.shape('square')
        player.setheading(0)
        return player

    def makeBlocks(self, x, y, row, col):
        '''This function creates the blocks for level 1 using a nested for loop so that they are created in a grid formation. The blocks are added to a list'''
        blocks = []
        for i in range (row):
            for j in range (col):
                block = turtle.Turtle()
                block.turtlesize(2,8)
                block.shape('square')
                block.color('white')
                block.penup()
                block.goto((x + (i *200)), (y + (j *50)))
                blocks.append(block)
        return blocks

    def makeBall(self):
        '''This function creates the ball and make it a star gif. This star is credited to https://www.baamboozle.com/game/118647'''
        self.dx = 2
        self.dy = 5
        ball = turtle.Turtle()
        self.screen.register_shape('star.gif')
        ball.shape('star.gif')
        ball.penup()
        ball.setheading(45)
        ball.goto(0,0)
        return ball

    def moveBall(self):
        ''' This function moves the ball. When the ball runs into either side or the top the direction is changed 
        to look as if it is actually bouncing off the wallas it would in real life. If the ball leaves the screen 
        on the bottom you gameOver function is called.'''
        ballXcor = self.ball.xcor()
        ballYcor = self.ball.ycor()
        winW, winH = self.screen.screensize()
        if ballXcor > winW/2 or ballXcor < -winW/2:
            self.dx = -self.dx
        if ballYcor > winH/2:
            self.dy = -self.dy
        if ballYcor < -winH/2:
            self.gameOver()
            return
        self.ball.goto(ballXcor + self.dx, ballYcor + self.dy)
        self.screen.ontimer(self.moveBall, 20)

    def checkCollisions1(self):
        ''' This function checks to see if the star collides with a block. If it collides with a block the block disappears and is
        added to a list. Once the list = 0 levelTwo is called. Also, every time the block is hit the score goes up one.'''
        ballXcor = self.ball.xcor()
        ballYcor = self.ball.ycor()
        playerXcor = self.player.xcor()
        playerYcor = self.player.ycor()

        if ballXcor > playerXcor - 40 and ballXcor < playerXcor + 40 and ballYcor > playerYcor - 10 and ballYcor < playerYcor + 10:
            self.dy = -self.dy

        blocksDelete = []
        for i in self.blocks:
            block_x = i.xcor()
            block_y = i.ycor()
            ballXcor = self.ball.xcor()
            ballYcor = self.ball.ycor()
            
            if ballXcor > block_x - 80 and ballXcor < block_x + 80 and ballYcor > block_y - 20 and ballYcor < block_y +20:
                self.dy = -self.dy
                self.scoreStart = self.scoreStart + 1
                print(self.scoreStart)
                self.title = turtle.Turtle()
                self.title.hideturtle()
                self.title.penup()
                self.title.write('Score:' + str(self.scoreStart), True, "center", ('Bebas Neue', 30, "bold"))
                self.title.clear()
                i.penup()
                i.hideturtle()
                blocksDelete.append(i)
                i.goto(500,500)
                
        for block in blocksDelete:
            self.blocks.remove(block)

        self.screen.ontimer(self.checkCollisions1, 20)

    def moveRight(self):
        '''This function moves the padde right'''
        self.player.setheading(0)
        self.player.forward(self.distance)

    def moveLeft(self):
        '''This function moves the padde right'''
        self.player.backward(self.distance)  

if __name__ == '__main__':
    game = Game()
    game.play()