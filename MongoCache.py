# -*- coding: UTF-8 -*-

import pickle
import zlib
from bson.binary import Binary
from datetime import datetime, timedelta
from pymongo import MongoClient


class MongoCache:
    """
    MongoCache(client=None, expires=timedelta(days=30), compress=False)
    self.__getitem__(url)
    self.__setitem__(url, result)
    """

    def __init__(self, client=None, expires=timedelta(days=30), compress=False):
        self.client = MongoClient('localhost', 27017) if client is None else client
        self.db = client.cache
        self.db.webpage.create_index('timestamp', expireAfterSeconds=expires.total_seconds())
        self.compress = compress

    def __getitem__(self, url):
        """Load value at this URL"""
        record = self.db.webpage.find_one({'_id': url})
        if record:
            if not self.compress:
                return record['result']
            else:
                return pickle.loads(zlib.decompress(record['result']))
        else:
            raise KeyError(url + ' does not exist')

    def __setitem__(self, url, result):
            """Save value for this URL"""
            if not self.compress:
                record = {'result': result, 'timestamp': datetime.utcnow()}
            else:
                record = {
                    'result': Binary(zlib.compress(pickle.dumps(result))),
                    'timestamp': datetime.utcnow()
                }
            self.db.webpage.update({'_id': url}, {'$set': record}, upsert=True)
