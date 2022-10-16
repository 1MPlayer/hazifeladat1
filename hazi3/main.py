def osztas(a,b):
    while (a !=0):
        print(a/b)
        print("Out of try exept block")

        a = int(input("Enter 'a' value:"))
        b = int(input("Enter 'b' value:"))
        if (b == 0):
            print("Division by 0 is not allowed")
            print("Out of try exept block")
        else:
            osztas(a, b)

if __name__=="__main__":
    a=int(input("Enter 'a' value:"))
    b=int(input("Enter 'b' value:"))
    if(b==0):
        print("Division by 0 is not allowed")
        print("Out of try exept block")
    else:
        osztas(a,b)
