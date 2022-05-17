"""Step 1: convert each word on a separate line to upper case"""

words = ['hello', 'hey', 'yo', 'ello', 'elephant', 'elf', 'goodbye']
# for word in words:
#     print(word.upper())

"""Step 2: turn this into a function"""


# def print_upper_words(words):
#     for word in words:
#         print(word.upper())


# print_upper_words(words)


"""Step 3: Only prints words that start with the letter "e" """


# def print_upper_words(words):
#     for word in words:
#         if word[0] == 'e':
#             print(word.upper())


# print(print_upper_words(words))

"""Step 4: Be able to pass in a set of letters that will print only the words that start with the letter """


def print_upper_words(words, must_start_with):
    for word in words:
        if word[0] == must_start_with:
            print(word.upper())


print(print_upper_words(words, 'h'))
