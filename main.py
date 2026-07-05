## EXPENSE TRACKER PROJECT

expenseslist =  [] ##list of all expenses in form or dictonary

print("Welocome to Expense Tracker : ")

while True:
    print("========MENU=========")
    print("1. Add Expense : ")
    print("2. View All Expenses list : ")
    print("3. view all Expense : ")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))

# Add Expense
    if(choice==1):
        date = input("Enter the date : ")
        category = input("Enter category (like FOOD,TRAVEL,MAKEUP,BOOKS) : ")
        description = input("Enter category detail : ")
        amount = int(input("Enter amount : "))

        expense ={
            "date":date,
            "category": category,
            "description": description,
            "amount" : amount
        }

        expenseslist.append(expense)
        print("\n Expense is added Succesfully")

# 2. View All Expenses
    elif(choice==2):
        if(len(expenseslist)==0):
            print("No Expenses Added")
        else :
            print("===List Of Expense===")
            count = 1
            for eachKharcha in expenseslist:
                print(f"Kharcha Number{count} -> {eachKharcha["date"]},{eachKharcha["category"]}, {eachKharcha["description"]}, {eachKharcha["amount"]}")
                count = count+1

# 3.View Total Spending
    elif(choice == 3):
        total = 0
        for eachkharcha in expenseslist:
            total = total + eachkharcha["amount"]

        print("\n TOTAL EXPENSE = ",total) 

# 4.Exit
    elif(choice == 4):
        print("Thank you")
        break

    else:
        print("Invalid choice. Try Again")


