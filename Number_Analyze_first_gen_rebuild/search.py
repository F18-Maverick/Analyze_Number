import tkinter
import webbrowser
import threading
class Search:
    def __init__(self, app):
        self.app = app
    def start_search(self):
        threading.Thread(target=self.open_url).start()
    def open_url(self):
        url = self.app.entry.get()
        if not url:
            tkinter.messagebox.showerror("Error", "You MUST enter a URL!")
            return
        webbrowser.open(url)
