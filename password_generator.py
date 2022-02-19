import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@','#','$', '%', '&', '(', ')', '*', '+']

no_letters = int(input("how many letters u would like in ur password? \n"))
no_numbers = int(input("how many numbers u would like in ur password? \n"))
no_symbols = int(input("how many symbols u would like in ur password? \n"))

password = []    # for shuffling we will convert "" into list [] continued on line 25
for let in range(1,no_letters+1):
    password.append(random.choice(letters))

for let in range(1,no_numbers+1):
    password+=random.choice(numbers)

for let in range(1,no_symbols+1):
    password += random.choice(symbols)
# print(password)
random.shuffle(password)    #shuffled
print(password)

