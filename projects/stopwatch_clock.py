# Project 12: Stopwatch and Clock in Python
# Author: Your Name
# Date: Your Date

import tkinter as tk
from datetime import datetime
import time

# Define main class
class ClockStopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch / Clock App")

        # -------- Clock Section --------
        self.clock_label = tk.Label(root, text="", font=("Helvetica", 24), fg="green")
        self.clock_label.pack(pady=10)
        self.update_clock()  # Start updating the clock

        # -------- Stopwatch Section --------
        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 36), fg="blue")
        self.stopwatch_label.pack(pady=20)

        # Buttons: Start, Stop, Reset
        self.start_button = tk.Button(root, text="Start", width=10, command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", width=10, command=self.stop_stopwatch)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Reset", width=10, command=self.reset_stopwatch)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        # Stopwatch control variables
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

    # Function to update the clock every second
    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=f"Current Time: {now}")
        self.root.after(1000, self.update_clock)  # Call this function again after 1 second

    # Start the stopwatch
    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_stopwatch()

    # Stop the stopwatch
    def stop_stopwatch(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    # Reset the stopwatch to 00:00:00
    def reset_stopwatch(self):
        self.running = False
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")

    # Function to update stopwatch while running
    def update_stopwatch(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            hours = int(self.elapsed_time // 3600)
            minutes = int((self.elapsed_time % 3600) // 60)
            seconds = int(self.elapsed_time % 60)

            time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.stopwatch_label.config(text=time_str)
            self.root.after(1000, self.update_stopwatch)

# ----------- Run the App -----------
if __name__ == "__main__":
    root = tk.Tk()
    app = ClockStopwatchApp(root)
    root.geometry("400x250")
    root.mainloop()
