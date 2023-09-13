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
        # get resourses
        # compare to ingredients
        # return true false
        if self.machine_resources["bread"] < ingredients["bread"]:
            return False
        if resources["ham"] < ingredients["ham"]:
            return False
        if resources["cheese"] < ingredients["cheese"]:
            return False
        else:
            return True

    # recipes["small"]["ingredients"]

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        # I spelled Received wrong 3 unique ways writing this
        # Figured it was worth a mention
        dollar = input("How many dollars are you inserting?")  # asks for money
        dollar = int(dollar)  # turns answer into a number for calculations
        print(f"Received {dollar} dollars!")  # returns number to make sure its working

        hdollar = input("How many half dollars are you inserting?")
        hdollar = int(hdollar)
        print(f"Received {hdollar} half dollars!")

        quarter = input("How many quarters are you inserting?")
        quarter = int(quarter)
        print(f"Received {quarter} quarters!")

        nickels = input("How many Nickels are you inserting?")
        nickels = int(nickels)
        print(f"Received {nickels} Nickels!")

        total_money = dollar + hdollar * .5 + quarter * .25 + nickels * .05
        print(f"You inserted ${total_money}!")
        return total_money

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        # coins will be total money from inputs
        if coins >= cost:
            return True
        else:
            print("ERROR, INSUFFICIENT FUNDS")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich made!")

    def report_stock(self):
        print(f"{recipes[resources]}")


### Make an instance of SandwichMachine class and write the rest of the codes ###


print("Welcome to Josh's EPIC Sandwich Shop!")

# declaring recipes because holy SHIT was it ugly before i did this
small_recipes = recipes["small"]
med_recipes = recipes["medium"]
large_recipes = recipes["large"]

machine = SandwichMachine(resources)  # initilizing

while True:
    # begin machine
    print("What can I get for ya? (small/medium/large/report)")
    customer = input(">")

    if customer == "report":
        print(f"{resources}")  # prints resources (fucking mindblowing i know)

    if customer == "small":  # small sandwich
        cash = machine.process_coins()  # get money for transaction
        if machine.transaction_result(cash, small_recipes["cost"]):  # if able to pay
            print(f'Here is your change! ({cash - small_recipes["cost"]})')  # returns change
            if machine.check_resources(small_recipes["ingredients"]):
                machine.make_sandwich("small", small_recipes["ingredients"])
            else:
                print("Not enough ingredients!")
                continue

        else:  # if unable
            continue  # returns error message in method

    if customer == "medium":  # small sandwich
        cash = machine.process_coins()  # get money for transaction
        if machine.transaction_result(cash, small_recipes["cost"]):  # if able to pay
            print(f'Here is your change! ({cash - small_recipes["cost"]})')  # returns change
            if machine.check_resources(small_recipes["ingredients"]):
                machine.make_sandwich("small", small_recipes["ingredients"])
            else:
                print("Not enough ingredients!")
                continue

        else:  # if unable
            continue  # returns error message in method
