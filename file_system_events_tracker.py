import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Ola, {event.src_path} foi criado")
    def on_deleted(self, event):
        print(f"opa! Alguem excluiu {event.src_path}!")
    def on_modified(self, event):
        print(f"alguem modificou {event.src_path}")
    def on_moved(self, event):
        print(f"alguem moveu {event.src_path}")
try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("Interrompido!")
    Observer.stop()


