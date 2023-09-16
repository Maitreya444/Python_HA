import multiprocessing
import os

def Task1(Value):
    print("Executing the first task...")
    for i in range(Value):
        if i % 2 == 0:
            print("Task1 : ",i)

def Task2(Value):
    print("Executing the second task...")
    for i in range(Value):
        if i % 2 !=0:
            print("Task2 : ",i)

def main():
    print("Demonstration of Multiprocessing")

    No1 = 20

    p1 = multiprocessing.Process(target = Task1, args = (No1,))
    p2 = multiprocessing.Process(target = Task2, args = (No1,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()
if __name__ == "__main__":
    main()
