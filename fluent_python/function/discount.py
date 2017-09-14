from abc import ABC, abstractmethod
from collections import namedtuple

customer = namedtuple("customer", "name fidelity")


class LineItem:

    def __init__(self, product, quanlity, price):
        self.product = product
        self.quanlity = quanlity
        self.price = price

    def total(self):
        return self.price * self.quanlity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())


class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        # return discount
        pass


class FidelityPromo(Promotion):
    """5% discount if custom's integration over 1000"""

    def discount(self, order):
        return order.total * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """10% discount for one product if one product's quanlity over 20"""

    def discount(self, order):
        dicount = 0
        for item in order.cart:
            if item.quanlity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):
    """7% discount for one product if over 10 different products in one order"""

    def discount(self, order):
        item = {item for item in order.cart}
        if len(item) >= 20:
            return order.total() * 0.07
        return 0

joe = customer("John Doe", 0)
ann = customer("Ann Smith", 1000)
cart = [LineItem("banana", 4, 0.5),
        LineItem("apple", 5, 0.7),
        LineItem("oringe", 10, 0.6)]
print(Order(joe, cart, FidelityPromo()))

