a = int(input())
b = int(input())

fun = input()

if (fun == "a"):
    addition(a,b)

elif (fun == "s"):
    subtraction(a,b)
elif (fun == "m"):
    multiplication(a,b)

elif(fun == "d"):
    Division(a,b)

def Division(a,b):
    print(a/b)            