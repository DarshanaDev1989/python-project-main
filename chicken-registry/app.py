chickens=["George", "Fleur", "Devon", "Casey", "Marigold","Apple Mint"]
def read():
    if not chickens:
        print("No chicken data found")
    else:
        for i in chickens:
            print(i)
def create():
    chicken=input("enter the chicken name ")
    chickens.append(chicken)
    print("Chicken added successfully")
def update():
    chicken=input("enter the chicken name")
    if chicken in chickens:
        print("Chicken found")
        chicken1=input("enter the new chicken name")
        index=chickens.index(chicken)
        chickens[index]=chicken1
        print("Chicken updated successfully")
    else:
        print("Chicken not found")
def delete():
    chicken=input("enter the chicken name")
    if chicken in chickens:
        index=chickens.index(chicken)
        del chickens[index]
        print("Chicken deleted successfully")
    else:
        print("Chicken not found")
print("Enter the choice you want to perform")
ch=int(input("Enter the choice " \
"0:exit the app"
"1:to read the chichen data " \
"2:to write chicken data " \
"3:to update chicken data " \
"4:to delete chicken data " \
))
if  ch==0:
    print("exit the app")
elif ch==1:
    read()
elif ch==2:
    create()
elif ch==3:
    update()
elif ch==4:
    delete()
else:
    print("invalid choice")