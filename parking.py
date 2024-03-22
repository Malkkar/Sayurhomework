import random
val=False
idData=[]
parkinglot=[[]]
#initilization parkng lot
def initPark( ):
    row=int(input("Enter The Row to Initial"))
    col=int(input("enter The Column "))
    parkinglot =[[0]*col]*row
    
#parking entry
def enterPark( ):
    r,c=int(input("enter the row and column to park"))
    if parkinglot !=0:
       parkinglot[r][c]=0
       id=random.randint(0,9)+random.randint(0,9)+ord(random.randint(0,9))
       idData=idData+id
       print("your parking lot is booked")
       print("your id is ",id)
    else:
       print("this lot is not available")
    	   
    	   
  #leaveparking
def enterPark( ):
    for check in idData:
      if check==id:
          val=True
      else :
          val=False
    if val==True :
      Row=int(input("enter the roe of your lot"))
      Col=int(input("enter the column of your"))
      parkinglot[Row][Col]=0
      print("you can leave")
    else:
        print("your id doen,t match")
     	
     	
     	
def main( ):
    ch=int(input("enter your choice"))
    print("1.initialize park")
    print("2.entering parking")
    print("3.leaveparking")
    print("4.exit")
    while(ch!=4):
        if ch==1:
            initPark( )
        elif ch==2:
            enterPark( )
        elif ch==3:
            enterPark( )
        else :
            exit()
       
       
       