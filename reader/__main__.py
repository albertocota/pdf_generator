import sys
import reader

if len(sys.argv) > 1:
    r = reader.Reader(sys.argv[1])
    try:
        print(r.read())
    finally:
        r.close()

class CallCount:
    def __init__(self, f):
        print('Creating Instance of {}'.format(__name__))
        self.f = f
        self.count = 0
    def action(self):
        print('Action')
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def test(x):
    return x

test('No Value')
test('No Value')
test('No Value')
test('No Value')
print(test.count)

i = [(x*2+y,int(test(y))) for x in range(3) for y in range(2)]
print(i[-2:])
