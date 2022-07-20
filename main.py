import random

special_characters = ["!", "@", "#", "$", "%", "^", "&", "*"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
password_list = []
final_passowrd = ""


num_of_special_characters = int(input("how many special characters?"))
num_of_numbers = int(input("how many numbers?"))
num_of_alphabets = int(input("how many alphabets?"))


for num in range(num_of_special_characters):
    random_special_character = random.choice(special_characters)
    password_list.append(random_special_character)

for num in range(num_of_numbers):
    random_numbers = random.choice(numbers)
    password_list.append(random_numbers)

for num in range(num_of_alphabets):
    random_alphabets = random.choice(alphabets)
    password_list.append(random_alphabets)

random.shuffle(password_list)


password_string = "".join(password_list)
print(password_string)


for item in password_list:
    final_passowrd += item
print(final_passowrd)



