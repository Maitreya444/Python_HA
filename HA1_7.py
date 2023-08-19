#Write a program which contains functions that accept one number from user and returns true if number is divisible by 5 
#otherwise return false

def ChkDiv(iNo):
    if((iNo % 5)==0):
        return True
    else:
        return False

def main():
    iValue = 0
    bRet = 0

    print("Enter a number")

    iValue = int(input())
    bRet = ChkDiv(iValue)

    if(bRet == True):
        print("Yes divisible by 5")
    else:
        print("No not divisible by 5")

if __name__=="__main__":
    main()