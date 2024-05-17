def HI():
    name=input("Your name: ")
    age=input("Your birthday: ")
    amount=input("How much money do you have (EUR) ? :")
    
    age=2022-int(age)
    UsdConver=float(amount)*1.01326
    print(f'HI {name}  and has {age} years old and {UsdConver}$ in my pocket ')
    
    
def Cara():
    text="Hello Mister, How are you today ?"
    print(text.find("Mister"))
    

    
def Fib(n):
    if n==0:
        return 0
    elif n<=2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
    
#HI()
#Cara()

     
dict= {
    "Rachid": 1336542,
    "Rf":3
}

print(dict["Rachid"])

    

 