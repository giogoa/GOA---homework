#1)
for i in range(23):
    print(i)
    
#2)
for i in range(12):
    print("GOA is best")
    
#3)
for i in range(23):
    print()
    
#4)
for i in range(1 , 35 , 5):
    print(f"this is numbers {i}")
    
#5)
number = int(input("enter time: "))
while number >= 0:
    number = number - 1
    print(number + 1)

#6)
for i in range(7):
    for x in range(6):
        print(f"i={i}, j={x}")
        
#7)
for i in range(1, 6):
    print(f"{i} squared is {i ** 2}")

#8)
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

#9)
numbers = list(range(4))
print(numbers)

#10)
for i in range(1, 10, 3):
    print(i)
