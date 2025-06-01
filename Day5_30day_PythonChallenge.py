def sum_num(num): #calculating the sum 
    return sum(num)

size = int(input("Enter the number of elements you want in the list: ")) #giving input for size of the list 
 
num = [] #assigning the empty list 

for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    num.append(element) #appending value in the list using above input 

print(f"This is your list of numbers: {num}") #printing the list 

total = sum_num(num) #calling the function for calculating sum
average = total / len(num) #calculating the avaerage

print(f"Sum: {total}") #printing sum
print(f"Average: {average}") #printing average 