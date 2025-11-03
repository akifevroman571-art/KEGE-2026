from turtle import *
screensize(3000, 3000)
m = 30
tracer(0)
lt(90)
rt(30)
for i in range(3):
    rt(150)
    fd(6* m)
    rt(30)
    fd(12* m)
up()
for x in range(-40, 40):
    for y in range(-40,40):
        goto(x * m, y * m)
        dot(4, 'red')
update()
done()