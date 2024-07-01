import dbconnector
mydb=dbconnector.connect()
cursor = mydb.cursor()
def currAvailibility():
  cursor.execute(" select rooms.roomNo,roomCategories.categoryname,roomcategories.roomprice from rooms join roomcategories on rooms.roomcategid=roomcategories.categoryID where rooms.roomNo not in(select roomno from roombooked);")
  roomsAvailable=cursor.fetchall()
  return roomsAvailable

def printRooms():
  roomsAvailable=currAvailibility()
  if len(roomsAvailable)==0:
    print("----Sorry no rooms available !")
    return False
  else:
    print("--->Rooms available are:")
    for room in roomsAvailable:
      for det in room:
        print("\t",det,end="")
      print("\n")
    return True