from math import pi
from sys import exit
from word2number import w2n


def main() -> None:
    PI: str = str(pi)
    LIMIT: int = 15
    print(f'Welcome to The 🥧 Approximator!')
    error_message: str = f'Please enter a whole number between 0 and {LIMIT}...'
    exit_message: str = 'Exiting program...'

    while True:
        try:
            user_input: str = input(
                f'Enter the number of decimal places (up to {LIMIT}): ')

            if user_input == 'exit':
                print(exit_message)
                exit()

            if user_input.isnumeric() and int(user_input) <= LIMIT:
                n: int = int(user_input)
            elif not user_input.isnumeric():
                n: int = w2n.word_to_num(user_input)
                if n > LIMIT:
                    print(error_message)
                    continue
            else:
                print(error_message)
                continue

        except ValueError:
            print(error_message)

        except KeyboardInterrupt:
            print(exit_message)
            exit()

        print(f'π = {PI[:n+2]} (to {n} d.p.)')


if __name__ == '__main__':
    main()
