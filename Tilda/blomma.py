from turtle import *
from LinkedQ import *

penup()
setpos(-300,200)
pendown()
w = list(range(50))
q = Queue()

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
while not q.empty():
    x = q.get()
    forward(x)
    left(5)
