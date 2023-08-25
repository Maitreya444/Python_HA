#Add, Mult, Div, Sub

def Add(iNo1, iNo2):
    Ans = 0
    Ans = iNo1 + iNo2
    return Ans

def Sub(iNo1, iNo2):
    Ans = 0
    Ans = iNo1 - iNo2
    return Ans

def Mult(iNo1, iNo2):
    Ans = 0
    Ans = iNo1 * iNo2
    return Ans

def Divide(iNo1, iNo2):
    Ans = 0
    Ans = iNo1 / iNo2
    return Ans

def main():
    iValue1 = 0
    iValue2 = 0
    iRet1 = 0
    iRet2 = 0
    iRet3 = 0
    iRet4 = 0

    print("Enter a number 1")
    iValue1 = int(input())

    print("Enter a number 2")
    iValue2 = int(input())

    iRet1 = Add(iValue1, iValue2)
    iRet2 = Sub(iValue1, iValue2)
    iRet3 = Mult(iValue1, iValue2)
    iRet4 = Divide(iValue1, iValue2) 

    print("Additon is : ", iRet1)
    print("Subtraction is : ", iRet2)
    print("Multiplication is : ", iRet3)
    print("Divide is : ", iRet4)

if __name__=="__main__":
    main()