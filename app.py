from datetime import datetime
import csv 
import os

file_name = "expenses.csv"


def add_expense():

    #creating expenses file if not available
    if not os.path.exists(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer=csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    try:
        date = datetime.strptime(input("Enter date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        category=input("Enter the category : ")
        amount=float(input("Enter the expense : "))
        description=input("Enter description og ")

        # adding data to the expenses file
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])
        print("added new expense")

    except ValueError:
        print("Enter valid details.")
    return 

def view_expenses():
    if not os.path.exists(file_name):
        print("No expenses found.")
    with open(file_name, mode='r') as file:
        reader=csv.reader(file)
        rows=list(reader)

        if len(rows)<=1:
            print("No enpenses added.")
            return 
    print("\n...All expenses...")
    print("S.no \tDate \tCategory \tAamount \tDescription")
    for i in range(1, len(rows)):
        single_row = rows[i]

        date = single_row[0]
        category = single_row[1]
        amount = single_row[2]
        description = single_row[3]

        print(i,"\t", date,"\t", category,"\t", amount,"\t", description)
add_expense()
view_expenses()




