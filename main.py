from dinner import Dinner

"""
This program helps users decide what to have for dinner by offering a selection of dishes based on protein type. 
Users can choose between chicken, beef, fish, and pork dishes. The program then randomly selects a dish and 
displays its name. Afterward, users have the option to view the recipe, view the ingredients, 
or return to the main menu and choose a different protein.

Usage:
1. Run the program.
2. Choose a protein option (1 - Chicken, 2 - Beef, 3 - Fish, 4 - Pork) or press 'X' to exit.
3. The program will display a randomly selected dish based on the chosen protein.
4. Enter 'R' to view the recipe, 'I' to view the ingredients, or 'G' to return to the main menu.
5. Repeat steps 2-4 as desired or press 'X' to exit the program.
"""

dinner = Dinner()

print("Welcome to Whats for dinner!")


# main loop
def main():
    while True:
        read_file = None
        while not read_file:
            dinner.display_menu()
            read_file = dinner.choose_protein()
            if read_file == "exit":
                return
        dish_name, dish_data = read_file  # Unpack dish name and data
        print(f"\nDish selected: {dish_name}\n")

        while True:
            action = input("Enter 'R' to view recipe, 'I' to view ingredients, or 'G' to go back to menu: ").lower()
            if action == 'r':
                dinner.show_recipe(dish_data)
            elif action == 'i':
                dinner.show_ingredients(dish_data)
            elif action == 'g':
                break
            else:
                print("Invalid input. Please try again.")


main()

