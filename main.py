from tkinter import Tk, Canvas
from math import floor, sin, cos
from random import random, seed


class Main():
    def __init__(self):
        self.root = Tk()
        self.root.title("Bong V.2.0")
        self.paused = False
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry("{}x{}".format(self.width, self.height))
        self.c = Canvas(self.root, width=self.width, height=self.height)
        self.platform = self.c.create_rectangle(self.width / 2 - 52, (self.height - self.height / 6) - 6, self.width / 2 + 52, (self.height - self.height / 6) + 6, fill="#000000")
        self.ball = self.c.create_oval(self.width / 2 - 50, self.height / 2 - 50, self.width / 2 + 50, self.height / 2 + 50, fill="#0000ff", outline="#0000ff")
        seed()
        self.coords = self.c.coords(self.platform)
        angle = str(random())
        angle = angle[2:]
        self.angle = int(angle) % 360
        self.c.pack()
        self.speed = 10
        self.speedx = self.speed
        self.speedy = self.speed
        self.root.bind("<Escape>", self.kr)
        self.root.bind("<Motion>", self.motion)
        self.root.after(16, self.afterloop)
        self.root.mainloop()



    def kr(self, event=None):
        if not self.paused:
            self.paused = True
            self.quit = self.c.create_rectangle(self.width / 2 - 150, self.height / 2 - 25, self.width / 2 + 150, self.height / 2 + 25, fill="#8a8a8a", outline="#8a8a8a", activeoutline="#00ddff")
            self.quittxt = self.c.create_text(self.width / 2, self.height / 2, text="Quit Game.")
            self.c.tag_bind(self.quit, "<Button-1>", lambda e: self.root.destroy())
            self.c.tag_bind(self.quittxt, "<Button-1>", lambda e: self.root.destroy())
        else:
            self.paused = False
            self.c.delete(self.quit)
            self.c.delete(self.quittxt)
            self.afterloop()


    def motion(self, event=None):
        self.coords = self.c.coords(self.platform)
        if not self.paused:
            self.c.coords(self.platform, event.x - 50, self.coords[1], event.x + 50, self.coords[3])


    def afterloop(self):
        self.c.move(self.ball, sin(self.angle) * self.speedx, cos(self.angle) * self.speedy)
        self.bcoords = self.c.coords(self.ball)
        if self.bcoords[0] <= 0 or self.bcoords[2] >= self.width:
           self.speedx *= -1
        elif (self.bcoords[1] <= 0) or ((self.coords[0] <= self.bcoords[0] <= self.coords[2] or self.coords[0] <= self.bcoords[2] <= self.coords[2]) and self.bcoords[3] >= (self.height - self.height / 6) - 6 >= self.bcoords[1]):
            self.speedy *= -1
            if ((self.coords[0] <= self.bcoords[0] <= self.coords[2] or self.coords[0] <= self.bcoords[2] <= self.coords[2]) and self.bcoords[3] >= (self.height - self.height / 6) - 6 >= self.bcoords[1]):
                self.c.coords(self.ball, self.bcoords[0], (self.height - self.height / 6) - 106, self.bcoords[2], (self.height - self.height / 6) - 6)
        if not self.paused:
            self.root.after(16, self.afterloop)

game = Main()
