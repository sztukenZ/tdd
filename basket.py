from typing import Union, Callable

from item import Item
from utils.colors import Bcolors


def check_item_name_is_number(item_name: str) -> bool:
    """
    Checks if the item name does not just a number
    :param item_name: The name of the item
    :return: bool
    """
    try:
        float(item_name)
    except ValueError:
        return False
    print(f"{Bcolors.WARNING}Please provide the name that is not just a number!{Bcolors.ENDC}")
    return True


def check_if_num_positive(num: str, num_type: Callable) -> Union[float, int]:
    """
    Checks if provided string input is a positive number
    :param num: number as a string
    :param num_type: int or float
    :return: int or float
    """
    try:
        if num_type(num) > 0:
            item_amount = num_type(num)
            return item_amount
    except ValueError:
        # print(num_type)
        num_type_desc = ""
        if num_type == int:
            num_type_desc = "whole "
        print(f"{Bcolors.WARNING}Please provide a positive {num_type_desc}number!{Bcolors.ENDC}\n")


class Basket:
    """
    A class implemented to imitate a store basket
    """

    def __init__(self):
        self.contents = dict()

    def count_total(self) -> float:
        """
        Returns the total price of the basket items
        :return: float
        """
        total = 0
        if self.contents:
            for k, v in self.contents.items():
                total += v["amount"] * v["item"].get_price
        return total

    def view_basket(self):
        """
        Prints out the basket contents
        :return: None
        """
        if self.contents:
            print(f"{Bcolors.OKGREEN + Bcolors.BOLD}Basket total: {self.count_total()} $\n"
                  f"Items: {Bcolors.ENDC}")
            for k, v in self.contents.items():
                print(f"{Bcolors.OKGREEN} - {k.capitalize()} - Unit price: {v['item'].get_price}, amount: {v['amount']}"
                      f"{Bcolors.ENDC}")
            print("")
        else:
            print(f"{Bcolors.OKCYAN}The basket is currently empty\n{Bcolors.ENDC}")

    def add_item(self):
        """
        Adds item/s to the basket
        :return: None
        """
        while True:
            item_name = input("Please provide an item name: ")
            if not check_item_name_is_number(item_name):
                break
        while True:
            item_amount = input("Please provide item amount: ")
            item_amount = check_if_num_positive(item_amount, int)
            if item_amount is not None:
                break

        if item_name in self.contents.keys():
            self.contents[item_name]["amount"] += item_amount
        else:
            while True:
                item_price = input("Please provide an item price: ")
                item_price = check_if_num_positive(item_price, float)
                if item_price is not None:
                    break
            item = Item(item_name, item_price)
            self.contents[item_name] = dict()
            self.contents[item_name]["item"] = item
            self.contents[item_name]["amount"] = item_amount
        print(f"{Bcolors.OKGREEN}----- {item_amount} items '{item_name.capitalize()}' added to the basket"
              f"{Bcolors.ENDC}\n")

    def delete_item(self):
        """
        Deletes the item/s from the basket
        :return: None
        """
        while True:
            item_name = input("Please provide an item name: ")
            if not check_item_name_is_number(item_name):
                break
        selected_item = self.contents.get(item_name)
        if selected_item is None:
            print(f"{Bcolors.FAIL} No item named {item_name.capitalize()} found in the basket. Nothing to delete."
                  f"{Bcolors.ENDC}\n")
        else:
            while True:
                item_amount = input("Please provide item amount: ")
                item_amount = check_if_num_positive(item_amount, int)
                if item_amount is not None:
                    break

            deleted_items = 0
            for i in range(item_amount):
                try:
                    if self.contents[item_name]["amount"] > 0:
                        self.contents[item_name]["amount"] -= 1
                        deleted_items += 1
                        if self.contents[item_name]["amount"] == 0:
                            self.contents.pop(item_name)

                    else:
                        deleted_items = 1
                        self.contents.pop(item_name)
                except KeyError:
                    break

            print(f"{Bcolors.WARNING}{deleted_items} {item_name.capitalize()} items have been deleted.{Bcolors.ENDC}\n")
