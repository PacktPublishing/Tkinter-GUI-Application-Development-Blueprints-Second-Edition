"""
Code illustration: 9.01
    Race Condition Demo
Tkinter GUI Application Development Blueprints
"""

import threading


class RaceConditionDemo:

    def __init__(self):
        self.shared_var = 0
        self.total_count = 100000
        self.demo_of_race_condition()

    def increment(self):
        for i in range(self.total_count):
            self.shared_var += 1

    def decrement(self):
        for i in range(self.total_count):
            self.shared_var -= 1

    def demo_of_race_condition(self):
        t1 = threading.Thread(target=self.increment)
        t2 = threading.Thread(target=self.decrement)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("value of shared_var after all increments & decrements :",
              self.shared_var)

if __name__ == "__main__":
    for i in range(100):
        RaceConditionDemo()
