import multiprocessing
import os

def Task1(Arr):
    print("Executing the first task of displaying even elements of array..")
    iCnt = 0
    for iCnt in Arr:
        if iCnt % 2 ==0:
            print(iCnt)

def Task2(Arr):
    print("Executing the first task of displaying odd elements of array..")
    iCnt = 0
    for iCnt in Arr:
        if iCnt % 2 !=0:
            print(iCnt)

def main():
    print("Demonstration of Multiprocessing")

    print("Enter number of elements that you want to store")
    Length = int(input())

    Arr = list()

    print("Enter the elements")
    for iCnt in range(Length):
        value = int(input())
        Arr.append(value)

    print("Elements from list are :")
    for iCnt in range(Length):
        print(Arr[iCnt])

    p1 = multiprocessing.Process(target = Task1, args = (Arr,))
    p2 = multiprocessing.Process(target = Task2, args = (Arr,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()
if __name__ == "__main__":
    main()