def add_expense():
    date=date(input())
    category=input()
    amount=float(input())
    description=input()
    expense={
        "date":date,
        "category":category,
        "amount":amount,
        "description":description
    }