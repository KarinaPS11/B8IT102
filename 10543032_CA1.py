# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:04:23 2020

@author: 10543032
"""

def add(first, second):
    return first + second

def sub(first, second):
    return first - second

def mul(first, second):
    return first * second

def div(first, second):
    return first / second

def square_root(first):
    return first**0.5

def square(first):
    return first**2

def average(first, second):
    return ((first + second)/2)

def cube(first):
    return first**3

def square_power(first, second):
    return first ** second

def square_3root(first):
    return ((first**0.5)**0.5)

def operator_menu():
    print('1 or add or + to do addition')
    print('2 or add or - to do subraction')
    print('3 or add or * to do multiplication')
    print('4 or add or / to do division')
    print('5 or sqrt to perform square root')
    print('6 or square to square')
    print('5 or sqrt to perform square root')
    print('7 or aver to find the average')
    print('8 or cube to find the cube')
    print('9 or power to find the #1 to the power of #2')
    print('10 or sqrt3 to find the squar root of square root of a number')
    
def process_operation():
    firstNumber = float(input('Choose a number: '))
    operator_menu()
    func = input('Choose an operation. Here is a menu: ')
    if func not in ['5', 'sqrt', '6', 'square', '8', 'cube', '10', 'sqrt3']:
        secondNumber = float(input('Choose another number: '))
    
    if func in ['1', '+']:
        print(add(firstNumber, secondNumber))
    if func in ['2', '-']:
        print(sub(firstNumber, secondNumber))
    if func in ['3', '*']:
        print(mul(firstNumber, secondNumber))
    if func in ['4', '/']:
        print(div(firstNumber, secondNumber))
    if func in ['5', 'sqrt']:
        print(square_root(firstNumber))
    if func in ['6', 'square']:
        print(square(firstNumber))
    if func in ['7', 'aver']:
        print(average(firstNumber, secondNumber))
    if func in ['8', 'cube']:
        print(cube(firstNumber))
    if func in ['9', 'power']:
        print(square_power(firstNumber, secondNumber))
    if func in ['10', 'sqrt3']:
        print(square_3root(firstNumber))

def process():
    ask_again = ''
    while ask_again != 'n':
        process_operation()
        ask_again = input('Would you like to exit the calculator (y/n)?')

process()

print((25 ** 0.5)**0.5)