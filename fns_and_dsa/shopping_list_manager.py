def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    exit = False
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add = input("Enter the item to be added: ")
            shopping_list.append(add)

            pass
        elif choice == '2':

            # Prompt for and remove an item
            remove_item = input("Which item do you want to remove? ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
            else:
                print("Item not in list.")
                pass
            pass
        elif choice == '3':
            print(shopping_list[:])
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
