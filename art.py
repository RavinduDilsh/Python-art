import turtle
from turtle import bgcolor, colormode,pencolor

turtle.bgcolor('black') # set a bacground color for the art

def hexagon(): # define the hexagonal spyral function
        colors = ['red', 'green', 'blue', 'pink', 'orange', 'yellow'] #define the colors we want to use
        t = turtle.Pen() # assign pen tool to 't'
        for x in range(300):
                t.pencolor(colors[x%6]) #set a pen color
                t.width(x/60 + 1) # set defaut line width
                t.forward(x) #navigating the pen to go forward
                t.left(59) #navigating the pen to turn left 59 degrees
                

def spyral(): # define the spyral function
        b, g, r = 0, 0, 255
        t = turtle.Pen() # assign pen tool to 't'
        
        for i in range(250*2):
            colormode(255) # set the color mode
    
            if i < 255//3:
                g += 3
            elif i < (255*2)//3:
                r -= 3
            elif i < 255:
                b += 3
            elif i < (255*4)//3:
                g -= 3
            elif i < (255*5)//3:
                r += 3
            else:
                b -= 3
                
        
            t.forward(-25+i+25) # set the art starting point
            t.right(91)
            t.pencolor(r, g, b) #pen colors

hexagon() # calling for hexagonal spyral function
spyral() # calling for spyral function

turtle.getscreen().getcanvas().postscript(file='art.ps') # get the art file into a postscript file
