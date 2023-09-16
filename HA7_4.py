import multiprocessing
import os

def Task1(Value):
    print("1 to 50 Straight")
    for i in range(1,Value,1):
        print("Task1 : ",i)

def Task2(Value):
    print("50 to 1 Reverse")
    for i in range(Value,1,-1):
        print("Task2 : ",i)

def main():
    print("Demonstration of Multiprocessing")

    No1 = 50

    p1 = multiprocessing.Process(target = Task1, args = (No1,))
    p2 = multiprocessing.Process(target = Task2, args = (No1,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()
if __name__ == "__main__":
    main()