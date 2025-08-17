import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = subprocess.Popen([sys.executable, self.script])

    def on_modified(self, event):
        if event.src_path.endswith(self.script):
            print("🔄 Black-hacker-py-rat.py Updated → Restarting...")
            self.process.kill()
            self.process = subprocess.Popen([sys.executable, self.script])

if __name__ == "__main__":
    script_name = "Black-Hacker-.py"  # <-- ඔයාගේ main bot file name
    event_handler = ReloadHandler(script_name)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        event_handler.process.kill()
    observer.join()