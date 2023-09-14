### Data ###

recipes = {  ##dicitionary
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete these functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # get resources
        # compare to ingredients
        # return true false
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                return False
        else:
            return True

    # recipes["small"]["ingredients"]

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        # I spelled Received wrong 3 unique ways writing this method
        # Figured it was worth a mention
        while True:
            try:  # is there a cleaner way to do this?
                print("How many dollars are you inserting?")  # asks for money
                dollar = input(">") # awaits input
                dollar = int(dollar)  # turns answer into a number for calculations
                # print(f"Received {dollar} dollars!")  # debug text

                print("How many half dollars are you inserting?")
                hdollar = input(">")
                hdollar = int(hdollar)
                # print(f"Received {hdollar} half dollars!")

                print("How many quarters are you inserting?")
                quarter = input(">")
                quarter = int(quarter)
                # print(f"Received {quarter} quarters!")

                print("How many Nickels are you inserting?")
                nickels = input(">")
                nickels = int(nickels)
                # print(f"Received {nickels} Nickels!")

                total_money = dollar + hdollar * .5 + quarter * .25 + nickels * .05
                print(f"You inserted ${total_money}!")
                return total_money
            except ValueError:
                print("Oops! I didn't quite understand that!")
                continue

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        # coins will be total money from inputs
        if coins >= cost:
            return True
        else:
            print(f"ERROR, INSUFFICIENT FUNDS ${abs(coins - cost)}")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich made!") # debug message
        print("Enjoy!")
        print()  # buffer line to increase terminal readability

    def report_stock(self):
        print(f"{recipes[resources]}")


### Make an instance of SandwichMachine class and write the rest of the codes ###
# no, shut up

print("Welcome to Josh's EPIC Sandwich Shop!") # welcome message

# declaring recipes to make code more readable
small_recipes = recipes["small"]
med_recipes = recipes["medium"]
large_recipes = recipes["large"]

machine = SandwichMachine(resources)  # initializing

while True:
    # begin machine
    print("What can I get for ya? (small/medium/large/report/q)")
    customer = input(">")

    match customer:
        case "report":
            print(f"{resources}")  # prints resources

        case "small":  # small sandwich
            if machine.check_resources(small_recipes["ingredients"]): # if we have the resources
                cash = machine.process_coins()  # get money for transaction
                if machine.transaction_result(cash, small_recipes["cost"]): # check to make sure you have enough money
                    print(f'Here is your change! (${cash - small_recipes["cost"]})')
                    machine.make_sandwich(customer, small_recipes["ingredients"])
                else:  # if unable
                    continue  # returns error message in method
            else:
                print("Not enough ingredients!")
                continue

        case "medium":  # medium sandwich
            if machine.check_resources(med_recipes["ingredients"]): # if we have the resources
                cash = machine.process_coins()  # get money for transaction
                if machine.transaction_result(cash, med_recipes["cost"]): # check to make sure you have enough money
                    print(f'Here is your change! (${cash - med_recipes["cost"]})')
                    machine.make_sandwich(customer, med_recipes["ingredients"])
                else:  # if unable
                    continue  # returns error message in method
            else:
                print("Not enough ingredients!")

        case "large":  # large sandwich
            if machine.check_resources(large_recipes["ingredients"]): # if we have the resources
                cash = machine.process_coins()  # get money for transaction
                if machine.transaction_result(cash, large_recipes["cost"]): # check to make sure you have enough money
                    print(f'Here is your change! (${cash - large_recipes["cost"]})')
                    machine.make_sandwich(customer, large_recipes["ingredients"])
                else:  # if unable
                    continue  # returns error message in method
            else:
                print("Not enough ingredients!")

        case "q":
            print("See you again soon!")
            break