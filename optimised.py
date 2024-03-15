import time
# Used to keep track of the time taken by the program
from sympy import isprime


# Used to check if a given number is prime using 'isprime'
# The Naming convention used here is camelCase
# code starts from line 58

# The function below is used to generate all the odd length palindromes within the value inputted into the function

def generatePalindromes(count):
    palindromes = []
    # the following is there to make sure that 1 is not added to the list of special numbers as it's not prime
    if count == 1:
        return list(range(1, 10))
    else:
        # Generate odd-length palindromes
        for i in range(10 ** (count // 2 - 1), 10 ** (count // 2)):
            # Turning number into a string to be compared if they are palindromes
            strI = str(i)
            # This for loop is used to make sure that the correct numbers are added to the list of palindromes
            for check in range(10):
                palindromes.append(int(strI + str(check) + strI[::-1]))
                # After all the cycles are completed we sort the list to make sure that it's in order from smallest to biggest
    palindromes.sort()
    # returns to SpecialNumbersList line 32
    return palindromes


# The function below generates a list to put all the special numbers into using values from generatePalindromes()


def specialNumbersList(minNumb, maxNumb):
    listOfSpecial = []
    # Next we get the length of each number to determine how many times the algorithm needs to run for
    digitStart = len(str(minNumb))
    digitEnd = len(str(maxNumb))
    # these length values are used in this for loop below to create the range
    for allDigits in range(digitStart, digitEnd + 1):
        # Next we go to the function of generatePalindromes located on line 11
        palindromes = generatePalindromes(allDigits)
        # then we go through the for loop till the counter (numbers) reaches the amount of palindromes in the list
        for numbers in palindromes:
            # if the start number is smaller than the current number and smaller than the end number, while being prime
            if minNumb <= numbers <= maxNumb and isprime(numbers):
                # if the number follows the above conditions then check if it's already in the list of special numbers
                if numbers in listOfSpecial:
                    pass
                else:
                    # if not in the list then it's a special number and gets added to the list
                    listOfSpecial.append(numbers)
                    # checks if the max is greater than 11 as this algortihm doesnt add 11 automatically
    # as its the only even length prime and palidrome
    if maxNumb >= 11:
        listOfSpecial.append(11)
        # sorts the list to make sure the numbers are in the correct order when printing them out to the user
    listOfSpecial.sort()
    # returns to line 67
    return listOfSpecial


def main():
    # First we take the inputs from the user (or the test cases)
    start = int(input("""please input a starting number that you want the program to start from 

(A special number are ones that are both prime numbers and are palindromic) """))
    ending = int(input("please input another number, which states when the program will end "))
    # Next we start the timer to be able to track how long it takes to collect all the special numbers
    startTimer = time.time()
    # After the code then goes to the function of specialNumbersList taking the values of start and ending (line(22))
    allSpecialNumbers = specialNumbersList(start, ending)
    # Once the algorithm has finished we stop the timer and then start to print the results
    stopTimer = time.time()

    print(f"There are a total of {len(allSpecialNumbers)} within {start} and {ending}")
    if len(allSpecialNumbers) <= 5:
        # if there is only 5 or less special numbers print all the numbers
        print(f"There is only {len(allSpecialNumbers)} which include the following {allSpecialNumbers}")
    else:
        # if there is 6 or more special numbers print the first 3 and then the last 3 numbers
        print(f"The first three numbers that are special are {allSpecialNumbers[:3]}")
        print(f"The last three numbers that are special are {allSpecialNumbers[-3:]}")
    runTimer = stopTimer - startTimer
    # gets the time it took to find all the numbers
    print(f"It took {round(runTimer, 4)} seconds to figure out the special numbers")


# Code starts here ###############
while True:
    main()  # located on line 41
    # once the algorithm has finish ask the user if they want to restart the program
    restart = input(f"Do you want to restart the program? ")
    if restart.lower() not in ["yes", "Yeah", "1"]:
        # ends the code
        break