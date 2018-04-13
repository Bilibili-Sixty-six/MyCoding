import Throttle
import urllib2
import urlparse ###


class Download:
    def __init__(self, delay=5,
                 user_agent='greenleg',
                 proxies=None,
                 num_retries=1,
                 cache=None):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.cache = cache

    def __call__(self, url):
        pass

    def download(self,
                 url,
                 headers,
                 num_tries,
                 data=None):
        print 'Downloading:', url
        headers = {'User_agent': self.user_agent} ###
        request = urllib2.Request(url, headers=headers)

        opener = urllib2.build_opener()
        if self.proxies:
            proxy_params = {urlparse.urlparse(url).scheme: self.proxies}
            opener.add_handler(urllib2.ProxyHandler(proxy_params))
        try:
            html = opener.open(request).read()
        except urllib2.URLError as e:
            print 'Download error:', e.reason
            html = None
            if not self.num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    html = self.download(url, self.user_agent, self.proxies, self.num_retries-1)
        return html
