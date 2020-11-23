import urllib.request
import time

def fetch(url: str) -> str:
    retries = 0
    while retries < 3:
        try:
            with urllib.request.urlopen(url) as r:
                return r.read()
        except:
            retries += 1
            time.sleep(5)    
    raise ValueError(f'Could not fetch from URL {url}.')