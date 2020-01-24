vowels = "aeiou"

user_word = input("Please enter a single word and if that word contains a set of vowels in consecutive characters I will extend the length of the vowels to 5 characters.")

add = ""

for element in range(len(user_word)):
    if user_word[element] == user_word[element - 1] and user_word[element] in vowels:
        add += user_word[element] * 4
    else:
            add += user_word[element]  
print(add)
        
