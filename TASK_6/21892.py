from turtle import *
screensize(3000, 3000)
m = 20
tracer(0)

rt(90)
for i in range(7):
    rt(45)
    fd(11 * m)
    rt(45)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()
#  считать в ручную
print(113)
