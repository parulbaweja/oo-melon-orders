"""Classes for melon orders."""

from random import randint


class AbstractMelonOrder(object):
    """Abstract class for melon orders"""

    shipped = False

    def __init__(self, species, qty):
        self.species = species
        if qty > 100:
            raise TooManyMelonsError()
        self.qty = qty

    def get_base_price(self):
        if not self.base_price:
            self.base_price = randint(5, 9)

    def get_total(self):
        """Calculate price, including tax."""
        self.get_base_price()
        print base_price
        if self.species == "Christmas melon":
            new_base_price = 1.5 * self.base_price

        total = (1 + self.tax) * self.qty * new_base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3

        return total

class GovernmentMelonOrder(AbstractMelonOrder):

    tax = 0.00
    passed_inspection = False

    def mark_inspection(self, passed):

        self.passed_inspection = passed

class TooManyMelonsError(ValueError):
    def __init__(self):
        super(TooManyMelonsError, self).__init__('No more than 100 melons!')
        # ValueError.__init__(self, 'No more than 100 melons!')
