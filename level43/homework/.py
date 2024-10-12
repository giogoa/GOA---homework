def count_items(item_list, item):
    """
    ითვლის, რამდენჯერ გვხვდება ელემენტი სიაში.

    :param item_list: ელემენტების სია
    :param item: ელემენტი, რომლის დათვლაც გსურს
    :return: რამდენჯერ გვხვდება ელემენტი სიაში
    """
    return item_list.count(item)

# მაგალითი გამოყენების
items = ['apple', 'banana', 'orange', 'apple', 'kiwi']
item_to_count = 'apple'
count = count_items(items, item_to_count)

print(f"'{item_to_count}' ელემენტი გვხვდება {count} ჯერ.")
#2
def sum_of_list(num_list):
    """
    ითვლის რიცხვების ჯამს სიაში.

    :param num_list: რიცხვების სია
    :return: რიცხვების ჯამი
    """
    total = 0
    for num in num_list:
        total += num
    return total

# მაგალითი გამოყენების
numbers = [1, 2, 3, 4, 5]
total_sum = sum_of_list(numbers)

print(f"რიცხვების ჯამი არის: {total_sum}")
#3
def sum_of_list(num_list):
    """
    ითვლის რიცხვების ჯამს სიაში.

    :param num_list: რიცხვების სია
    :return: რიცხვების ჯამი
    """
    total = 0
    for num in num_list:
        total += num
    return total

def average_of_list(num_list):
    """
    ითვლის რიცხვების საშუალო მნიშვნელობას სიაში.

    :param num_list: რიცხვების სია
    :return: რიცხვების საშუალო მნიშვნელობა
    """
    if len(num_list) == 0:  # დარწმუნდებით, რომ სია არ არის ცარიელი
        return 0
    
    total_sum = sum_of_list(num_list)
    average = total_sum / len(num_list)
    return average

# მაგალითი გამოყენების
numbers = [1, 2, 3, 4, 5]
average_value = average_of_list(numbers)

print(f"რიცხვების საშუალო მნიშვნელობა არის: {average_value}")
#4
def reverse_list(items):
    """
    სიის გადაბრუნება.

    :param items: ელემენტების სია
    :return: გადაბრუნებული სია
    """
    reversed_items = []
    for item in items:
        reversed_items.insert(0, item)  # ელემენტს ვამატებთ სიაში პირველ ადგილზე
    return reversed_items

# მაგალითი გამოყენების
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)

print(f"პირველი სია: {original_list}")
print(f"გადაბრუნებული სია: {reversed_list}")
