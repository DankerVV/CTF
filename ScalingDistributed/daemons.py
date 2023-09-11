from threading import Thread
import time

def task():
    for i in range(10):
        print(i)
        time.sleep(0.5)

thread = Thread(target=task, daemon=True)
thread.start()
time.sleep(2)
print("END")
