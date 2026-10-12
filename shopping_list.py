
# Part B: Shopping List Manager

shopping_list = [{"item": "bread", "quantity": 2}, {"item": "milk", "quantity": 1}, {"item": "eggs", "quantity": 12}]

while True:
    print("\n--- Shopping List Menu ---")
    print("add / remove / show / done")

    choice = input("What would you like to do? ").strip().lower()

    if choice == "add":
        item = input("Enter the item to add: ").strip()

        if item:
            shopping_list.append({"item": item, "quantity": 1})
            print(item, "has been added to your list.")
        else:
            print("Please enter an item.")

    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if shopping_list:
            print("\nYour shopping list:")
            for item in shopping_list:
                print(item)
        else:
            print("Your shopping list is empty.")

    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break

    else:
        print("Invalid choice. Please enter add, remove, show, or done.")