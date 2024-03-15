class Category:
    def __init__(self,category):
        self.category=category
        self.ledger = []
    
    def __str__(self):
        response=""
        response+=(f"{self.category:*^30}\n")
        for item in self.ledger:
            response += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"


        response+=(f"Total: {(sum (item['amount'] for item in self.ledger))}")
        return f"{response}"           
        
    
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
    L=[]
    categories_percentages={}
    for item in categories_spend:
        percentage=(categories_spend[item])*100/total_spend
        percentage=int((percentage // 10)*10)
        categories_percentages[item]=percentage
        L.append(percentage)

    #String
    chart=""

    #Title
    chart+=(f"Percentage spent by category\n")

    #Data
    for i in range (100,-1,-10):
        line=f"{i:>3}| "
        for percentage in L:
            if percentage >=i:
                percentage="o"
            else:
                percentage=" "
            
            line+=f"{percentage}  "
        chart+=f"{line}\n"

    #Tags
    leng=len(categories)
    chart+=(f"    {'---'*leng}-\n")
    maximo=0

    for category in categories:
        if len(category.category)>maximo:
            maximo=len(category.category)    
    for i in range (maximo):
        ln="    "
        for category in categories:
            if i < len(category.category):            
                char=category.category[i]
            else:
                char=" "
            ln+=" "+char+" "
        if i!=maximo-1:
            chart+=f"{ln} \n"
        else:
            chart+=f"{ln} "
    return(chart)

   
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)