from dinner import Dinner

dinner = Dinner()

print("Welcome to Whats for dinner!")


# main loop
def main():
    while True:
        read_file = None
        while not read_file:
            dinner.display_menu()
            read_file = dinner.choose_protein()
            # TODO: add save option
            # exit the loop and program if user enters exit
            if read_file == "exit":
                return
        # show the randomly selected dish to user
        print(f"\nDish selected: {read_file}\n")


main()
