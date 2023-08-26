#Write a program which accept N numbers from user and store it into List. Return Max number from List

def main():
    Length = 0
    value = 0
    Max = Arr
    print("Enter number of elements that you want to enter")
    Length = int(input())

    Arr=list()

    print("Enter the elemets : ")
    for iCnt in range(Length):
        value = int(input())
        Arr.append(value)

    print("Elements from list are : ")
    for iCnt in range(Length):
        print(Arr[iCnt])

    Max = Arr[0]
    
    for iCnt in range(Length):
        if((Arr[iCnt] > Max)):
            Max = Arr[iCnt]
    print("Max element is ",Max)    

if __name__=="__main__":
    main()