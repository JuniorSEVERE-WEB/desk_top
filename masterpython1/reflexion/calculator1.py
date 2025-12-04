def cost(expense:str)->float:
    expense = expense.replace("$", "")
    return float(expense)

def percentage(rate:str)->float:
    rate = rate.replace("%", "")
    return float(rate) / 100

def tip(mealCost:float, mealPercentage:float)->str:
    result = mealCost * mealPercentage
    return result 

def main():
    inputCost = input("Enter the cost of a meal with a $: ")
    inputPercentage = input("Enter the percentage with a %: ")
    mealCost = cost(inputCost)
    mealPercentage = percentage(inputPercentage)
    tip_amount = tip(mealCost, mealPercentage)
    print(f"The tip is ${tip_amount:.2f}")

main()