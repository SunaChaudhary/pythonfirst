#finsing vowel using logical operator or
user_input = input("Enter a word:")
first_char =user_input.lower()[0]

if first_char=='a' or first_char=='e' or first_char=='i' or first_char=='o' or first_char=='u':
    print("Word is vowel")
else:
    print("Word is not vowel")