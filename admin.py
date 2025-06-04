from data import connection

def admin():
    conn = connection()
    cursor = conn.cursor()
    while True:
        print("\nAdmin Menu:")
        print("1. Login Account")
        print("2. Balance Amount")
        print("3. Deposit Amount")
        print("4. Withdraw Amount")
        print("5. Logout")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            login_account(conn, cursor)
        elif ch == 2:
            balance_amount(conn, cursor)
        elif ch == 3:
            deposite_amount(conn, cursor)
        elif ch == 4:
            withdraw_amount(conn, cursor)
        elif ch == 5:
            logout()
            break
        else:
            print("not-valid choice. Please try again.")

def login_account(conn, cursor):
    account_number = input("enter account number: ")
    password = input("enter password: ")
    query = "select * from bankingsystem3 where account_number = %s and password = %s"
    values = (account_number, password)
    cursor.execute(query, values)
    if cursor.fetchone():
        print("Login successful")
    else:
        print("Invalid account number or password")
def balance_amount(conn, cursor):
    account_number = input("Enter account number: ")
    query = "select balance_amount from bankingsystem3 where account_number = %s"
    values = (account_number,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    if result:
        print(f"Balance_amount: {result[0]}")
    else:
        print("Account not found")

def deposite_amount(conn, cursor):
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    query = "update bankingsystem3 set balance_amount = balance_amount + %s where account_number = %s"
    values = (amount, account_number)
    cursor.execute(query, values)
    conn.commit()
    print("Deposit successful")
def withdraw_amount(conn,cursor):
    account_number = input("Enter account number: ")
    amount = int(input("Enter amount to withdraw: "))
    # fetch existing balance amount(stor in varaible)
    # exitiging_ balance-amount= final _balance:
    # u[date the balaance amoiunt with fina1la]
    query = "update bankingsystem3 set balance_amount = balance_amount = %s where account_number = %s"
    values = (amount, account_number)
    cursor.execute(query, values)
    # if cursor.fetchone()>amount:
    #     print("Account not found")
    # elif cursor.fetchone < amount:
    #     print("Insufficient balance")
    # else:
    cursor.execute(query, values)
    conn.commit()
    print("Withdrawal successful")


def logout():
    print("logging out...")

if __name__ == "__main__":
    admin()