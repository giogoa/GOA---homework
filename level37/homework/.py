fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)

print(fruits[0])
print(fruits[-1])

fruits.append("fig")
fruits.remove("banana")
fruits[1] = "blueberry"
print(len(fruits))

#2
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]


numbers.append(100)


numbers.insert(0, 5)

numbers.remove(30)


numbers.sort()


numbers.reverse()


index_of_50 = numbers.index(50)
print(index_of_50)


count_of_20 = numbers.count(20)
print(count_of_20)
#3
numbers = list(range(1, 11))

first_half = numbers[:5]
second_half = numbers[5:]

squares = [x**2 for x in numbers]

print("First half:", first_half)
print("Second half:", second_half)
print("Squares:", squares)
