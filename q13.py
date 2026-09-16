#13. Write a Python program to simulate an ATM withdrawal by accepting a PIN, account balance, and withdrawal amount. Validate the transaction and display an appropriate message.

pin = 7860
balance = 55000

enter_pin = int(input("Enter your ATM PIN: "))
if enter_pin == pin:
    print("Pin verified Successfully...")
    print("Acount Balance: ",balance)

    withdrawl_amt = int(input("Enter Withdrawl Amount: "))
    if withdrawl_amt <= balance:
        balance -= withdrawl_amt
        print("Transaction Successful")
        print("Balance: ",balance)
    else:
        print("Insufficient Balance!!!")
        print("Transaction Failed")
else:
    print("Incorrect Pin!!\nAccess Denied ")

