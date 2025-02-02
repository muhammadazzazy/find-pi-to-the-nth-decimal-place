from math import pi
from sys import exit


def main() -> None:
    PI: str = str(pi)

    LIMIT: int = 15
    print(f'Welcome to The 🥧 Approximator!')

    prompt: str = f'Enter the number of decimal places (up to {LIMIT}): '

    while True:
        user_input: str = input(prompt)
        if user_input == 'exit':
            print('Thanks for trying my program!')
            exit()
        if not user_input.isnumeric() or int(user_input) > LIMIT:
            print(f'Please enter a whole number between 0 and {LIMIT}...')
            continue

        n: int = int(user_input)
        print(f'pi to the {n}th decimal place is {PI[:n+2]}')


if __name__ == '__main__':
    main()
