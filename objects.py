from datetime import datetime
"""
This file only acts to serve as a list of properties associated with eact object related to a 
transaction. This is not to be runnable code. Eventually this will be deleted once replaced 
with functional objects.
"""
class Transaction:
    """
    transaction_id
    location_id
    user_id
    items
    transaction_datetime # datetime should be recorded. Want it all the way down to the second.
    transaction_coords # if this is empty, then it should default to the company location.
    sub_total # can either be provided or calculated from all items
    tax # can be used to calculate the tax rate
    total # will probably be provided, but can be calculated as sub_total + tax
    """
    def __init__(self, location_id, user_id, items, sub_total, tax, total, transaction_coords=None):
        self.transaction_id = self.generate_transaction_id()
        self.location_id = location_id
        self.user_id = user_id
        self.items = items
        self.sub_total = sub_total
        self.tax = tax
        self.total = total
        self.transaction_coords = transaction_coords if transaction_coords \
                                    else Location.get_location_by_id(location_id).get_coords()
        self.transaction_datetime = datetime.now()

    def generate_transaction_id(self):
        """
        Function to generate a new transaction id
        :return:
        """
        pass


class Items:
    """
    item_id
    transaction_id
    item_name
    item_common_name
    item_cost
    """
    def __init__(self, item_id, transaction_id, item_name, item_common_name, item_cost):
        self.item_id = item_id
        self.transaction_id = transaction_id
        self.item_name = item_name
        self.item_common_name = item_common_name
        self.item_cost = item_cost


class Company:
    """
    company_id
    company_name
    """
    def __init__(self, company_id, company_name):
        self.company_id = company_id
        self.company_name = company_name


class Location:
    """
    location_id
    company_id
    location_coords
    """
    def __init__(self, location_id, company_id, location_coords):
        self.location_id = location_id
        self.company_id = company_id
        self.coords = location_coords

    def get_coords(self):
        return self.coords

    def get_location_by_id(id):
        """
        Static method used to get the Location object by id from a database.
        :return:
        """
        pass


class User:
    """
    user_id
    """
    def __init__(self, user_id):
        self.user_id = user_id

