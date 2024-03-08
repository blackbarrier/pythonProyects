class Category:
    def __init__(self,category):
        self.category=category
        self.ledger = []
    
    def __str__(self):
        response=""
        response+=(f"{self.category:*^30}\n")
        for item in self.ledger:
            response+=(f"{item['description'][:23]:<23}{item['amount']:>7}\n")
        response+=(f"Total: {(sum (item['amount'] for item in self.ledger))}")
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
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False     

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    

def create_spend_chart(categories):
    #Take values by category
    categories_spend={}
    total_spend=0
    for category in categories:
        category_dict={}
        category_spend=0
        for spend in category.ledger:
            if spend["amount"]<0:
                category_spend+=spend["amount"]                
        categories_spend[f"{category.category}"]=category_spend
        total_spend+=category_spend
     
    #Calculate percentage
    categories_percentages={}
    for item in categories_spend:
        percentage=(categories_spend[item])*100/total_spend
        percentage=round(percentage / 10) * 10
        categories_percentages[item]=percentage
    print(categories_percentages)

    #GragicarString

    
    leng=len(categories_percentages)
    # for i in range(100, -1, -10):
    
    L=[]
    for item in categories_percentages:
        if (categories_percentages[item])>=10:
            L.append("o")
        else:
            L.append("")
    linea = ' '.join(L)
    
    print(linea)



            # L.append(categories_percentages[item])
        # myvar=f" {}{}{}"
        # y=f"{i:>3}|{myvar}"
        # print(y)
   


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)

clothing.withdraw(30.15, "cosas")


# print(food)
# print(food.transfer(50, clothing))
# print(clothing)
create_spend_chart([food,clothing])