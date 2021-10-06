#File HertzAllissaLab04b.py
import math

import graphics
from graphics import *


def main():
    ###Set the Name of the window
    winName = "Lab 4 - HertzAllissa"
    ###Ask the user what color the circle should be
    color1 = input("What color would you like the circle to be? ")
    ###Ask the user what the x,y coordinates of the circle are
    x1,y1 = eval(input("What are the x,y coordinates of the center of the circle? "))
    ###Ask the user what the radius of the circle is
    radius1 = eval(input("What is the radius of the circle? "))

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
    print(x2, y2)
    ###Draw a green circle
    circ2 = Circle(center2, radius2)
    circ2.setFill(color2)
    circ2.draw(win)

    ###Draw a line from the center of the first circle to the center of the second
    line = Line(center1, center2)
    line.setFill('red')
    line.draw(win)

    while True:
       if win.getMouse():
           # ox, oy = origin
           # px, py = point
           #
           # qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
           # qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
           # return qx, qy

            originX = circ1.getCenter().x;
            originY = circ1.getCenter().y
            pointX = originX + math.cos(math.pi/2) * (circ2.getCenter().x - originX) - math.sin(math.pi/2) * (circ2.getCenter().y - originY)
            pointY = originY + math.sin(math.pi/2) * (circ2.getCenter().x - originX) + math.cos(math.pi/2) * (circ2.getCenter().y - originY)

            circ2.move(pointX - circ2.getCenter().x, pointY - circ2.getCenter().y)
            line.undraw()
            time.sleep(0.1)
            center2 = circ2.getCenter()
            line = Line(center1, center2)
            line.setFill('red')
            line.draw(win)

main()
