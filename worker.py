import time
def worker(id, event):
    while(not event.is_set()):
        time.sleep(2)
        print(id)
    return 0

def worker_watch_queue(id, event, conn, callbacks):
    while(not event.is_set()):
        packed = conn.blpop('queue:jobs', 1)
        if not packed:
            continue
        name, args = json.loads(packed[1])
        if name not in callbacks:
            log_error("Unknown callback %s"%name)
            continue
        callbacks[name](*args)