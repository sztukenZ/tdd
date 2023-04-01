from basket import Basket
from utils.colors import Bcolors


def app_controller(basket: Basket):
    while True:
        print(f"{Bcolors.HEADER}###############################{Bcolors.ENDC}")
        print("""
        Add item to the basket: type a
        Delete item from the basket: type d
        Quit the program: q
        View basket: v\n""")
        user_input = input("Please provide your command: ").lower()
        match user_input:
            case "a":
                basket.add_item()
            case "d":
                basket.delete_item()
            case "v":
                basket.view_basket()
            case "q":
                print("Gracefully stopping...")
                break


def run_app():
    """
    Runs the app
    :return: None
    """
    basket = Basket()
    app_controller(basket)


if __name__ == '__main__':
    run_app()
