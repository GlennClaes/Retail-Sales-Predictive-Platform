from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import subprocess
import os

REPO_PATH = "C:/Projecten/Retail-Sales-Predictive-Platform"

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".csv") or event.src_path.endswith(".py"):
            print(f"Detected change: {event.src_path}")
            os.chdir(REPO_PATH)
            
            # Auto-commit en push alleen als er iets te committen is
            subprocess.run(["git", "add", "."])
            result = subprocess.run(["git", "diff", "--cached", "--quiet"])
            if result.returncode != 0:  # 0 = geen veranderingen
                subprocess.run(["git", "commit", "-m", "Auto-update changes"])
                subprocess.run(["git", "push", "origin", "main"])
            
            # Pull laatste changes en retrain model lokaal
            subprocess.run(["git", "pull", "--rebase"])
            subprocess.run(["python", "app/ml/retrain_model.py"])
            print("Synced and retrained model.")

if __name__ == "__main__":
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=REPO_PATH, recursive=True)
    observer.start()
    print("Watching for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
