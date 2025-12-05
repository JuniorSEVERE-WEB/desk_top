def format_time(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    return hours + minutes

def meal_time(time):
    if time >= 7 and time <= 8:
        result = "breakfast time"
    elif time > 12 and time < 13:
        result = "lunch time"
    elif time > 18 and time < 19:
        result = "dinner time"   
    else:
        result = "Nothing"    
    return result
    
    

def main():
    input_hour = input("Type the hour like that : ")
    get_hour = format_time(input_hour)
    mealtime = meal_time(get_hour)
    print(mealtime)


main()
