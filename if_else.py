n1=int(input("Number1: "))
n2=int(input("Number2: "))
n3=int(input("Number3: "))
if((n1>n2) and (n1>n3)):
    print("Number1 greater")
elif((n2>n1) and (n2>n3)):
    print("Number2 greater")
elif((n3>n1) and (n3>n2)):
    print("Number3 greater")
