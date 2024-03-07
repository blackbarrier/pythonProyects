class Category:
    def __init__(self,category):
        self.category=category
        self.ledger = []
    
    def __str__(self):
        print(f"{self.category:*^30}\n")
        for item in self.ledger:
            print(f"{item['description']:<23}{item['amount']:>7}\n")
        print("Total:",(sum (item["amount"] for item in self.ledger)))
        response=""
        return response           
        
        # return response
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            amount*=-1
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance=0
        for item in self.ledger:
            balance+=item["amount"]

        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {self.category}")
            self.deposit(amount, f"Transfer from {category.category}")
            return True
        return False     

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    

def create_spend_chart(categories):
    #Gragico de barras
    pass


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
# print(food.transfer(50, clothing))
