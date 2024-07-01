amt=float(input("Enter Amount:"))
cash=float(input("Enter amount paid in cash :"))
denominations=(500,200,100,50,20,10,5,2,1,0.5)
change=cash-amt
changeQueue=[]
i=0
while change!=0:
    note=denominations[i]
    while note>change:
        i=i+1
        note=denominations[i]
    if note<change:
        changeQueue.append(note)
        change=change-note
    if note==change:
        changeQueue.append(note)
        change=change-note
print(changeQueue)
    


