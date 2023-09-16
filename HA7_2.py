import multiprocessing
import os

def Task1(Value):
    print("Executing the first task...")
    iCnt = 0
    SumFact=0
    for iCnt in range(1,Value,1):
        if Value % iCnt == 0 and iCnt %2 ==0:
            SumFact = SumFact + iCnt

    print("Even factors are : ",SumFact)

def Task2(Value):
    print("Executing the second task...")
    iCnt = 0
    SumFact1 = 0
    for iCnt in range(1,Value,1):
        if Value % iCnt ==0 and iCnt %2 !=0:
            SumFact1 = SumFact1 + iCnt
    
    print("Odd Factors are : ",SumFact1)

def main():
    print("Demonstration of Multiprocessing")

    No1 = 0
    
    No1 = int(input("Enter a number"))

    p1 = multiprocessing.Process(target = Task1, args = (No1,))
    p2 = multiprocessing.Process(target = Task2, args = (No1,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()
if __name__ == "__main__":
    main()