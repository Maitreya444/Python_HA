#Lambda function for multiplication

ChkNoX = lambda iValue1, iValue2 : iValue1 + iValue2
    

def main():
    iNo1 = 0
    iNo2 = 0
    iRet = 0
    print("Enter a number")
    iNo1 = int(input())
    iNo2 = int(input())

    iRet = ChkNoX(iNo1, iNo2)

    print("Addition is :",iRet)

if __name__=="__main__":
    main()