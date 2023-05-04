import random
import json


class Dinner:
    """
        Represents a dinner selection system based on protein type.

        The class reads recipe data from JSON files, provides a menu for users to choose a protein,
        and randomly selects a dish based on the user's choice. It also allows users to view the recipe and
        ingredients of the selected dish.

        Attributes:
            protein (dict): A dictionary mapping user input to corresponding JSON files containing recipe data.

        Methods:
            display_menu: Displays the menu options for the user to choose a protein.
            read_file: Reads the recipe data from a JSON file and returns a randomly selected dish name and its data.
            show_recipe: Displays the recipe of the selected dish in a readable format.
            show_ingredients: Displays the ingredients of the selected dish in a readable format.
            choose_protein: Prompts the user to choose a protein and returns the corresponding dish name and data.
        """
    def __init__(self):
        # Initialize the protein attribute with a dictionary mapping user input to corresponding JSON files
        self.protein = {
            "1": "chicken.json",
            "2": "beef.json",
            "3": "fish.json",
            "4": "pork.json",
        }

    def display_menu(self):
        """Displays the menu options for the user to choose a protein."""
        print("Choose your protein between 1-4.")
        print("1. Chicken")
        print("2. Beef")
        print("3. Fish")
        print("4. Pork")
        print("Enter X to exit")

    def read_file(self, filename):
        """Reads the recipe data from a JSON file and returns a randomly selected dish name and its data."""
        with open(filename) as f:
            recipe_book = json.load(f)
            recipes = recipe_book["recipeBook"]["recipes"]
            random_recipe = random.choice(recipes)
            # Return a randomly selected dish name and its data
            return random_recipe["name"], random_recipe

    def show_recipe(self, dish_data):
        """Displays the recipe of the selected dish in a readable format."""
        print("\nRecipe:")
        for index, step in enumerate(dish_data["instructions"], 1):
            print(f"{index}. {step}")
        print()

    def show_ingredients(self, dish_data):
        """Displays the ingredients of the selected dish in a readable format."""
        print("\nIngredients:")
        for ingredient in dish_data["ingredients"]:
            print(f"{ingredient['name']}: {ingredient['quantity']}")
        print()

    def choose_protein(self):
        """Prompts the user to choose a protein and returns the corresponding dish name and data."""
        choice = input("Choose your protein: ")
        # Return exit to quit program if user enters x
        if choice.lower() == "x":
            return "exit"
        # Get the filename associated with the user's choice
        filename = self.protein.get(choice)
        # If a valid choice was made, read the file and return a random recipe name
        if filename:
            return self.read_file(filename)
        else:
            # If the choice is invalid, display an error message and return None
            print("Pick a choice between 1-5.")
            return None
