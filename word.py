#****************************************************************************************************
#
#       Name:          Joi Wilson
#       Course:        COSC 2110 Computer Languages: Python
#       Assignment:    word.py
#       Due Date:      10/02/2020
#       Description:
#               Write a program that allows the user to enter a string; All the words are
#               together but the first character is uppercase. Seperate and convert them
#
#****************************************************************************************************

def convert(user_enter):
    result = user_enter[0]
    for i in range(1, len(user_enter)):
        if user_enter[i].isupper():
            result += ' '
        result += user_enter[i].lower()
    return result

#****************************************************************************************************

def pigLatin(user_enter):
    converted = convert(user_enter)
    words = converted.split()
    result = ''
    for i in words:
        x = i[1:] + i[0] + 'ay '
        result += x
    return result.upper()

#****************************************************************************************************

def main():
    user_enter = input('Enter a string: ')
    converted = convert(user_enter)
    print('Normal string is:', converted)
    pig_latin = pigLatin(user_enter)
    print('Pig Latin is:', pig_latin)


if __name__ == '__main__':
    main()
