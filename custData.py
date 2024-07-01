import dbconnector
mydb=dbconnector.connect()
cursor = mydb.cursor()
def askData():
    bookerId=int(input("\n-----Enter BookerId: "))
    numOfBoarders=int(input("----Number of boarders :"))
    boarderInfoList=[]
    for i in range(numOfBoarders):
        print("--->boarder ",i+1,"---")
        boardersName=input("----Enter name of boarder :")
        t1=(boardersName,)
        boardersAge=int(input("----Age :"))
        t2=(boardersAge,)
        t3=(bookerId,)
        custList=t1+t2+t3
        boarderInfoList.append(custList)
    dbPush(boarderInfoList,bookerId)
def dbPush(boarderInfoList,bookerId):
    bookerName=boarderInfoList[0][0]
    if checkBooker(bookerId)==0:
        query=f"insert into bookerdetails values({bookerId},'{bookerName}',0)"
        cursor.execute(query)
        mydb.commit()
    query="insert into boarders (boarderName,boarderage,bookerid) values(%s,%s,%s)"
    cursor.executemany(query,boarderInfoList)
    mydb.commit()
def checkBooker(bookerId):
    query=f"select exists (select bookerID from bookerdetails where bookerID={bookerId})"
    cursor.execute(query)
    checker=cursor.fetchone()[0]
    return checker
