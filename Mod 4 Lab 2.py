"""
CTEC 121
<Stephen Guild>
<Mod 4 Lab 2>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from graphics import*
def main():
    '''
    #example of setting own coordinates
    win=GraphWin("demo",800,800)
    win.setCoords(-4.0,-4.0,4.0,4.0)
    p1=Circle(Point(2,3),1)
    p1.setFill("red")
    p1.draw(win)
    p2=Circle(Point(-3,1),1)
    p2.setFill("blue")
    p2.draw(win)
    p3=Circle(Point(-1.5,-2.5),1)
    p3.setFill("black")
    p3.draw(win)

    input()
    '''
    #Tic Tac Toe Grid
    win=GraphWin("Tin-Tac-Toe Grid",600,600)
    win.setCoords(0,0,3,3)

    #draw vertical lines
    Line(Point(1,0),Point(1,3)).draw(win)
    Line(Point(2,0),Point(2,3)).draw(win)

    #draw horizontal lines
    Line(Point(0,1),Point(3,1)).draw(win)
    Line(Point(0,2),Point(3,2)).draw(win)

    input()

main()    