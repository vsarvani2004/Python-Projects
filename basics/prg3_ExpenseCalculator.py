expenses = []
while True:
    print(" 1. Enter new expense\n 2.Total expenses\n 3. View Expenses\n 4.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        expenses.append({"amount": amount, "category": category})
        print("Expense added successfully!")
    elif choice == '2':
        total = 0
        for expense in expenses:
            total += expense['amount'] 
        print(f"Total expenses: {total}")
    elif choice == '3':
        if not expenses:
            print("No expenses recorded")
        else:
            print("Your expenses:")
            for expense in expenses:
                i = expenses.index(expense)
                print(f"{i+1}. Amount: {expense['amount']}, Category: {expense['category']}")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")