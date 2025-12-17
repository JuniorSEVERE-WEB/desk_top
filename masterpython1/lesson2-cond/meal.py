def format_time(time:str)->float:
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60 
    return hours + minutes

def mealtime(time:float)->float:
    if time >= 7 and time <= 8:
        result = "breakfast time"
    elif time >= 12 and time <= 13:
        result = "lunch time"
    elif time >= 18 and time <= 19:
        result = "dinner time"
    else:
        result = None   
    return result 

def main():
    input_time = input("Type the hour with minutes like that 3:15...: ")     
    time_float = format_time(input_time)    
    eating_time = mealtime(time_float)
    print(f"{eating_time}")

if __name__ == "__main__":
    main() 
