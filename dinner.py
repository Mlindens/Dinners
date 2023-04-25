import random


class Dinner:
    def __init__(self):
        self.protein = {
            "1.": "chicken.txt",
            "2.": "beef.txt",
            "3.": "fish.txt",
            "4.": "turkey.txt",
        }

    def display_menu(self):
        print("Welcome to Whats for dinner!")
        print("Choose your protein")
        print("1. Chicken")
        print("2. Beef")
        print("3. Turkey")
        print("4. Steak")
        print("5. Fish")

    def read_file(self, filename):
        with open(filename) as f:
            words = f.readlines()
            words = [word.split() for word in words]
            return random.choice(words)

    def choose_protein(self):
        choice = input("Choose your protein: ")
        filename = self.protein.get(choice)
        if filename:
            return self.read_file(filename)
        else:
            print("Pick a choice between 1-5.")
            return None