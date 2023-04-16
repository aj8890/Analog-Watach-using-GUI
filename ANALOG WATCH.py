import tkinter as tk
import math
import time

class AnalogWatch(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create canvas to draw the clock face
        self.canvas = tk.Canvas(self, width=200, height=200)
        self.canvas.pack()

# draw clock face
    canvas.create_oval(10, 10, 190, 190, width=2)
    for i in range(1, 13):
        angle = i * math.pi / 6
        x = 95 + 80 * math.cos(angle)
        y = 95 + 80 * math.sin(angle)
        canvas.create_text(x, y, text=str(i))

        # draw clock hands
        self.hour_hand = self.canvas.create_line(100, 100, 100, 60, width=3)
        self.minute_hand = self.canvas.create_line(100, 100, 100, 40, width=2)
        self.second_hand = self.canvas.create_line(100, 100, 100, 20, width=1)

        # update clock every second
        self.update_clock()

    def update_clock(self):
        # get current time
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec

        # calculate angles of clock hands
        hour_angle = (hour % 12) * 30 + minute * 0.5
        minute_angle = minute * 6
        second_angle = second * 6

        # rotate clock hands
        self.canvas.coords(self.hour_hand, 100, 100, 100 + 40 * math.sin(hour_angle * math.pi / 180), 100 - 40 * math.cos(hour_angle * math.pi / 180))
        self.canvas.coords(self.minute_hand, 100, 100, 100 + 60 * math.sin(minute_angle * math.pi / 180), 100 - 60 * math.cos(minute_angle * math.pi / 180))
        self.canvas.coords(self.second_hand, 100, 100, 100 + 80 * math.sin(second_angle * math.pi / 180), 100 - 80 * math.cos(second_angle * math.pi / 180))

        # update clock every second
        self.after(1000, self.update_clock)

root = tk.Tk()
app = AnalogWatch(master=root)
app.mainloop()
