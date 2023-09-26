import data

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients): # self, ingredients
        for item in ingredients: # get resources
            if self.machine_resources[item] < ingredients[item]: # compare to ingredients
                print(f"Sorry! We don't have enough {item}!")
                print()  # buffer line for readability
                return False
        else:
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            data.resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich made!") # debug message
        print("Enjoy!")
        print() # buffer line to increase terminal readability