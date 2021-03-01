import time
def worker(id, event):
    while(not event.is_set()):
        time.sleep(2)
        print(id)
    return 0