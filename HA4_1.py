#Write a program which conatins one lamda function which accepts parametre and return power of two.
#Input : 4 
#Output: 16
def ChkNo(iValue):
    iPower = 0
    iPower = iValue * iValue
    return iPower

def main():
    iNo = 0
    iRet = 0
    print("Enter a number")
    iNo = int(input())

    iRet = ChkNo(iNo)

    print("Power of 2 is :",iRet)

if __name__=="__main__":
    main()