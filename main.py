from basket import Basket
from utils.colors import Bcolors


def run_app():
    """
    Runs the app
    :return: None
    """
    basket = Basket()
    is_on = True
    while is_on:
        print(f"{Bcolors.HEADER}###############################{Bcolors.ENDC}")
        print("""Add item to the basket: type a\nDelete item from the basket: type d\nQuit the program: q
View basket: v\n""")
        user_input = input("Please provide your command: ").lower()

        # Controls the app by user's input
        match user_input:
            case "a":
                basket.add_item()
            case "d":
                basket.delete_item()
            case "v":
                basket.view_basket()
            case "q":
                is_on = False


if __name__ == '__main__':
    run_app()

