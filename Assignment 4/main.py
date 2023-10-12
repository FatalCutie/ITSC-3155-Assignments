import cashier
import data
import sandwich_maker
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
machine = sandwich_maker.SandwichMaker(resources)
cashier = cashier.Cashier()  ######


def main():
    ###  write the rest of the codes ###
    print("Welcome to Josh's EPIC Sandwich Shop!")  # welcome message

    # declaring recipes to make code more readable
    small_recipes = data.recipes["small"]
    med_recipes = data.recipes["medium"]
    large_recipes = data.recipes["large"]

    while True:
        # begin machine
        print("What can I get for ya? (small/medium/large/report/q)")
        customer = input(">")

        match customer:
            case "report":
                print(f"{resources}")  # prints resources

            case "small":  # small sandwich
                if machine.check_resources(small_recipes["ingredients"]):  # if we have the resources
                    cash = cashier.process_coins()  # get money for transaction
                    if cashier.transaction_result(cash,
                                                  small_recipes["cost"]):  # check to make sure you have enough money
                        print(f'Here is your change! (${cash - small_recipes["cost"]})')
                        machine.make_sandwich(customer, small_recipes["ingredients"])
                    else:  # if unable
                        continue  # returns error message in method

            case "medium":  # medium sandwich
                if machine.check_resources(med_recipes["ingredients"]):  # if we have the resources
                    cash = cashier.process_coins()  # get money for transaction
                    if cashier.transaction_result(cash,
                                                  med_recipes["cost"]):  # check to make sure you have enough money
                        print(f'Here is your change! (${cash - med_recipes["cost"]})')
                        machine.make_sandwich(customer, med_recipes["ingredients"])
                    else:  # if unable
                        continue  # returns error message in method

            case "large":  # large sandwich
                if machine.check_resources(large_recipes["ingredients"]):  # if we have the resources
                    cash = cashier.process_coins()  # get money for transaction
                    if cashier.transaction_result(cash,
                                                  large_recipes["cost"]):  # check to make sure you have enough money
                        print(f'Here is your change! (${cash - large_recipes["cost"]})')
                        machine.make_sandwich(customer, large_recipes["ingredients"])
                    else:  # if unable
                        continue  # returns error message in method

            case "q":
                print("See you again soon!")
                break


# if __name__=="__main__":
#     main()


main()
