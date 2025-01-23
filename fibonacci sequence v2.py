import math

#Def functions

# 0) More info about Fibonacci and Golden Ratio
def more_info():
    print('''
    Fibonacci Sequence: A sequence of numbers where each number is the sum of the two preceding ones, 
    usually starting with 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, and so on.

    Golden Ratio: An irrational number, approximately 1.618, which occurs when the ratio of two numbers 
    is the same as the ratio of their sum to the larger of the two numbers. 
    It appears frequently in mathematics, art, and nature due to its aesthetically pleasing properties.
    When you divide two consecutive Fibonacci numbers, the result approximates the Golden Ratio as you move further along the sequence.
    ''')
    print("Ready to start calculating? Press ENTER")
    input()

#1) Fibonacci Sequence Generator
def fibonacci_sequence(): 
    #Lenght of fibonacci sequence
    length = int(input("Please enter the number of terms for your Fibonacci sequence: "))
    fib1 = 0
    fib2 = 1 

    for i in range(length):
        fib = fib1 + fib2
        print(fib)
        fib1 = fib2 
        fib2 = fib

#2) Number finder
#Fn = ( (1 + √5)^n - (1 - √5)^n ) / (2^n × √5)

def number_finder():
    #User Input position
    n = int(input("Enter the position number (starts at 1): "))
    #formula 
    fn = ((1+math.sqrt(5))**n - (1-math.sqrt(5))**n ) / (2**n * math.sqrt(5))

    #Integer to ordinal function for string result
    def make_ordinal(n):
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
        return str(n) + suffix

    #Print Result
    print("The ", make_ordinal(n), "position corresponds to: ", int(fn))
    print(" ")

# 3) Calculate golden ratio
def golden_ratio_calc():
    n = int(input("Please enter the Fibonacci position (higher numbers increase precision): "))
    n2 =n-1

    fn1 = ((1+math.sqrt(5))**n - (1-math.sqrt(5))**n ) / (2**n * math.sqrt(5))

    fn2 = ((1+math.sqrt(5))**n2 - (1-math.sqrt(5))**n2 ) / (2**n2 * math.sqrt(5))

    golden_ratio = fn1/fn2
    
    print("Fibonacci Numbers: ", int(fn1), "/", int(fn2))
    print(" ")
    print("Golden Ratio: ", golden_ratio)
    print(" ")

# 4) Goodbye
def goodbye():
    print("Goodbye :) ")
    


#Greetings
print("Hello, welcome to my Fibonacci Calculator.")

#Mode Selection
while True:
    #Ask user to select mode
    print('''Please select the function you would like to run:
      
      0) Learn about the Fibonacci Sequence and the Golden Ratio   
      
      1) Fibonacci Sequence Generator

      2) Find a number in the sequence

      3) Calculate Golden Ratio

      4) Exit
      ''')
    
    

    try:
        selection = int(input("Select mode: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer. (0, 1, 2, 3, or 4)")
        continue

    print(" ")

    valid_choice = True

    if selection == 0:
        more_info()
        valid_choice = False
    
    elif selection == 1:
        fibonacci_sequence()
    elif selection == 2:
        number_finder()
    elif selection == 3:
        golden_ratio_calc()
    elif selection == 4:
        goodbye()
        break
    else:
        print("Invalid choice. Please, select a valid option")
        print(" ")
        valid_choice = False
    
    

#When a valid option is selected and completed, it will ask to user if they want to continue calculating 
    if valid_choice == True:
        print("Would you like to do another calculation? (Yes / No)")
        continue_choice = str(input())
        if continue_choice.lower() != "yes":
            goodbye()
            break