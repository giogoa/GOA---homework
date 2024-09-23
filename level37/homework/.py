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

print(first_half)
print(second_half)
print(squares)
#4
temperatures = [72, 68, 75, 70, 78, 74, 71]

highest_temp = max(temperatures)
print("Highest temperature:", highest_temp)

lowest_temp = min(temperatures)
print("Lowest temperature:", lowest_temp)

average_temp = sum(temperatures) / len(temperatures)
print("Average temperature:", average_temp)

above_70 = [temp for temp in temperatures if temp > 70]
print("Temperatures above 70:", above_70)
