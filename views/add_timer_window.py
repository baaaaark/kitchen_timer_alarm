import tkinter as tk
from tkinter import ttk, messagebox

class AddTimerWindow:
    def __init__(self, parent):
        self.parent = parent
        self.add_window = tk.Toplevel(parent.root)
        self.add_window.title("Add Timer")
        self.add_window.geometry("300x220")
        
        # Title/Name Entry
        self.title_label = ttk.Label(self.add_window, text="Alarm Name:")
        self.title_label.pack(pady=5)
        self.title_entry = ttk.Entry(self.add_window)
        self.title_entry.pack(pady=5)

        # Timer Entry Frame
        self.timer_frame = ttk.Frame(self.add_window)
        self.timer_frame.pack(pady=20)

        # Labels Above Timer
        self.hours_label = ttk.Label(self.timer_frame, text="HH")
        self.hours_label.grid(row=0, column=0)
        self.intermediate_label_1 = ttk.Label(self.timer_frame, text=":")
        self.intermediate_label_1.grid(row=0, column=1)
        self.minutes_label = ttk.Label(self.timer_frame, text="MM")
        self.minutes_label.grid(row=0, column=2)
        self.intermediate_label_2 = ttk.Label(self.timer_frame, text=":")
        self.intermediate_label_2.grid(row=0, column=3)
        self.seconds_label = ttk.Label(self.timer_frame, text="SS")
        self.seconds_label.grid(row=0, column=4)
        
        # Hours Entry
        self.hours_entry = ttk.Entry(self.timer_frame, width=2, justify='center')
        self.hours_entry.grid(row=1, column=0)
        
        self.hours_character_label = ttk.Label(self.timer_frame, text=":")
        self.hours_character_label.grid(row=1, column=1)
        
        # Minutes Entry
        self.minutes_entry = ttk.Entry(self.timer_frame, width=2, justify='center')
        self.minutes_entry.grid(row=1, column=2)
        
        self.minutes_character_label = ttk.Label(self.timer_frame, text=":")
        self.minutes_character_label.grid(row=1, column=3)
        
        # Seconds Entry
        self.seconds_entry = ttk.Entry(self.timer_frame, width=2, justify='center')
        self.seconds_entry.grid(row=1, column=4)
        
        # Add Timer Button
        self.add_button = ttk.Button(self.add_window, text="Add Timer", command=self.add_timer)
        self.add_button.pack(pady=10)
        
    def add_timer(self):
        try:
            title = self.title_entry.get().strip()
            hours = int(self.hours_entry.get() or 0)
            minutes = int(self.minutes_entry.get() or 0)
            seconds = int(self.seconds_entry.get() or 0)
            
            if hours < 0 or minutes < 0 or seconds < 0:
                raise ValueError("Time must be non-negative.")
            
            total_seconds = hours * 3600 + minutes * 60 + seconds
            
            if total_seconds <= 0:
                raise ValueError("Total time must be greater than zero.")
            
            if not title:
                raise ValueError("Title cannot be empty.")
            
            self.parent.add_timer(title, hours, minutes, seconds)
            self.add_window.destroy()
            
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))