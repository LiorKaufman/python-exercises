import os
import time


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


print('Check output.txt for the solution')
max_word_len('dorian_gray.txt')
print('*'*25)


# Q 4 create a function that will accepts a number
# if the number is positive we will want to know how many times the digit 0 appears in that number.
# E.G for 10030 the function should return "The digit 0 appears 3 times"
# Solve the problem using 3 diffirent ways and measure how long each solution took.
# Use import time

def find_digits_one():
    try:
        num = int(input("Enter a positive integer: "))
        t0 = time.perf_counter()
        count = 0
        if num < 0:
            return "Num must be positive"
        while num > 0:
            # If the number can be divided by 10 and the remainder is 0 that means the last digit of the number is 0.
            if num % 10 == 0:
                count = count + 1
            # floor division rounds the result to the nearest whole number
            # Any number below 10 when // by 10 result in 0
            num = num // 10
        t1 = time.perf_counter()
        print('Number of times the digit 0 appears: ', count)
        print('Running time: ', t1-t0, 'sec')
    except ValueError:
        print('Not a valid value, try again!')


def find_digits_two():
    try:
        num = int(input("Enter a positive integer: "))
        t0 = time.perf_counter()
        count = 0
        if num < 0:
            return "Num must be positive"
        num_as_string = str(num)
        for digit in num_as_string:
            if digit == '0':
                count = count + 1
        t1 = time.perf_counter()
        print('Number of times the digit 0 appears: ', count)
        print('Running time: ', t1-t0, 'sec')
    except ValueError:
        print('Not a valid value, try again!')


def find_digits_three():
    try:
        num = int(input("Enter a positive integer: "))
        t0 = time.perf_counter()
        count = 0
        if num < 0:
            return "Num must be positive"
        #  Using the string count method
        num_as_string = str(num)
        count = num_as_string.count('0')
        t1 = time.perf_counter()
        print('Number of times the digit 0 appears: ', count)
        print('Running time: ', t1-t0, 'sec')
    except ValueError:
        print('Not a valid value, try again!')


# Q 5 create a function that simulates the game: 7 Boom!
#  if a number can be divided by 7 but does not have the digit 7 the output should be Boom!
# If a number has the digit 7 one or more times the out put should be boom-boom-boom! as the number of times the digit 7 appears
# if the number has the digit 7 and can be divided by 7 the output should be bada-boom!
#  your function k_boom will simulate the game where K can be any positive integer in the range of 1 and 9
#  E.g: 770 -> bada-boom!, 14-> Boom!, 7177 -> boom-boom-boom!


def find_digits(num, digit):
    num_as_string = str(num)
    count = num_as_string.count(str(digit))
    return count


def k_boom(start, end, k):
    for num in range(start, end):
        count_k = find_digits(num, k)
        if num % k == 0 and count_k == 0:
            print(num, 'Boom!')
        elif num % k == 0 and count_k >= 1:
            print(num, 'Bada-Boom!')
        elif num % k != 0 and count_k >= 1:
            if count_k == 1:
                print(num, 'Boom!')
            elif count_k > 1:
                print(num, 'Boom-'*(count_k - 1), 'boom!')
        else:
            print(num)


k_boom(10, 29, 4)
print('*'*25)


find_digits_one()
print('*'*25)
find_digits_two()
print('*'*25)
find_digits_three()
print('*'*25)
