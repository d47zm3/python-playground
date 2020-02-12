import threading
import time
import os

next_call = time.time()
src_path = "/src"


def start_loop():
    global next_call
    count = 0
    for file in os.listdir(src_path):
        if file.endswith(".xml"):
            filepath = os.path.join(src_path, file)
            threading.Thread(target=process, args=(filepath,)).start()
            count = count + 1

    if count > 0:
        print(f"received {count} new files...")

    next_call = next_call + 30
    threading.Timer(next_call - time.time(), start_loop).start()


def process(filepath):
    print(f"processing file {filepath}...")


if __name__ == "__main__":
    start_loop()
