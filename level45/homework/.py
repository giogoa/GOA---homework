#1
def word_count(text):
    words = text.split()  
    return len(words)


text = "ეს არის მაგალითი ტექსტი"
print(f"სიტყვების რაოდენობა: {word_count(text)}")


#2

def number(num):
    if num > 0:
        print("რიცხვი დადებითია")
    elif num < 0:
        print("რიცხვი უარყოფითია")
    else:
        print("რიცხვი ნულია")


num = float(input("შეიყვანეთ რიცხვი: "))
number(num)
#3

def categorize_age(age):
    if age < 0:
        print("არასწორი ასაკი")
    elif age <= 12:
        print("ბავშვი")
    elif age <= 19:
        print("თინეიჯერი")
    elif age <= 64:
        print("ზრდასრული")
    else:
        print("ხანდაზმული")


age = int(input("შეიყვანეთ ასაკი: "))
categorize_age(age)
#4

def separate_even_odd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens, odds = separate_even_odd(numbers)
print(f"ლუწი რიცხვები: {evens}")
print(f"კენტი რიცხვები: {odds}")
#5

def find_average(numbers):
    if len(numbers) == 0:
        return 0 
    return sum(numbers) / len(numbers)


numbers = [10, 20, 30, 40, 50]
average = find_average(numbers)
print(f"საშუალო რიცხვი: {average}")
