from views.main_window import TimerApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()