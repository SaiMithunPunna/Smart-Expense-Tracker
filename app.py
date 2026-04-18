from datetime import datetime
import csv 
import os

file_name = "expenses.csv"
#creating expenses file if not available
if not os.path.exists(file_name):
    with open(file_name, mode='w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    try:
        date = datetime.strptime(input("Enter date (DD-MM-YYYY): "), "%d-%m-%Y").date()
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


# def monthly_summary():
#     time_period=input("Enter month and year(mm-yyyy) : ")

#     #read file
#     with open(file_name, mode='r') as file:
#         reader=csv.reader(file)
#         rows=list(reader)
#     #total spending in month 

#     #total spending category wise

#     #highest spending category and lowest spending category


def monthly_summary():
    time_period = input("Enter month and year (mm-yyyy): ")
    month, year = map(int, time_period.split('-'))
    if (month>12 and month<1) or (year<1):
        print("Enter valid month. ")
        return
    total_spending = 0
    category_wise_amount = {}

    with open(file_name, 'r') as file:
        next(file)  # skipin column names
        for line in file:
            date_str, category, amount_str, description = line.strip().split(',')
            date = datetime.strptime(date_str, "%d-%m-%Y")
            amount = float(amount_str)

            if date.month == month and date.year == year:
                total_spending += amount
                category_wise_amount[category] = category_wise_amount.get(category, 0) + amount

    if total_spending == 0:
        print(f"No expenses for {time_period}.")
        return

    print(f"\nMonthly Summary for {time_period}:")
    print(f"Total spending: {total_spending:.2f}")
    print("Spending by category:")
    for cat, amt in category_wise_amount.items():
        print(f"{cat}: {amt:.2f}")

    highest = max(category_wise_amount, key=category_wise_amount.get)
    lowest = min(category_wise_amount, key=category_wise_amount.get)
    print(f"\nHighest spending category: {highest} ({category_wise_amount[highest]:.2f})")
    print(f"Lowest spending category: {lowest} ({category_wise_amount[lowest]:.2f})")


def overall_summary():
    total_spending = 0
    category_totals = {}

    with open(file_name, 'r') as file:
        next(file)  # skip header
        for line in file:
            date_str, category, amount_str, description = line.strip().split(',')
            amount = float(amount_str)

            total_spending += amount
            category_totals[category] = category_totals.get(category, 0) + amount

    if total_spending == 0:
        print("No expenses recorded yet.")
        return

    print("\nOverall Expense Summary:")
    print(f"Total spending: {total_spending:.2f}")
    print("Spending by category:")
    for cat, amt in category_totals.items():
        print(f"{cat}: {amt:.2f}")

    highest = max(category_totals, key=category_totals.get)
    lowest = min(category_totals, key=category_totals.get)
    print(f"\nHighest spending category: {highest} ({category_totals[highest]:.2f})")
    print(f"Lowest spending category: {lowest} ({category_totals[lowest]:.2f})")


# add_expense()
# view_expenses()
monthly_summary()