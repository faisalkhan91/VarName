'''
# Write a piece of code to create a Fibonacci sequence using recursion.
def fibr(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n>2:
        return fibr(n-1) + fibr(n-2)


print("\nFibonacci using recursion:\n")
for n in range(1,11):
    print(n, ":", fibr(n))


# Write a piece of code to create a Fibonacci sequence using the iterative method.
def fibi(n):
    a,b = 1,1
    for i in range(0, n):
        a, b = b, a + b
    return a


print("\nFibonacci using iteration 1:\n")
for n in range(1,11):
    print(n, ":", fibi(n))


def fibip(n):
    series =[1, 1]
    i = 2
    while i<=n:
        series.append(series[i-1] + series[i-2])
        i += 1
    return series


print("\nFibonacci using iteration 2:\n")
print(fibip(5))


# Write a piece of code to determine whether a number is a palindrome.

def palinum(num):

    check = num
    reverse = 0
    while num > 0:
        dig = num%10
        reverse = reverse * 10 + dig
        num = num // 10

    if check == reverse:
        print("It is a palindrome.")
    else:
        print("Not a palindrome!")


num_check = 35253
print("\nPalindrome for a number:\n")
palinum(num_check)


# Write a piece of code to determine whether two words are anagrams.


def is_anagram(str_1, str_2):

    if len(str_1) != len(str_2):
        return False

    str_1 = str_1.lower()
    str_2 = str_2.lower()

    dict_1 = dict.fromkeys(list(str_1), 0)
    dict_2 = dict.fromkeys(list(str_2), 0)

    for i in range(len(str_1)):
        dict_1[str_1[i]] += 1
        dict_2[str_2[i]] += 1
    return dict_1 == dict_2


word1 = 'earth'
word2 = 'heart'

print("\nAnagram of two words:\n")
print(is_anagram(word1, word2))


# How would you write a programme to find the biggest number in a list of 10 numbers?

list_of_numbers = [10, 20, 39, 4, 5, 54, 76, 36]

list_of_numbers.sort()
print("\nBiggest number in the list of numbers:\n")
print(list_of_numbers[len(list_of_numbers)-1])


# Write a piece of code to combine fractions from two arrays into a single array.

from fractions import Fraction
print("\nSum of two fractions:\n")
print(Fraction(1, 4) + Fraction(1, 4))


# try - except code


try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("Not a positive number!")
except ValueError as ve:
    print(ve)


# Find the smallest subarray in a given array that has a sum equal to or greater than a given sum


def subarray(arr, target):
    print("The given array: ", arr, " and the target sum: ", target)

    sum = 0
    count = 0

    for i in arr:
        sum += i
        count += count

    if sum >= target:
        print("\nThe sum is ", sum, " and the maximum subarray is of ", count, " elements.")
    elif sum < target:
        print("No subarray exists for the given sum:", target)
        return -1

    for i in range(len(arr)):
        # How to put info
        placeholder


array = [1, 2, 3, 4]
given_sum = 6

print("\nSmallest sub array for a given sum:\n")

output = subarray(array, given_sum)
print("Output: ", output)

'''

# Flatten a list of list
# example [[4, [5, [6]]], [1, 2], [3]] = [1,2,3,4,5,6]


def flatten(list_to_flatten):

        output = []
        for list in list_to_flatten:
            for item in list:
                output.append(item)

        print(output)
        return output


example = [[4, [5, [6]]], [1, 2], [3]]
result = flatten(example)
