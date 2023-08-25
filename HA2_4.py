#Sum of factors

def Factorial(iNo):
    Fact = 0
    for iCnt in range(1, iNo-1, 1):
        if((iNo % iCnt)==0):
            Fact = Fact + iCnt
    return Fact

def main():
    iValue = 0
    iRet = 0

    print("Enter a number")
    iValue =int(input())

    iRet = Factorial(iValue)

    print("Sum of Factorial is : ", iRet)
    
if __name__=="__main__":
    main()