#This Program for Water Jug problem
x=0 #current state of jug1
y=0 #current state of jug2
m=5 #capacity of jug 1
n=3 #capacity of jug 2
t=0
print("Initial State",(x,y))
print("Capacity of Jug",(m,n))
print("Rule 1 : Completely Fill jug 1")
print("Rule 2 : Completely Fill jug 2")
print("Rule 3 : Fill some Water to Jug 2 from jug 1 ")
print("Rule 4 : Fill some Water to Jug 1 from jug 2 ")
print("Rule 5 : Fill Complete Water to Jug 1 from jug 2 ")
print("Rule 6 : Fill Complete Water to Jug 2 from jug 1 ")
print("Rule 7 : Empty Whole Jug 2 ")
print("Rule 8 : Empty Whole Jug 1 ")
while(x!=4):
    rule=int(input("Enter Rule:"))
    if(rule==1):
        x=m;
    elif(rule==2):
        y=n;
    elif(rule==3):
        t=n-y;
        y=n;
        x-=t;
    elif(rule==4):
        t=m-x;
        x=m;
        y-=t;
    elif(rule==5):
        x+=y;
        y=0;
    elif(rule==6):
        y+=x;
        x=0;
    elif(rule==7):
        y=0;
    elif(rule==8):
        x=0;
    else:
        print("Not Exactly");
    print("Jug 1 Water,Jug 2 Water",(x,y))
        
