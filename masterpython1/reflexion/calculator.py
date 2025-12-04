def cost(expense):
    expense = expense.replace("$", "")
    return float(expense)

def percentage(rate):
    rate = rate.replace("%", "")
    return float(rate) / 100

def tip(meal_cost: float, tip_percentage:float)->float:
    result = float(meal_cost) * float(tip_percentage)
    return result 

def main():
    enterCost = input("Enter the cost with $: ")
    enterRate = input("Enter the percentage with %: ")
    meal_cost = cost(enterCost)
    tip_percentage = percentage(enterRate)
    tip_amount = tip(meal_cost, tip_percentage)
    print(f"The tip is ${tip_amount:.2f}")

if __name__ == "__main__":
    main()    