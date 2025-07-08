def show_menu():

    print("1.Add Expenses")
    print("2.View Total")
    print("3.View Expenses by category")
    print("4.Exit")

def get_user_choice():

    choice = input("Enter your choice from 1 to 4:")
    return choice

def add_expense():
    amount = float(input("Enter amount:"))
    category = input("Enter category:")
    description = input("Enter a short description:")
    
    return{"amount":amount, "category":category, "description":description}

def save_expense(expense, expenses_list):
    expenses_list.append(expense)
    return(expenses_list)

def calculate_total(expenses_list):
    total = 0
    for expense in expenses_list:
        total += expense["amount"]
        return(total)
    
def show_total(total):

    print(f"Show the total:{total:.2f}")

def get_expenses_by_category(expenses_list, category):
    pass

def show_expenses(expenses_list):
    for expense in expenses_list:
        print(f"{expense['amount']}")
        print(f"{expense['category']}")
        print(f"{expense['description']}")


def get_all_categories(expenses_list):
    pass

def show_category_report(expenses_list):
    pass

def exit_program():
    print("Exiting Program")

def handle_choice(choice, expenses_list):
    if choice == '1':
        expense = add_expense()
        save_expense(expense,expenses_list)
    elif choice =='2':
        total = calculate_total(expenses_list)
        show_total(total)
    elif choice == '3':
        category = get_category_input()
        get = get_all_categories(expenses_list)
        show_category_report(get)
    elif choice == '4':
        exit_program()
    else:
        print("invalid choice")


def main():
    pass

def valid_choices(choice):
    pass

def get_category_input():
    cat = input("Enter category name:")
    return cat