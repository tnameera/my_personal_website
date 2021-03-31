# Draw n-rayed fractal star using recursion
# Language: Python 3.8
# Author: Syeda Nameera Tahseen
# Date: 03/30/2021


import sys 
from turtle import *

def star(turtle, n,r):
  """ draw a star of n rays of length d"""
  for k in range(0,n):
    turtle.pendown()
    turtle.forward(r)
    turtle.penup()
    turtle.backward(r)
    turtle.left(360/n)

f = 0.3  # rescaling factor
    
def recursive_star(turtle, n, r, depth):
  """At each point of the star, draw another smaller star,
  and so on, up to given depth.  Rescale the stars by a factor f
  at each generation."""
  global f
  if depth == 0:
    star(turtle, n, f*4)
  else:
    for k in range(0,n):
      turtle.pendown()
      turtle.forward(r)
      recursive_star(turtle, n, f*r, depth - 1)
      turtle.penup()
      turtle.backward(r)
      turtle.left(360/n)

def saveImage(turtle, filename):
  """Save turtle graphics drawing to eps file."""
  ts = turtle.getscreen()
  tc = ts.getcanvas()
  tc.postscript(file=filename)
 
fred = Turtle()
fred.speed("fastest")

# Draw a fractal star of depth sys.argv[2] with sys.argv[1] rays:
recursive_star(fred, 3, 200, 3)
fred.hideturtle()


saveImage(fred,"snowflake.eps")

exitonclick()  
    