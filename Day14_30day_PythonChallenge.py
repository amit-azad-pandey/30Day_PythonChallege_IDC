def factorial(n):          #function 
    if (n==0 or n==1):
        return 1
    return n * factorial(n-1)   #Recursive call in return statement 


number=int(input("Enter the number: ")) #input
result=factorial(number) #function call
print(f"Factorial of {number}= {result}")  #output