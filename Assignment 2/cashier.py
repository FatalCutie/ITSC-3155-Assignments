class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        # I spelled Received wrong 3 unique ways writing this method
        # Figured it was worth a mention
        while True:
            try:  # is there a cleaner way to do this?
                print("How many dollars are you inserting?")  # asks for money
                dollar = input(">")  # awaits input
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

                print("How many nickels are you inserting?")
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
        # coins will be total money from inputs
        if coins >= cost:
            return True
        else:
            print(f"ERROR, INSUFFICIENT FUNDS ${abs(coins - cost)}")
            return False
