# -*- coding: UTF-8 -*-

import urllib2
import urlparse
import random
from Throttle import Throttle


class Download:
    def __init__(self, delay=5, user_agent='greenleg', proxies=None, num_retries=1, cache=None):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.cache = cache

    def __call__(self, url):
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                pass
            else:
                if self.num_retries > 0 and 500 < result['code'] < 600:
                    result = None
        if result is None:
            self.throttle.wait(url)
            proxy = random.choice(self.proxies) if self.proxies else None
            headers = {'User_agent': self.user_agent}
            result = self.download(url, headers, proxy, self.num_retries)
            if self.cache:
                self.cache[url] = result
        return result['html']

    def download(self, url, headers, proxy, num_retries, data=None):
        print 'Downloading:', url
        # headers = {'User_agent': self.user_agent}
        request = urllib2.Request(url, headers=headers)
        code = None

        opener = urllib2.build_opener()
        if proxy:
            proxy_params = {urlparse.urlparse(url).scheme: self.proxies}
            opener.add_handler(urllib2.ProxyHandler(proxy_params))
        try:
            html = opener.open(request).read()
        except urllib2.URLError as e:
            print 'Download error:', e.reason
            html = None
            if not num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    code = e.code
                    html = self.download(url, headers, proxy, self.num_retries-1)

        return {'html': html, 'code': code}
