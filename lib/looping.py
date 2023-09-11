#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    return [num ** 2 for num in int_list]

def fizzbuzz():
    for num in range(1, 101):
     # For numbers which are multiples of both three and five, return "FizzBuzz". 
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
     # For multiples of three, return "Fizz" instead of the number. 
        elif num % 3 == 0:
            print("Fizz")
    # For the multiples of five, return "Buzz". 
        elif num % 5 == 0:
            print("Buzz")
    # For all other numbers, just return the number itself.
        else:
            print(num)