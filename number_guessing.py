import random


def get_guess(low, high):
    while True:
        raw = input(f"Your guess ({low}-{high}): ").strip()
        if raw.isdigit() and low <= int(raw) <= high:
            return int(raw)
        print(f"Please enter a whole number between {low} and {high}.")


def play_round(low=1, high=100, max_attempts=7):
    secret = random.randint(low, high)
    print(f"\nI'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts.\n")

    for attempt in range(1, max_attempts + 1):
        guess = get_guess(low, high)
        if guess == secret:
            print(f"Correct! You got it in {attempt} attempt(s).")
            return
        print("Too low!" if guess < secret else "Too high!")
        print(f"Attempts left: {max_attempts - attempt}\n")

    print(f"Out of attempts. The number was {secret}.")


def main():
    print("=== Number Guessing Game ===")
    while True:
        play_round()
        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
