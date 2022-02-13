import queue
import threading
import turtle


class MultithreadedDrawing:
    def __init__(self):
        self.turtle1 = turtle.Turtle('turtle')
        self.turtle1.color('red')

        self.turtle2 = turtle.Turtle('turtle')
        self.turtle2.color('blue')

        self.graphics = queue.Queue(1)

    def task1(self):
        for _ in range(360):
            self.graphics.put(self.turtle1.forward)
            self.graphics.put(self.turtle1.left)

    def task2(self):
        for _ in range(360):
            self.graphics.put(self.turtle2.forward)
            self.graphics.put(self.turtle2.right)

    def process_queue(self):
        while not self.graphics.empty():
            (self.graphics.get())(1)

        if threading.active_count() > 1:
            turtle.ontimer(self.process_queue, 100)


md = MultithreadedDrawing()

thread1 = threading.Thread(target=md.task1)
thread1.daemon = True  # thread dies when only non-daemon thread exits.
thread1.start()

thread2 = threading.Thread(target=md.task2)
thread2.daemon = True  # thread dies when only non-daemon thread exits.
thread2.start()

md.process_queue()

turtle.exitonclick()
