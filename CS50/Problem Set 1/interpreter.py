e=input("Enter Expression: ").split(" ")
if e[1]=="+":
    print(float(e[0])+float(e[2]))
elif e[1]=="-":
    print(float(e[0])-float(e[2]))
elif e[1]=="*":
    print(float(e[0])*float(e[2]))
elif e[1]=="/":
    if float(e[2])==0:
        print("Division by 0")
    else:
     print(float(e[0])/float(e[2]))
elif e[1]=="//":
    if float(e[2])==0:
        print("Division by 0")
    else:
        print(float(e[0])//float(e[2]))
elif e[1]=="**":
    print(float(e[0])**float(e[2]))
else:
    print("Invalid Symbol")