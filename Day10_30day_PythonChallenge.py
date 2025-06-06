try:
    with open("books.txt") as f:
        x = f.read().split()
        for i in x:
            try:
                num = float(i)  
                print(f'{num} is a number')
            except ValueError:
                print(f"Error: {i}")
except FileNotFoundError:
    print("Error: File does not exist")

print("Sucessful !!")