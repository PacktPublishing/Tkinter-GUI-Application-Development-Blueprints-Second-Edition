"""
Code illustration: 8.01
    Screensaver
Tkinter GUI Application Development Blueprints
"""


from tkinter import Tk, Canvas, BOTH
from random import randint


class RandomBall:

    def __init__(self, canvas):
        self.canvas = canvas
        self.screen_width = canvas.winfo_screenwidth()
        self.screen_height = canvas.winfo_screenheight()
        self.create_ball()

    def create_ball(self):
        self.generate_random_attributes()
        self.create_oval()

    def generate_random_attributes(self):
        self.radius = r = randint(40, 70)
        self.x_coordinate = randint(r, self.screen_width - r)
        self.y_coordinate = randint(r, self.screen_height - r)
        self.x_velocity = randint(6, 12)
        self.y_velocity = randint(6, 12)
        self.color = self.generate_random_color()

    def generate_random_color(self):
        r = lambda: randint(0, 0xffff)
        return '#{:04x}{:04x}{:04x}'.format(r(), r(), r())

    def create_oval(self):
        x1 = self.x_coordinate - self.radius
        y1 = self.y_coordinate - self.radius
        x2 = self.x_coordinate + self.radius
        y2 = self.y_coordinate + self.radius
        self.ball = self.canvas.create_oval(
            x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        self.check_screen_bounds()
        self.x_coordinate += self.x_velocity
        self.y_coordinate += self.y_velocity
        self.canvas.move(self.ball, self.x_velocity, self.y_velocity)

    def check_screen_bounds(self):
        r = self.radius
        if not r < self.y_coordinate < self.screen_height - r:
            self.y_velocity = -self.y_velocity
        if not r < self.x_coordinate < self.screen_width - r:
            self.x_velocity = -self.x_velocity


class ScreenSaver:

    balls = []

    def __init__(self, number_of_balls):
        self.root = Tk()
        self.number_of_balls = number_of_balls
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.1)
        self.root.wm_attributes('-alpha',0.1)
        self.quit_on_interaction()
        self.create_screensaver()
        self.root.mainloop()

    def create_screensaver(self):
        self.create_canvas()
        self.add_balls_to_canvas()
        self.animate_balls()

    def create_canvas(self):
        self.canvas = Canvas(self.root)
        self.canvas.pack(expand=1, fill=BOTH)

    def add_balls_to_canvas(self):
        for i in range(self.number_of_balls):
            self.balls.append(RandomBall(self.canvas))

    def quit_on_interaction(self):
        for seq in ('<Any-KeyPress>', '<Any-Button>', '<Motion>'):
            self.root.bind(seq, self.quit_screensaver)

    def animate_balls(self):
        for ball in self.balls:
            ball.move_ball()
        self.root.after(30, self.animate_balls)

    def quit_screensaver(self, event):
        self.root.destroy()

if __name__ == "__main__":
    ScreenSaver(number_of_balls=18)
