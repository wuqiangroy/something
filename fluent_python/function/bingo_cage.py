import random


class BingoCage(object):

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except Exception:
            raise LookupError("pick from a empty BingoCage")

    def __call__(self):
        return self.pick()

if __name__ == "__main__":
    bingo = BingoCage(range(6))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))
