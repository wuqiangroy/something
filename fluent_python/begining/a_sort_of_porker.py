# _*_ utf-8 _*_

from collections import namedtuple

Card = namedtuple("card", ["rank", "suit"])


class Deck(object):
    """define func self"""

    ranks = [str(i) for i in list(range(2, 11)) + list("JQKA")]
    suits = "spades diamonds clubs hearts".split(" ")

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        # define the new len
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

if __name__ == "__main__":
    d = Deck()
    print(len(d))
    # print(d.__len__())
    print(d[1])
    print(d[0])
    # you even can loop object -d
    for card in d:
        print(card)
