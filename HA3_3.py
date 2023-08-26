#Write a program which accept N numbers from user and store it into List. Return Min number from List

def main():
    Length = 0
    value = 0
    Min = 0
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

    Min = Arr[0]
    
    for iCnt in range(Length):
        if((Arr[iCnt] < Min)):
            Min = Arr[iCnt]
    print("Min element is ", Min)    

if __name__=="__main__":
    main()