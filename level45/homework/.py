def word_count(text):
    words = text.split()  
    return len(words)
text = input()

text = "ეს არის მაგალითი ტექსტი"
print(f"სიტყვების რაოდენობა: {word_count(text)}")
