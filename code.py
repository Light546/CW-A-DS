import time


def isPrime(numbers):
    global counter
    if numbers <= 1:
        return False
    if numbers == 2 or numbers == 3 or numbers == 5 or numbers == 7:
        return True
    if numbers % 3 == 0 or numbers % 5 == 0 or numbers % 7 == 0:
        return False
    counter = 11
    while counter * counter <= numbers:
        if numbers % counter == 0:
            return False
        counter += 2
    return True
def generatePalindromes(count):
    palindromes = []
    if count == 1:
        return list(range(1, 10))
    else:
        for i in range(10 ** (count // 2 - 1), 10 ** (count // 2)):
            strI = str(i)
            for check in range(10):
                palindromes.append(int(strI + str(check) + strI[::-1]))
    palindromes.sort()
    return palindromes


def specialNumbersList(minNumb, maxNumb):
    listOfSpecial = []
    digitStart = len(str(minNumb))
    digitEnd = len(str(maxNumb))
    for allDigits in range(digitStart, digitEnd + 1):
        palindromes = generatePalindromes(allDigits)
        for numbers in palindromes:
            if minNumb <= numbers <= maxNumb and isPrime(numbers):
                if numbers in listOfSpecial:
                    pass
                else:
                    listOfSpecial.append(numbers)
    if maxNumb >= 11 >= minNumb:
        listOfSpecial.append(11)
    listOfSpecial.sort()
    return listOfSpecial


def main():
    start = int(input("""please input a starting number that you want the program to start from 

(A special number are ones that are both prime numbers and are palindromic) """))
    ending = int(input("please input another number, which states when the program will end "))
    startTimer = time.time()
    allSpecialNumbers = specialNumbersList(start, ending)
    stopTimer = time.time()

    print(f"There are a total of {len(allSpecialNumbers)} within {start} and {ending}")
    if len(allSpecialNumbers) <= 5:
        print(f"There is only {len(allSpecialNumbers)} which include the following {allSpecialNumbers}")
    else:
        print(f"The first three numbers that are special are {allSpecialNumbers[:3]}")
        print(f"The last three numbers that are special are {allSpecialNumbers[-3:]}")
    runTimer = stopTimer - startTimer
    print(f"It took {round(runTimer, 4)} seconds to figure out the special numbers")


while True:
    main()
    restart = input(f"Do you want to restart the program? ")
    if restart.lower() not in ["yes", "Yeah", "1"]:
        break

