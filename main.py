from database import create_tables, add_transaction, get_all_transactions, delete_transaction
from utils import valid_date

def menu():
    print("\n--- Finance Tracker ---")
    print("1) Add Transaction")
    print("2) Show All Transactions")
    print("3) Delete Transaction")
    print("0) Exit")

def run_app():
    create_tables()

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            typ = input("Type (income/expense): ").lower()
            date = input("Date (YYYY-MM-DD): ")

            if not valid_date(date):
                print("❌ Invalid date format")
                continue

            desc = input("Description: ")

            add_transaction(amount, category, typ, date, desc)
            print("✔️ Added Successfully")

        elif choice == "2":
            data = get_all_transactions()
            for row in data:
                print(row)

        elif choice == "3":
            id_to_delete = int(input("Enter ID to delete: "))
            delete_transaction(id_to_delete)
            print("✔️ Deleted Successfully")

        elif choice == "0":
            break

        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    run_app()