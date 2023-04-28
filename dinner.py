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
        print("Welcome to Whats for dinner!")
        print("Choose your protein")
        print("1. Chicken")
        print("2. Beef")
        print("3. Fish")
        print("4. Pork")

    @staticmethod
    def read_file(filename):
        with open(filename) as f:
            recipe_book = json.load(f)
            recipes = recipe_book["recipeBook"]["recipes"]
            random_recipe = random.choice(recipes)
            return random_recipe["name"]

    def choose_protein(self):
        choice = input("Choose your protein: ")
        filename = self.protein.get(choice)
        if filename:
            return self.read_file(filename)
        else:
            print("Pick a choice between 1-5.")
            return None
