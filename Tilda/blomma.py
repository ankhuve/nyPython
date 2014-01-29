from turtle import *
from listQfile import *

penup()
setpos(-300,200)
pendown()
w = list(range(50))
q = ListQ()

for i in w:
    q.put(i)

for i in range(200):
    x = q.get()
    forward(x)
    right(45)
    x = q.get()
    q.put(x)
    q.put(x)

right(180)
while not q.isEmpty():
    x = q.get()
    forward(x)
    left(5)
