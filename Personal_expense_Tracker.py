import time

expenses_list = []

def add_expense():
    name = input('Enter name of expense: ')
    amount = float(input('Enter expense amount: '))
    category = input('Enter expense category: ')

    expense_dict = {
        'name':name,
        'amount':amount,
        'category':category
    }

    expenses_list.append(expense_dict)


def view_expense():
    total = 0
    for index, expense in enumerate(expenses_list,1):
        print(f"{index}. {expense['name']}-{expense['amount']}({expense['category']}) ")
        total += expense['amount']
    print(f'\n Total:{total}')


def view_category_summary():
    category_total = {}

    for expense in expenses_list:
        category = expense['category']
        amount = expense['amount']

        category_total[category] = category_total.get(category,0)+amount 

    for category, total in category_total.items():
        print(f"{category}:${total}")



def main_menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
            time.sleep(2.5)
        elif choice == '3':
            view_category_summary()
            time.sleep(2.5)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

main_menu()