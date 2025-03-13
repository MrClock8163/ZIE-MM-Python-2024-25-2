from turtle import forward, right, speed, mainloop, shape


shape("turtle")
speed(0)

l = 100
n = 10

for i in range(n):
    forward(l)
    right(360 / n)

mainloop()
