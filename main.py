from math import pi

# print(type(pi))
PI = str(pi)

LIMIT = 15
print(f'This program finds pi to the nth decimal place where n is at most {LIMIT}.')

prompt = 'Enter the number of decimal places: '

user_input = input(prompt)

if user_input.isnumeric():
    n = int(user_input)
    while n > LIMIT:
        user_input = input(prompt)
        if user_input.isnumeric():
            n = int(user_input)
        else:
            break

while not user_input.isnumeric():
    user_input = input(prompt)
    if user_input.isnumeric():
        n = int(user_input)
        while n > LIMIT:
            user_input = input(prompt)
            if user_input.isnumeric():
                n = int(user_input)
            else:
                break

print(f'pi to the {n}th decimal place is {PI[:n+2]}')
