"""Classes for melon orders."""

from random import randint
from datetime import time, date, datetime


class AbstractMelonOrder:
    """Parent class for all melon orders."""
    shipped = False

    # init defines species, qty, shipped
    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        
    # def get_base_price, choose random num between 5 & 9
    # use new base price in get_total
    def get_base_price(self):
        """return random baseprice 5-9"""

        
        # if Mon-Fri 8-11am, add $4
        # use datetime.hour to check time
        # use date.weekday to return DOW

        base_price = randint(5, 10)
        order_time = datetime.now()

        # check if during rush hour (need time and day of week)
        #if date.weekday(order_time) <= 4 and order_time.hour >= 8 and order_time.hour < 11:
        if date.weekday(order_time) <= 4 and 8 <= order_time.hour < 11:
            base_price += 4

        return base_price


    # add methods get_total, mark_shipped
    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        # if species "christmas" base*1.5
        if self.species.startswith("Christmas"):
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

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
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super().get_total()
        if self.qty < 10:
            total += 3

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """An order from the government."""
    tax = 0
    passed_inspection = False

    # mark_method(passed) checks passed, updates passed_inspection
    def mark_inspection(self, passed):
        """Checks if melons passed inspection."""

        if passed:
            self.passed_inspection = True

        return self.passed_inspection
 