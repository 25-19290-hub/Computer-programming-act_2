# vowels.py
sentence = input("Enter a sentence: ")
vowel_list = ['a','e','i','o','u','A','E','I','O','U']
count = 0
index = 0

while index < len(sentence):
    char = sentence[index]
    if char in vowel_list:
        count +=1
    index +=1

print(f"\nNumber of vowels: {count}")