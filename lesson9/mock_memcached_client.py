import queue
import time

class MockMemcachedClient:
    def __init__(self):
        self.data = {}
        self.ttls = queue.PriorityQueue()
    
    def vacuum(self):
        # Any calls to the mock client will call vacuum
        # to clean up any items that have exceeded their
        # time to live.
        now = time.time()
        try:
            while True:
                t, key = self.ttls.get(False)
                if t <= now:
                    del self.data[key]
                else:
                    self.ttls.put((t, key))
                    return
        except queue.Empty:
            return

    def set(self, key, value, expire=0, noreply=None, flags=None):
        self.data[key] = value
        if expire != 0:
            self.ttls.put((
                time.time()+expire, 
                key,
            ))
        self.vacuum()
        return True

    def get(self, key, default=None):
        self.vacuum()
        return self.data.get(key, default)