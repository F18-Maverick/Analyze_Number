import tkinter
import urllib.request
import json
import tkinter.messagebox
import threading
class Downloader:
    def __init__(self, app):
        self.app = app
    def start_download(self):
        threading.Thread(target=self.download_file).start()
    def download_file(self):
        url = self.app.entry.get()
        if not url:
            tkinter.messagebox.showerror("Error", "You MUST enter a URL!")
            return
        try:
            response = urllib.request.urlopen(url)
            file_type = self.get_file_type(response)
            self.save_file(response.read(), file_type)
            tkinter.messagebox.showinfo("Download", "File downloaded successfully!")
        except Exception as e:
            tkinter.messagebox.showerror("Error", str(e))
    def get_file_type(self, response):
        content_type = response.getheader("Content-Type")
        return content_type.split(';')[0].strip()  # 获取主类型
    def save_file(self, content, file_type):
        filename = f"downloaded_file.{file_type.split('/')[-1]}"
        with open(filename, "wb") as file:
            file.write(content)
