#Prime Number

def Prime(iNo):
    for iCnt in range (2,iNo//2,1):
        if((iNo % iCnt)==0):
            return True
        else:
            return False

def main():
    iValue = 0
    iRet = False

    print("Enter a number")
    iValue =int(input())

    iRet = Prime(iValue)

    if(iRet == True):
        print("Not a prime numnber", iValue)
    else:
        print("It's a prime numnber", iValue)
    
if __name__=="__main__":
    main()