#Write a program which accept number and print that number of *

def Star(iNo):
    for iCnt in range (0, iNo,1):
        print("*")

def main():
    iValue = 0

    print("ENter a number")
    iValue = int(input())

    Star(iValue)

if __name__ =="__main__":
    main()