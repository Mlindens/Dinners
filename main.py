import random



def test():
    print("Welcome to Whats for dinner!")
    # read item from file and save in var
    # with open("test.txt") as file:
    #    item = file.readlines()
    # strip the item and save as another var
    # food = item[0].strip()

    # print the food
    # print(f"Your last dinner was {food}")
    print("1. Chicken")
    print("2. Beef")
    print("3. Turkey")
    print("4. Steak")
    print("5. Fish")
    choice = input("Choose a protein: ")

    if choice == "1":
        with open('chicken.txt', 'r') as f:
            words = f.readlines()

            # remove newline characters from each word
            words = [word.strip() for word in words]

            # randomly select a word from the list
            random_word = random.choice(words)
    elif choice == "2":
        with open("beef.txt") as f:
            words = f.readlines()
            words = [word.strip() for word in words]
            random_word = random.choice(words)

    print(random_word)


test()
