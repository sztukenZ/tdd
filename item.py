
class Item:

    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def get_name(self):
        return self._name

    @property
    def get_price(self):
        return self._price
