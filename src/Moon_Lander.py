#Problem_A
import turtle
import math
import random


class Lander(turtle.Turtle):
    '''
    Purpose: An object falling towards the moon’s surface
    Instance variables:
        x: The starting x position for the lander
        y: The starting y position for the lander
        self.vx: The starting x velocity
        self.vy: The starting y velocity
        self.fuel: The fuel remaining for our lander
    Methods:
        __init__(self, x, y, vx, vy): Constructor to make instance variables
        move(self): Moves the Lander to a new position each step, based on its current velocity
        thrust(self): Increases velocity in whatever direction its currently pointing
        Left(self): Makes the Lander turns left 10 degrees
        Right(self): Makes the Lander turns right 10 degrees
    '''
    def __init__(self, x, y, vx, vy):
        turtle.Turtle.__init__(self)
        self.vx = vx
        self.vy = vy
        self.fuel = 50
        self.penup()
        self.speed(0)
        self.left(90)
        self.setpos(x, y)

    def move(self):
        self.vy -= 0.0486
        self.setpos(self.xcor()+self.vx, self.ycor()+self.vy)

    def thrust(self):
        print('Up button pressed')
        if self.fuel > 0:
            self.fuel -= 1
            self.vx += math.cos(math.radians(self.heading()))
            self.vy += math.sin(math.radians(self.heading()))
            print('Remaining fuel:',self.fuel)

        else:
            print('Out of fuel')

    def Left(self):
        print('Turn left button pressed')
        if self.fuel > 0:
            self.fuel -= 1
            self.left(10)
            print('Remaining fuel:',self.fuel)

        else:
            print('Out of fuel')

    def Right(self):
        print('Turn right button pressed')
        if self.fuel > 0:
            self.fuel -= 1
            self.right(10)
            print('Remaining fuel:',self.fuel)

        else:
            print('Out of fuel')



class Game:
    '''
    Purpose: It is responsible for keeping the game running, keeping track of the meteors...
    Instance variables:
        self.player: Creates a Lander object to be controlled by the player
        self.meteors: Creates a meteors list that has maximum number limit
        self.max_meteors: Maximum number limit of meteors in the list
        self.tick: Records the number of gameloops
    Methods:
        __init__(self): Constructor to make instance variables
        gameloop(self): Game gets the loop or stop in some conditions

    '''
    def __init__(self):
        turtle.setworldcoordinates(0, 0, 1000, 1000)
        turtle.delay(0)
        self.player = Lander(random.uniform(100, 900), random.uniform(500, 900), random.uniform(-5, 5), random.uniform(-5, 0))
        self.player.turtlesize(2)
        self.meteors = []
        self.max_meteors = 10
        self.tick = 0
        self.gameloop()
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.Left, 'Left')
        turtle.onkeypress(self.player.Right, 'Right')
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        if self.tick % 3 == 0 and len(self.meteors) < self.max_meteors:
            self.meteors.append(Meteor())

        new_metrors = []
        for m in self.meteors:
            if (self.player.ycor()-m.ycor())**2 + (self.player.xcor()-m.xcor())**2 <= 400:
                print("You crashed!")
                return
            if not m.is_end():
                new_metrors.append(m)
            m.move()
        self.meteors = new_metrors

        if self.player.ycor() < 10:
            if abs(self.player.vx) < 3 and abs(self.player.vy) < 3:
                print('Successful landing!')
            else:
                print('You crashed!')
            return
        self.player.move()
        turtle.Screen().ontimer(self.gameloop, 30)
        self.tick += 1

class Meteor(turtle.Turtle):
    '''
    Purpose: An object represents meteor above the moon
    Instance variables:
        self.vx: The starting x velocity
        self.vy: The starting y velocity
    Methods:
        __init__(self): Constructor to make instance variables
        move(self): Moves the meteor to a new position each step, based on gravity
        is_end(self): Checks if the meteor has fallen to the bottom
    '''
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.vx = random.uniform(-10, 10)
        self.vy = random.uniform(-20, -10)
        self.penup()
        self.speed(0)
        self.color('red')
        self.shape('circle')
        self.setpos(random.uniform(0, 1000), 1000)

    def move(self):
        self.vy -= 0.0486
        self.setpos(self.xcor()+self.vx, self.ycor()+self.vy)

    def is_end(self):
        return self.ycor() < -15

Game()
