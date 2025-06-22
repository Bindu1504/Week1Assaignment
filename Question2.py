'''
Count Vowels and Consonants:
Write a program that takes a string as input. Use a for loop to iterate through the string, and use an if-else condition inside the loop to count the number of vowels and consonants. Print the counts at the end.

'''


text = input("Enter a string: ")


vowel_count = 0
consonant_count = 0


vowels = "aeiouAEIOU"

for char in text:

    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1


print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
