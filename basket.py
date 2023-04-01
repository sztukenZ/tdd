from item import Item
from pprint import pprint
from utils.colors import Bcolors


class Basket:

    def __init__(self):
        self.contents = dict()

    def count_total(self):
        total = 0
        if self.contents:
            for k, v in self.contents.items():
                total += v["amount"] * v["item"].get_price
        return total

    def view_basket(self):
        if self.contents:
            # print(self.contents)
            print(f"{Bcolors.OKGREEN + Bcolors.BOLD}Basket total: {self.count_total()}\n"
                  f"Items: {Bcolors.ENDC}")
            for k, v in self.contents.items():
                print(f"{Bcolors.OKGREEN} - {k.capitalize()} - Unit price: {v['item'].get_price}, amount: {v['amount']}"
                      f"{Bcolors.ENDC}")
            print("")
        else:
            print(f"{Bcolors.OKCYAN}The basket is currently empty\n{Bcolors.ENDC}")

    def add_item(self):
        item_name = input("Please provide an item name: ")
        # print(self.contents)
        # print(self.contents.get(item_name))
        if item_name in self.contents.keys():

            self.contents[item_name]["amount"] += 1
        else:
            while True:
                item_price = input("Please provide an item price: ")
                try:
                    if float(item_price) > 0:
                        item_price = float(item_price)
                        break
                except ValueError:
                    print(f"{Bcolors.FAIL}The price must be a positive number!{Bcolors.ENDC}")
            item = Item(item_name, item_price)
            self.contents[item_name] = dict()
            self.contents[item_name]["item"] = item
            self.contents[item_name]["amount"] = 1
        print(f"{Bcolors.OKGREEN}----- One {item_name.capitalize()} added to the basket{Bcolors.ENDC}\n")

    def delete_item(self):
        item_name = input("Please provide an item name: ")
        selected_item = self.contents.get(item_name)
        if selected_item is None:
            print("Nothing to delete")
        else:
            if self.contents[item_name]["amount"] > 0:
                self.contents[item_name]["amount"] -= 1
            else:
                self.contents.pop(selected_item)
            print(f"{Bcolors.WARNING}One {item_name.capitalize()} has been deleted.{Bcolors.ENDC}\n")
