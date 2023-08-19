#Addition of numbers

def Add(iNo1, iNo2):
    Ans = 0

    Ans = iNo1 + iNo2

    return Ans

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter number 1")
    iValue1 = int(input())

    print("Enter number 2")
    iValue2 = int(input())

    iRet = Add(iValue1, iValue2)

    print("Addition is :", iRet)

if __name__ =="__main__":
    main()