import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from views.add_timer_window import AddTimerWindow
from controllers.timer_controller import TimerController

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.root.geometry("400x400")
        
        self.controller = TimerController(self)
        
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, anchor="center")
        
        self.add_timer_button = ttk.Button(self.main_frame, text="Add Timer", command=self.open_add_timer_window)
        self.add_timer_button.pack(pady=10)
        
        self.timer_list_frame = ttk.Frame(self.main_frame)
        self.timer_list_frame.pack(fill="both", expand=True)
        
        self.update_timers(self.controller.get_timers())

    def open_add_timer_window(self):
        AddTimerWindow(self)
        
    def update_timers(self, timers):
        for widget in self.timer_list_frame.winfo_children():
            widget.destroy()
            
        current_time = datetime.now()
        updated_timers = []
        
        for timer in timers:
            end_time = timer["end_time"]
            time_left = end_time - current_time
            if time_left.total_seconds() > 0:
                updated_timers.append(timer)
                
                title_label = ttk.Label(self.timer_list_frame, text=timer["title"], justify='center')
                title_label.grid(row=len(updated_timers), column=0, padx=10)
                
                countdown_label = ttk.Label(self.timer_list_frame, text=str(time_left).split('.')[0], justify='center')
                countdown_label.grid(row=len(updated_timers), column=1, padx=10)
                
                end_time_label = ttk.Label(self.timer_list_frame, text=end_time.strftime("%I:%M:%S %p"), justify='center')
                end_time_label.grid(row=len(updated_timers), column=2, padx=10)
                
                delete_button = ttk.Button(self.timer_list_frame, text="Delete", command=lambda t=timer: self.confirm_delete(t))
                delete_button.grid(row=len(updated_timers), column=3, padx=10)

            elif time_left.total_seconds() < 0:
                updated_timers.append(timer)
                time_left_abs = abs(time_left)
                negative_countdown_text = f"-{str(time_left_abs).split('.')[0]}"
                
                title_label = ttk.Label(self.timer_list_frame, text=timer["title"], justify='center')
                title_label.grid(row=len(updated_timers), column=0, padx=10)

                countdown_label = ttk.Label(self.timer_list_frame, text=negative_countdown_text, justify='center')
                countdown_label.grid(row=len(updated_timers), column=1, padx=10)
                
                end_time_label = ttk.Label(self.timer_list_frame, text=end_time.strftime("%I:%M:%S %p"), justify='center')
                end_time_label.grid(row=len(updated_timers), column=2, padx=10)
                
                delete_button = ttk.Button(self.timer_list_frame, text="Clear", command=lambda t=timer: self.clear_time(t) )
                delete_button.grid(row=len(updated_timers), column=3, padx=10)

                if not timer["completion_status"]:
                    self.controller.expired_timer(timer)
                
        self.root.after(1000, lambda: self.update_timers(self.controller.get_timers()))

    def clear_time(self, timer):
        self.controller.clear_timer(timer)
        self.update_timers(self.controller.timers)

    def confirm_delete(self, timer):
        result = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{timer['title']}'?")
        if result:
            self.controller.delete_timer(timer)
            self.update_timers(self.controller.timers)
        
    def add_timer(self, title, hours, minutes, seconds):
        self.controller.add_timer(title, hours, minutes, seconds)
        self.update_timers(self.controller.timers)
