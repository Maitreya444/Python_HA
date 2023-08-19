#Write a program whiach accept numbers from user and check wheather taht number is positive or negative or 0
#Input : 69     Output : +ve
#Input : -88     Output : -ve
#Input : 00     Output : zero

def ChkNo(iNo):
    if(iNo > 0):
        print("Positive")
    elif(iNo < 0):
        print("Negative")
    else:
        print("Zero")
    

def main():
    iValue = 0

    print("Enter a number")
    iValue = int(input())

    ChkNo(iValue)

if __name__ =="__main__":
    main()