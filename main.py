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
    # Main loop that continues until the user decides to exit
    while True:
        read_file = None
        # Keep looping until a valid dish is selected or the user decides to exit
        while not read_file:
            dinner.display_menu()
            # Get the user's choice and the corresponding dish name and data
            read_file = dinner.choose_protein()
            # If the user decides to exit, break out of the main loop
            if read_file == "exit":
                return

        # Unpack dish name and data from the read_file variable
        dish_name, dish_data = read_file
        print(f"\nDish selected: {dish_name}\n")

        while True:
            # Prompt the user for their desired action
            action = input("Enter 'R' to view recipe, 'I' to view ingredients, or 'G' to go back to menu: ").lower()
            # Show the recipe if the user enters 'r'
            if action == 'r':
                dinner.show_recipe(dish_data)
            # Show the ingredients if the user enters 'i'
            elif action == 'i':
                dinner.show_ingredients(dish_data)
            # Break out of the inner loop and return to the menu if the user enters 'g'
            elif action == 'g':
                break
            else:
                print("Invalid input. Please try again.")


main()

