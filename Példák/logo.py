from turtle import forward, right, speed, mainloop, shape


def polygon(n, l=100):
    for i in range(n):
        forward(l)
        right(360 / n)


shape("turtle")
speed(0)

for i in range(4):
    polygon(4)
    right(90)

mainloop()
