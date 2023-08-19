#Write a program which contains one function named as ChkNum() which accept one parametre as Number.
#If number is even then it display even or else odd

def ChkNum(iNo):
    if((iNo % 2)==0):
        print("EVEN")
    else:
        print("ODD")

def main():
    iValue = 0

    print("Enter a number")
    iValue = int(input())

    ChkNum(iValue)

if __name__ =="__main__":
    main()