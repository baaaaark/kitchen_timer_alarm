from datetime import datetime, timedelta
import requests

class TimerController:
    def __init__(self, view):
        self.view = view
        self.server_url = 'http://127.0.0.1:8080/'
        self.timers = []

    def add_timer(self, title, hours, minutes, seconds):
        end_time = datetime.now() + timedelta(hours=hours, minutes=minutes, seconds=seconds)
        completion_status = False
        timer = {"title": title, "end_time": end_time, "completion_status": completion_status}
        self.timers.append(timer)
        self.notify_server(timer, method="POST")
        return timer

    def delete_timer(self, timer):
        self.timers.remove(timer)
        self.notify_server(timer, method="DELETE")

    def clear_timer(self, timer):
        self.timers.remove(timer)
    
    def completed_timer(self, timer):
        timer["completion_status"] = True
        timer = {"title": timer["title"], "end_time": timer["end_time"], "completion_status": timer["completion_status"]}
        self.notify_server(timer, method="PUT")
    
    def get_timers(self):
        return self.timers

    def notify_server(self, timer, method):
        data = {
            "title": timer["title"],
            "end_time": timer["end_time"].strftime("%Y-%m-%d %H:%M:%S"),
            "completion_status": timer["completion_status"]
        }
        try:
            if method == "POST":
                response = requests.post(f"{self.server_url}/timer", json=data)
            elif method == "DELETE":
                response = requests.delete(f"{self.server_url}/timer", json=data)
            elif method == "PUT":
                response = requests.put(f"{self.server_url}/timer", json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to notify server: {e}")