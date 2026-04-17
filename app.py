from datetime import datetime
def add_expense():
    try:
        date = datetime.strptime(input("Enter date (YYYY-MM-DD): "), "%Y-%m-%d")
        category=input("Enter the category : ")
        amount=float(input("Enter the expense : "))
        description=input("Enter description og ")
    except ValueError:
        print("Enter valid details.")
    expense={
        "date":date,
        "category":category,
        "amount":amount,
        "description":description
    }
    

