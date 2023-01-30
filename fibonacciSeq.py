import math

def fibSeq():
    print('Check Fibonacci sequence for: ')
    checkFib = int(float(input()))

    fibArr = [1, 0]
    for num in range(0, checkFib):
        fibSum = fibArr[0] + fibArr[1]

        if num % 2 == 0:
            fibArr[0] = fibSum
        if num % 2 != 0:
            fibArr[1] = fibSum

        print(fibSum, fibArr)
        
fibSeq()

