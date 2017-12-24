#!/usr/bin/env python

import sys
import time
import blinkt
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

FILE_TO_WATCH = "/tmp/blink_count"

blinkt.set_brightness(0.05)
blinkt.set_clear_on_exit(True)

class Watcher:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, "/tmp", recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print "Error"

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'modified':
            if event.src_path == FILE_TO_WATCH:
		value = open(FILE_TO_WATCH, "r").read().split("\n")[0]
		open(FILE_TO_WATCH, "r").seek(0)
		try:
                	count = int(value)
                except ValueError:
                	count = 255 # failover

		blinkt.set_all(0,0,0) # clear 
	
		if count == 0:
    			blinkt.set_all(0,0,0)
  		else:
    			for i in range(count):
       				blinkt.set_pixel(i, 0, 255, 255)
       				blinkt.show()
       				time.sleep(0.05)

    			time.sleep(0.3)
	

if __name__ == "__main__":
    w = Watcher()
    w.run()
