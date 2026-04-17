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
        date = datetime.strptime(input("Enter date (YYYY-MM-DD): "), "%Y-%m-%d")
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

add_expense()
    




