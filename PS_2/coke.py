amountDue = 50
while amountDue > 0:
    print("Amount Due:", amountDue)
    coinUsed = int(input("Insert coin: "))
    if coinUsed in [25, 10, 5]:
        amountDue = amountDue - coinUsed

change = abs(amountDue)
print("Change Owed:", change)