a = int(input("Enter a number: ")) #giving input

count = 0

for i in range(1,a+1): #loop for calculating the divisors
    if a%i==0:
        count = count + 1

if count==2:  #output using if else condition
    print(f"{a} is a prime number")
else:
    print(f"{a} is not a prime number!")
