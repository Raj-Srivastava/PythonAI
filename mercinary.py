#This Program for Mercinary Cannible problem
mr=3   #Mercinary Right 
cr=3   #cannibles Right
ml=0   #Mercinary Left
cl=0   #Cannibles Left
print("Current state in right side",(mr,cr))
print("Goal State in left side",(mr,cr))
print("Current state in left side",(ml,cl))
print("Rule 1 : Send two Cannibles from right to left")
print("Rule 2 : Send two mercinary from right to left")
print("Rule 3 : Send one mercinary and one cannibles from right to left")
print("Rule 4 : Send one mercinary and one cannible from left to right")
print("Rule 5 : Send two mercinary from left to right")
print("Rule 6 : Send two cannible from left to right")
print("Rule 7 : Send one cannibles from left to right")
print("Rule 8 : Send one mercinary from left to right")
print("Rule 9 : Send one mercinary from right to left")
print("Rule 10 : Send one cannibles from right to left")
while((ml!=3)or(cl!=3)):
    rule=int(input("Enter Rule : "))
    if(rule==1):
        cl+=2
        cr-=2
        print("Right to Left")
    elif(rule==2):
        ml+=2
        mr-=2
        print("Right to Left")
    elif(rule==3):
        mr-=1
        cr-=1
        ml+=1
        cl+=1
        print("Right to Left")
    elif(rule==4):
        mr+=1
        cr+=1
        ml-=1
        cl-=1
        print("Left to Right")
    elif(rule==5):
        ml-=2
        mr+=2
        print("Left to Right")
    elif(rule==6):
        cl-=2
        cr+=2
        print("Left to Right")
    elif(rule==7):
        cl-=1
        cr+=1
        print("Left to Right")
    elif(rule==8):
        ml-=1
        mr+=1
        print("Left to Right")
    elif(rule==9):
        mr-=1
        ml+=1
        print("Right to Left")
    elif(rule==10):
        cr-=1
        cl+=1
        print("Right to Left")
    else:
        print("Rule Not Defined")
    if(((ml!=0)and(ml<cl))or((mr!=0)and(mr<cr))):
        print("Dead")
        break
    print(mr,cr)
    print(ml,cl)
print("Goal Reached")
