from urlparse import urlparse
from datetime import datetime
from time import sleep


class Throttle:
    """Add a delay between downloads to the same domain"""
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)

        if self.delay > 0 and last_accessed is not None:
            # sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            sleep_secs = self.delay - (datetime.now().second - last_accessed.second)
            if sleep_secs > 0:
                sleep(sleep_secs)

        self.domains[domain] = datetime.now()
