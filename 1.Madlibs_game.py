print("\n=== MAD LIBS: CHAOS EDITION ===\n")

name = input("What is your name? ")
print(f"\nWelcome aboard, {name}. Let's generate some nonsense.\n")

# Inputs
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
adj3 = input("Enter one more adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
place = input("Enter a place: ")
emotion = input("Enter an emotion: ")

# Story
print("\n--- YOUR STORY ---\n")

print(f"Once upon a time, in the middle of {place}, there lived a very {adj1} idiot named {name}.")
print(f"Everyone knew {name} for being unusually {adj2} and slightly unpredictable.")

print(f"\nOne fine morning, {name} stumbled upon a {noun1}.")
print(f"It looked {adj3}, so without thinking twice, {name} {verb1}ed it.")

print(f"\nSuddenly, a wild {noun2} appeared out of nowhere.")
print(f"Panicking, {name} decided to {verb2} as fast as possible.")

print(f"\nAfter all that chaos, {name} felt extremely {emotion}.")
print("Instead of learning a lesson, however,")
print(f"{name} smiled confidently and decided to do everything again the very next day.")

print("\nMoral of the story?")
print("Think twice. Or don’t. Some people are just built different.\n")

# Replay option
choice = input("Do you want to play again? (yes/no): ").lower()
if choice == "yes":
    print("\nRestart the program and unleash chaos again. 💥")
else:
    print("\nThanks for playing. Productivity has officially decreased. Mission accomplished.")
