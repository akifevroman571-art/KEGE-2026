print(12*14/2)
from turtle import *
screensize(3000, 3000)
tracer(0)
m = 15
rt(90)
for i in range(2):
    fd(8 * m)
    rt(120)
rt(120)
for i in range(2):
    rt(120)
    fd(3 * m)
    rt(240)
rt(240)
for i in range(2):
    fd(14  * m)
    rt(120)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x  * m, y * m)
        dot(3, 'red')
update()
done()
