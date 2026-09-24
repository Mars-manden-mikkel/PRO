import turtle
t = turtle.Turtle()
t.speed(2)
t.right(50)

#højre klunk
for i in range(26):
  t.forward (10)
  t.right(10)
t.left(180)

#Venstreklunk
for i in range(26):
  t.forward (10)
  t.right(10)
for i in range(10):
  t.left(5)
  t.forward(5)

#shaft.left
t.left(31)
t.forward(250)

#Head
x = 56
t.right(90)
t.forward(x)
t.right(180)
t.forward(x)

#Tip
t.right(90)
for i in range(45):
  t.forward(1)
  t.right(2)
t.right(90)
t.forward(25)
t.back(25)
t.left(90)
for i in range(45):
  t.forward(1)
  t.right(2)

#shaft.right
t.forward(220)
for i in range(12):
  t.left(5)
  t.forward(5)
t.forward(10)

turtle.done() 
