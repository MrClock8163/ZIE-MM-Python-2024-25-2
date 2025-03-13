import turtle as t
from math import sqrt
from contextlib import contextmanager


def regular(n: int, a: float):
    for i in range(n):
        t.fd(a)
        t.rt(360/n)


def tree(depth: int, angle: float):
    t.forward(depth * 10)
    if depth > 1:
        t.left(angle)
        tree(depth - 1, angle)
        t.right(2 * angle)
        tree(depth - 1, angle)
        t.left(angle)

    t.back(depth * 10)


def fractal(depth: int, length: float):
    if depth == 0:
        return
    
    newlen = length / 3

    t.penup()
    t.right(45)
    t.forward(newlen * sqrt(2))
    t.left(45)
    t.pendown()
    t.begin_fill()
    regular(4, newlen)
    t.end_fill()
    t.penup()
    t.right(45)
    t.back(newlen * sqrt(2))
    t.left(45)

    if depth <= 1:
        return

    fractal(depth - 1, newlen)
    t.forward(newlen)
    fractal(depth - 1, newlen)
    t.forward(newlen)
    fractal(depth - 1, newlen)
    t.right(90)
    t.forward(newlen)
    t.left(90)
    fractal(depth - 1, newlen)
    t.right(90)
    t.forward(newlen)
    t.left(90)
    fractal(depth - 1, newlen)
    t.back(newlen)
    fractal(depth - 1, newlen)
    t.back(newlen)
    fractal(depth - 1, newlen)
    t.left(90)
    t.forward(newlen)
    t.right(90)
    fractal(depth - 1, newlen)
    t.left(90)
    t.forward(newlen)
    t.right(90)


@contextmanager
def noupdate():
    try:
        t.tracer(0)
        yield
    finally:
        t.update()


def main():
    t.shape("turtle")
    t.left(90)
    t.speed(0)
    
    with noupdate():
        # tree(10, 15)
        L = 400
        regular(4, L)
        fractal(1, L)

    t.mainloop()


if __name__ == "__main__":
    main()
