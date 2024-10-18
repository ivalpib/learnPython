user_input = input("Enter any word: ")
first_char = user_input[0].lower()
print(first_char)
if first_char == 'a' or first_char == 'e' or first_char == 'i' or first_char == 'o' or first_char == 'u':
    print("The first character of the word is vowel ")
else:
    print("The first character of the word is consonant ")