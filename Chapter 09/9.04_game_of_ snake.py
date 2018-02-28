"""
Code illustration: 9.04
    Game of Snake
Tkinter GUI Application Development Blueprints
"""
import threading
import queue
import random
import time
from tkinter import Tk, Canvas, Button


class View(Tk):

    def __init__(self, queue):
        Tk.__init__(self)
        self.queue = queue
        self.create_gui()
        self.queue_handler()

    def create_gui(self):
        self.canvas = Canvas(self, width=495, height=305, bg='#FF75A0')
        self.canvas.pack()
        self.snake = self.canvas.create_line(
            (0, 0), (0, 0), fill='#FFCC4C', width=10)
        self.food = self.canvas.create_rectangle(
            0, 0, 0, 0, fill='#FFCC4C', outline='#FFCC4C')
        self.points_earned = self.canvas.create_text(
            455, 15, fill='white', text='Score: 0')

    def queue_handler(self):
        try:
            while True:
                task = self.queue.get_nowait()
                if 'game_over' in task:
                    self.game_over()
                elif 'move' in task:
                    points = [x for point in task['move'] for x in point]
                    self.canvas.coords(self.snake, *points)
                elif 'food' in task:
                    self.canvas.coords(self.food, *task['food'])
                elif 'points_earned' in task:
                    self.canvas.itemconfigure(
                        self.points_earned, text='Score: {}'.format(task['points_earned']))
                self.queue.task_done()
        except queue.Empty:
            self.after(100, self.queue_handler)

    def game_over(self):
        self.canvas.create_text(200, 150, fill='white', text='Game Over')
        quit_button = Button(self, text='Quit', command=self.destroy)
        self.canvas.create_window(200, 180, anchor='nw', window=quit_button)


class Food:

    def __init__(self, queue):
        self.queue = queue
        self.generate_food()

    def generate_food(self):
        x = random.randrange(5, 480, 10)
        y = random.randrange(5, 295, 10)
        self.position = (x, y)
        rectangle_position = (x - 5, y - 5, x + 5, y + 5)
        self.queue.put({'food': rectangle_position})


class Snake(threading.Thread):
    is_game_over = False

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.daemon = True
        self.points_earned = 0
        self.snake_points = [
            (495, 55), (485, 55), (475, 55), (465, 55), (455, 55)]
        self.food = Food(queue)
        self.direction = 'Left'
        self.start()

    def run(self):
        while not self.is_game_over:
            self.queue.put({'move': self.snake_points})
            time.sleep(0.1)
            self.move()

    def on_keypress(self, e):
        self.direction = e.keysym

    def move(self):
        new_snake_point = self.calculate_new_coordinates()
        if self.food.position == new_snake_point:
            self.points_earned += 1
            self.queue.put({'points_earned': self.points_earned})
            self.food.generate_food()
        else:
            self.snake_points.pop(0)
        self.check_game_over(new_snake_point)
        self.snake_points.append(new_snake_point)

    def calculate_new_coordinates(self):
        last_x, last_y = self.snake_points[-1]
        if self.direction == 'Up':
            new_snake_point = (last_x, last_y - 10)
        elif self.direction == 'Down':
            new_snake_point = (last_x, last_y + 10)
        elif self.direction == 'Left':
            new_snake_point = (last_x - 10, last_y)
        elif self.direction == 'Right':
            new_snake_point = (last_x + 10, last_y)
        return new_snake_point

    def check_game_over(self, snake_point):
        x, y = snake_point
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.is_game_over = True
            self.queue.put({'game_over': True})


def main():
    q = queue.Queue()
    gui = View(q)
    snake = Snake(q)
    for key in ("Left", "Right", "Up", "Down"):
        gui.bind("<Key-{}>".format(key), snake.on_keypress)
    gui.mainloop()

if __name__ == '__main__':
    main()
