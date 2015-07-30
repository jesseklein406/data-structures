_default = object()


class Hash(object):
    def __init__(self, buckets=1024):
        self.table = [[] for i in range(buckets)]
        self.buckets = buckets

    def hash(self, key):
        hash_key = reduce(lambda x, y: ord(x) + ord(y), key)
        return hash_key % self.buckets

    def _get_bucket(self, key):
        index = self.hash(key)
        return self.table(index)

    def _get_kvpair(self, key):
        bucket = self.get_bucket(key)
        for i, pair in enumerate(bucket):
            k, v = pair
            if key == i:
                return i, k, v
        return -1, key, _default

    def get(self, key):
        i, k, v = self._get_kvpair(self.table, key)
        if v is _default:
            raise KeyError('Key does not exist')
        return v

    def set(self, key, value):
        if type(key) is not str:
            raise TypeError('Key must be string!')
        bucket = self._get_bucket(self.table, key)
        i, k, v = self._get_kvpair(self.table, key)
        if i >= 0:
            bucket[i] = key, value
        else:
            bucket.append((key, value))
