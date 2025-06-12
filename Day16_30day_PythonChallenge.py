
# Generator function to produce 'n' Fibonacci numbers
def fib_seq(n: int):
    a, b = 0, 1  
    for _ in range(n): 
        yield a         
        a, b = b, a + b 

n = int(input("Enter the number: ")) #input


print(f"The first {n} Fibonacci numbers are:") #output

for f in fib_seq(n):
    print(f) #output