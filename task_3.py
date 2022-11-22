import turtle

def mountain(n):
  turtle.left(60)
  turtle.forward(n * 60)
  turtle.right(120)
  turtle.forward((n * 60) / 3)
  turtle.left(20)
  turtle.forward(n * 5)
  turtle.left(40)
  turtle.forward(n * 5)
  turtle.left(30)
  turtle.forward(n * 6)
  turtle.right(80)
  turtle.forward(n * 45)
  turtle.backward(n * 45)
  turtle.right(20)
  turtle.forward(n * 20)
  turtle.left(10)
  turtle.forward(n * 10)
  turtle.right(20)
  turtle.forward(n * 5)
  turtle.left(25)
  turtle.forward(n *10)
  turtle.penup()
  turtle.home()
  turtle.left(60)
  turtle.forward(n * 60)
  turtle.pendown()
  turtle.right(140)
  turtle.forward(n * 25)
  turtle.left(15)
  turtle.forward(n * 5)
  turtle.right(30)
  turtle.forward(n * 10)
  turtle.left(30)
  turtle.forward(n * 20)
