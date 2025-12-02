#ask user for their name
name = input("what's your name ? ")


#split user's name into first name and last name 
first, last = name.split(" ")
print("hello, ", sep=" ")
print(f"hello, son prenom est : {first} et son nom est :{last}")