import os

from .compressed import bzipped, gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gzip': gzipped.opener,
}


class Reader:
    def __init__(self, filename):
        print(filename)
        extension = os.path.splitext(filename)[1]
        print(extension)
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')

    def read(self):
        return self.f.read()

    def close(self):
        self.f.close()

