import random

def get_random_greeting():
    greetings = [
        "You're doing great!",
        "Keep up the awesome work!",
        "You've got this!",
        "Today is your day!",
        "You make a difference!"
    ]
    return random.choice(greetings)

def main():
    name = input("What's your name? ")
    print(f"Hello, {name}!")
    print(get_random_greeting())

if __name__ == "__main__":
    main()