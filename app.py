from datetime import datetime
import csv 
import os
import matplotlib.pyplot as plt

categories = {
    1: "Food",
    2: "Travel",
    3: "Bills",
    4: "Shopping",
    5: "Health",
    6: "Education",
    7: "Entertainment",
    8: "Investment",
    9: "Other"
}


file_name = "expenses.csv"
#creating expenses file if not available
if not os.path.exists(file_name):
    with open(file_name, mode='w', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    try:
        date = datetime.strptime(input("Enter date (DD-MM-YYYY): "), "%d-%m-%Y").date()
        category_no = int(input(
            "1: Food\n"
            "2: Travel\n"
            "3: Bills\n"
            "4: Shopping\n"
            "5: Health\n"
            "6: Education\n"
            "7: Entertainment\n"
            "8: Investment\n"
            "9: Other\n"
            "Choose the category from above: "))
        category=categories[category_no]
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


def monthly_summary(ret_data=False):
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

    highest = max(category_wise_amount, key=category_wise_amount.get)
    lowest = min(category_wise_amount, key=category_wise_amount.get)


    if(ret_data):
        return category_wise_amount, time_period  , total_spending
    

    print(f"\nMonthly Summary for {time_period}:")
    print(f"Total spending: {total_spending:.2f}")
    print("Spending by category:")
    for cat, amt in category_wise_amount.items():
        print(f"{cat}: {amt:.2f}")

   
    print(f"\nHighest spending category: {highest} ({category_wise_amount[highest]:.2f})")
    print(f"Lowest spending category: {lowest} ({category_wise_amount[lowest]:.2f})")

    return 

def overall_summary(ret_data=False):
    total_spending = 0
    category_wise_amount = {}

    with open(file_name, 'r') as file:
        next(file)  # skip header
        for line in file:
            date_str, category, amount_str, description = line.strip().split(',')
            amount = float(amount_str)

            total_spending += amount
            category_wise_amount[category] = category_wise_amount.get(category, 0) + amount

    if total_spending == 0:
        print("No expenses recorded yet.")
        return

    highest = max(category_wise_amount, key=category_wise_amount.get)
    lowest = min(category_wise_amount, key=category_wise_amount.get)

    if(ret_data):
        return category_wise_amount , total_spending
    
    print("\nOverall Expense Summary:")
    print(f"Total spending: {total_spending:.2f}")
    print("Spending by category:")
    for cat, amt in category_wise_amount.items():
        print(f"{cat}: {amt:.2f}")

    
    print(f"\nHighest spending category: {highest} ({category_wise_amount[highest]:.2f})")
    print(f"Lowest spending category: {lowest} ({category_wise_amount[lowest]:.2f})")
    return 



def monthly_visual_summary():
    data = monthly_summary(ret_data=True)
    if not data:
        return  

    category_wise_amount, time_period, total_spending = data

    #pie chart
    labels = list(category_wise_amount.keys())
    amounts = list(category_wise_amount.values())

    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f'Monthly Expense Distribution for {time_period}\nTotal: {total_spending:.2f}')
    plt.axis('equal')  #to get cicular pie
    plt.show()


def overall_visual_summary():
    data = overall_summary(ret_data=True)
    if not data:
        return  

    category_wise_amount, total_spending = data

    # pie chart
    labels = list(category_wise_amount.keys())
    amounts = list(category_wise_amount.values())

    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f'Overall Expenses Category wise\nTotal: {total_spending:.2f}\n')
    plt.axis('equal')
    plt.show()

def delete_expense():
    try:
        date_input = input("Enter the date of the expense to delete (DD-MM-YYYY): ")
        date = datetime.strptime(date_input, "%d-%m-%Y").date()
        category_no = int(input(
            "1: Food\n"
            "2: Travel\n"
            "3: Bills\n"
            "4: Shopping\n"
            "5: Health\n"
            "6: Education\n"
            "7: Entertainment\n"
            "8: Investment\n"
            "9: Other\n"
            "Choose the category from above: "))
        category=categories[category_no]
        amount = float(input("Enter the amount of the expense: "))

        # opeing file with read mode 
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Find matching expense
        new_rows = [rows[0]] 
        deleted = False

        for row in rows[1:]:
            row_date = datetime.strptime(row[0], "%d-%m-%Y").date()
            row_category = row[1]
            row_amount = float(row[2])

            if row_date == date and row_category == category and row_amount == amount and not deleted:
                deleted = True  # delete only the first one ( if more than onee is there)
                print(f"Deleted expense: {row_date} | {row_category} | {row_amount} | {row[3]}")
                continue
            new_rows.append(row)

        if not deleted:
            print("No matching expense found.")
            return

        # updating CSV without the deleted expense
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)

    except ValueError:
        print("Invalid input. Please check date format or amount.")
# add_expense()
# view_expenses()
# monthly_summary()
# overall_summary()

# monthly_visual_summary()
# overall_visual_summary()
delete_expense()