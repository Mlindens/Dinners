import random
import json


class Dinner:
    def __init__(self):
        self.protein = {
            "1": "chicken.json",
            "2": "beef.json",
            "3": "fish.json",
            "4": "pork.json",
        }

    @staticmethod
    def display_menu():
        print("Choose your protein between 1-4.")
        print("1. Chicken")
        print("2. Beef")
        print("3. Fish")
        print("4. Pork")
        print("Press S to save")
        print("Press X to exit")

    @staticmethod
    def read_file(filename):
        with open(filename) as f:
            recipe_book = json.load(f)
            recipes = recipe_book["recipeBook"]["recipes"]
            random_recipe = random.choice(recipes)
            return random_recipe["name"]

    def choose_protein(self):
        choice = input("Choose your protein: ")
        # return exit to quit program if user enters x
        if choice.lower() == "x":
            return "exit"
        # get the filename associated with the user's choice
        filename = self.protein.get(choice)
        # if a valid choice was made, read the file and return a random recipe name
        if filename:
            return self.read_file(filename)
        else:
            # if the choice is invalid, display an error message and return None
            print("Pick a choice between 1-5.")
            return None
