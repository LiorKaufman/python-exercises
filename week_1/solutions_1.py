import os


# Q 1
# Find 3 string methods that do not exist in a list object and show them on the string "abcd"
# Find 3 list methods that do not exist in a string object and show them on the list ["a","b","c","d"]
text = "abcd"
string_list = ['a', 'b', 'c', 'd']

print('*'*25)
print(text.islower())
print(text.capitalize())
print(text.istitle())

print('*'*25)
string_list.append('b')
print(string_list)
string_list.pop()
print(string_list)

print(string_list.index('a'))


# Q 2
# Find your Israeli ID control digit and print each iteration of the algorithm on the console
# https://he.wikipedia.org/wiki/%D7%A1%D7%A4%D7%A8%D7%AA_%D7%91%D7%99%D7%A7%D7%95%D7%A8%D7%AA
# An Israeli ID consists of 9 numbers with the last digit being the control digit. Each of the 8 first digits recives a score 1,2,1,2,1,2,1,2
#  multiply each digit by its score and sum the digits.
# If a digit multiplied by it's score is over 10 split the digit to 2 seperate digits and sum each of them seperatley
# Take the sum and round it up to the nearest multiple of 10
# e.g 54370042 -> 5×1 = 5, 4×2 = 8, 3 ×1 = 3, 7×2 = 14, 0×1 = 0 ,0 ×2 = 0, 4 ×1 = 4, 2 ×2 = 4
# 5 + 8 + 3 + (1+4) + 0 + 0 + 4 + 4 = 29 thus the control digit is 1 (30-29 = 1)

print('*'*25)


def control_digit(ID):
    sum_of_digits = 0
    for i in range(8):
        # Convert a string to INT
        value = int(ID[i])
        if(i % 2 == 0):
            sum_of_digits = sum_of_digits + value
        else:
            if value < 5:
                sum_of_digits += 2*value
            else:
                # sepearte the 2 digits, since the max value of the operation is 18 we can always just find the right most digit and then just add 1
                sum_of_digits += (2*value % 10) + 1

    sum_of_digits = sum_of_digits % 10
    control_digit = (10 - sum_of_digits) % 10

    return str(control_digit)


print("The control digit is: ")
print(control_digit("43658297"))

# Q 3 Create a function called max_word_len(filename) that recives a file and return a new output file
#  named output.txt. Each line in output.txt should have length of the longest word in the line.
#  use the dorain_gray.txt file
#  First 5 lines  7,2,5,7,7
#  Last 5 lines 11,0,10,9,9


print('*'*25)


def longest_word(sentence):
    current_max = 0
    values = sentence.split()
    for v in values:
        if len(v) > current_max:
            current_max = len(v)
    return current_max


def write_to_file(list_to_write):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, 'output.txt')
    with open(file_path, 'w') as f:
        for item in list_to_write:
            f.write(str(item))
            f.write('\n')


def max_word_len(filename):
    longest_words = []
    try:
        dir_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(dir_path, filename)
        with open(file_path) as fobj:
            text = fobj.read().split('\n')
            for line in text:
                longest_words.append(longest_word(line))
        write_to_file(longest_words)

    except FileNotFoundError:
        text = 'File not found'


max_word_len('dorian_gray.txt')
print('*'*25)
