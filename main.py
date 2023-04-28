from dinner import Dinner

dinner = Dinner()


def main():
    dinner.display_menu()
    read_file = None
    while not read_file:
        read_file = dinner.choose_protein()

    print(read_file)


main()
