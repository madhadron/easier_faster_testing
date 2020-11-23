async def assertEventuallyTrue(
    self, predicate, message, timeout=3, sleep_time=0.1):
    t0 = time.time()
    while not predicate():
        if time.time() >= t0 + timeout:
            self.fail(message)
        await asyncio.sleep(sleep_time)