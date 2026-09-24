import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.forward(100)
for i in range(26):
  t.forward (10)
  t.right(10)
t.forward (30)
for i in range(8):
  t.left(10)
  t.forward(2)
t.forward(100)
for i in range(22):
  t.right(8)
  t.forward(2)
t.forward(75)