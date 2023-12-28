from __future__ import annotations

from turtle import begin_fill
from turtle import circle
from turtle import dot
from turtle import end_fill
from turtle import fd
from turtle import fillcolor
from turtle import goto
from turtle import lt
from turtle import mainloop
from turtle import pendown
from turtle import pensize
from turtle import penup
from turtle import Screen
from turtle import seth
from turtle import speed
from turtle import tracer


class Doraemon:
    def __init__(self):
        self.s = Screen()
        self.s.setup(width=1000, height=800)

    @staticmethod
    def my_goto(x, y):
        penup()
        goto(x, y)
        pendown()

    @staticmethod
    def eyes():
        fillcolor('White')
        begin_fill()
        tracer(False)
        a = 2.5
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                lt(3)
                fd(a)
            else:
                a += 0.05
                lt(3)
                fd(a)
        tracer()
        end_fill()

    def beard(self):
        self.my_goto(-32, 135)
        seth(165)
        fd(60)
        self.my_goto(-32, 125)
        seth(180)
        fd(60)
        self.my_goto(-32, 115)
        seth(193)
        fd(60)
        self.my_goto(37, 125)
        seth(15)
        fd(60)
        self.my_goto(37, 125)
        seth(0)
        fd(60)
        self.my_goto(37, 115)
        seth(-13)
        fd(60)

    def mouth(self):
        self.my_goto(5, 148)
        seth(270)
        fd(100)
        seth(0)
        circle(120, 50)
        seth(230)
        circle(-120, 100)

    @staticmethod
    def scarf():
        fillcolor('Red')
        begin_fill()
        seth(0)
        fd(200)
        circle(-5, 90)
        fd(10)
        circle(-5, 90)
        fd(207)
        circle(-5, 90)
        fd(10)
        circle(-5, 90)
        end_fill()

    def nose(self):
        self.my_goto(-10, 158)
        seth(315)
        fillcolor('Red')
        begin_fill()
        circle(20)
        end_fill()

    def pupil(self):
        seth(0)
        self.my_goto(-20, 195)
        fillcolor('black')
        begin_fill()
        circle(13)
        end_fill()
        pensize(6)
        self.my_goto(20, 205)
        seth(75)
        circle(-10, 150)
        pensize(4)
        self.my_goto(-17, 200)
        seth(0)
        fillcolor('White')
        begin_fill()
        circle(5)
        end_fill()
        self.my_goto(0, 0)

    def face(self):
        fd(183)
        lt(45)
        fillcolor('White')
        begin_fill()
        circle(120, 100)
        seth(180)
        fd(121)
        pendown()
        seth(215)
        circle(120, 100)
        end_fill()
        self.my_goto(63.56, 218.24)
        seth(90)
        self.eyes()
        seth(180)
        penup()
        fd(60)
        pendown()
        seth(90)
        self.eyes()
        penup()
        seth(180)
        fd(64)

    @staticmethod
    def head():
        penup()
        circle(150, 40)
        pendown()
        fillcolor('Blue')
        begin_fill()
        circle(150, 280)
        end_fill()

    def start(self):
        self.head()
        self.scarf()
        self.face()
        self.pupil()
        self.nose()
        self.mouth()
        self.beard()

        self.my_goto(0, 0)
        seth(0)
        penup()
        circle(150, 50)
        pendown()
        seth(30)
        fd(40)
        seth(70)
        circle(-30, 270)
        fillcolor('Blue')
        begin_fill()
        seth(230)
        fd(80)
        seth(90)
        circle(1000, 1)
        seth(-89)
        circle(-1000, 10)
        seth(180)
        fd(70)
        seth(90)
        circle(30, 180)
        seth(180)
        fd(70)
        seth(100)
        circle(-1000, 9)
        seth(-86)
        circle(1000, 2)
        seth(230)
        fd(40)
        circle(-30, 230)
        seth(45)
        fd(81)
        seth(0)
        fd(203)
        circle(5, 90)
        fd(10)
        circle(5, 90)
        fd(7)
        seth(40)
        circle(150, 10)
        seth(30)
        fd(40)
        end_fill()

        seth(70)
        fillcolor('White')
        begin_fill()
        circle(-30)
        end_fill()

        self.my_goto(103.74, -182.59)
        seth(0)
        fillcolor('White')
        begin_fill()
        fd(15)
        circle(-15, 180)
        fd(90)
        circle(-15, 180)
        fd(10)
        end_fill()

        self.my_goto(-96.26, -182.59)
        seth(180)
        fillcolor('White')
        begin_fill()
        fd(15)
        circle(15, 180)
        fd(90)
        circle(15, 180)
        fd(10)
        end_fill()

        self.my_goto(-133.97, -91.81)
        seth(50)
        fillcolor('White')
        begin_fill()
        circle(30)
        end_fill()

        self.my_goto(-103.42, 15.09)
        seth(0)
        fd(38)
        seth(230)
        begin_fill()
        circle(90, 260)
        end_fill()

        self.my_goto(5, -40)
        seth(0)
        fd(70)
        seth(-90)
        circle(-70, 180)
        seth(0)
        fd(70)
        self.my_goto(-103.42, 15.09)
        fd(90)
        seth(70)
        fillcolor('Yellow')
        begin_fill()
        circle(-20)
        end_fill()

        seth(170)
        fillcolor('green')
        begin_fill()
        circle(-2, 180)
        seth(10)
        circle(-100, 22)
        circle(-2, 180)
        seth(180 - 10)
        circle(100, 22)
        end_fill()

        goto(-13.42, 15.09)
        seth(250)
        circle(20, 110)
        seth(90)
        fd(15)
        dot(10)
        self.my_goto(0, -150)


if __name__ == '__main__':
    pensize(5)
    speed(10)
    d = Doraemon()
    d.start()
    mainloop()
