def calculate_sum(*args):
    total = 0 
    for n in args:
        total += n 
    return total 

print(calculate_sum(1, 2, 3))    
