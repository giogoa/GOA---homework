#N1 
for i in range(5):
    print("GOA IS BEST")
           
           
#N2
number = int(input("enter time: "))
while number >= 0:
    number = number - 1
    print(number + 1)
           
#N3
for i in range(126, -1, -1):
   print(i , end= " ")
   
#N4
sum_numbers = 0
for i in range(1  , 48):
    sum_numbers += i

print("რიცხვების ჯამი ( + ოპერატორი):", sum_numbers)

product_numbers = 1
for i in range(1 , 48):
    product_numbers *= i

print("რიცხვების ჯამი ( * ოპერატორი):", product_numbers)

#N5
num = 100
while num >= 1:
    print(num , end=" 90")
    num -= 1