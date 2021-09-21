#File HertzAllissaLab04b.py

import graphics
from graphics import *

def main():
    ###Set the Name of the window
    winName = "Lab 4 - HertzAllissa"
    ###Ask the user what color the circle should be
    color1 = 'blue'
    ###Ask the user what the x,y coordinates of the circle are
    x1,y1 = 100,100
    ###Ask the user what the radius of the circle is
    radius1 = 20

    ###Create a 500x500 window with the title "Lab 4 - HertzAllissa"
    win = GraphWin(winName, 500, 500)
    ###Create the center of the first circle
    center1 = Point(x1, y1)
    print(center1)
    ###Create the first circle around the center point
    circ1 = Circle(center1, radius1)
    ###Fill the circle with the color that the user selected
    circ1.setFill(color1)
    ###Draw the circle in the window
    circ1.draw(win)

    ###Assign the radius as half of the radius of the first circle
    radius2 = (1/2 * radius1)
    ###Assign the color as green
    color2 = 'green'
    ###The distance from the center of the first circle to the center
    ###of the second circle is twice the radius of the first circle
    x2 = x1
    y2 = y1-(2*radius1)
    center2 = Point(x2, y2)
    print(center2)
    ###Draw a green circle
    circ2 = Circle(center2, radius2)
    circ2.setFill(color2)
    circ2.draw(win)

    ### we have 2 circles, the next thing to do is to draw a line between the centers of them
    ### recall that center1 is the center of the 1st circle, and center2 is the center of the 2nd
    line = Line(center1, center2)
    ### set the color of the line to be red
    line.setFill('red')
    ### draw the line
    line.draw(win)

    ### this statement has the computer wait for a mouse click from the user.
    ### on some systems this may only work with a left or a right mouse click
    win.getMouse()
    
    ### this loop will now move the circle 
    for i in range (1):
        ### ???
        circ2.move(40, 40)
        ### this gets rid of the line…it doesn’t have to be in the loop!
        line.undraw()
        ### tell the computer to pause so that we can see the circle moving
        time.sleep(2)

    ### once we are done with the movement, query the center of the moved circle
    center2 = circ2.getCenter()
    print(center2)

    ### draw a new line from the center of the first cicle to the center of the new circle.  
    line = Line(center1, center2)
    line.setFill('red')
    line.draw(win)

        ### this loop will now move the circle 
    for i in range (1):
        ### ???
        circ2.move(-40, 40)
        ### this gets rid of the line…it doesn’t have to be in the loop!
        line.undraw()
        ### tell the computer to pause so that we can see the circle moving
        time.sleep(2)

    ### once we are done with the movement, query the center of the moved circle
    center2 = circ2.getCenter()
    print(center2)

    ### draw a new line from the center of the first cicle to the center of the new circle.  
    line = Line(center1, center2)
    line.setFill('red')
    line.draw(win)

            ### this loop will now move the circle 
    for i in range (1):
        ### ???
        circ2.move(-40, -40)
        ### this gets rid of the line…it doesn’t have to be in the loop!
        line.undraw()
        ### tell the computer to pause so that we can see the circle moving
        time.sleep(2)

    ### once we are done with the movement, query the center of the moved circle
    center2 = circ2.getCenter()
    print(center2)

    ### draw a new line from the center of the first cicle to the center of the new circle.  
    line = Line(center1, center2)
    line.setFill('red')
    line.draw(win)

main()


    









    


    

    
