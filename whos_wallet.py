import random

print("Welcome to 'Whose Wallet?'")
names = input("Enter names separated by a comma and a space (e.g., Alice, Bob, Charlie): ")
list_names = names.split(", ")

if len(list_names) < 2:
    print("Please enter at least two names.")
else:
    chosen = random.choice(list_names)
    print(f"Please ask {chosen} to take their wallet out. Dinner is on them!")
