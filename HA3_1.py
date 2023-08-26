#Write a program which accept N numbers from user and store it into List. Return addition of all elements in list.
#Input : 6
#Elements : 13  5   45  7   4   56
#Output : 130

def main():
    Length = 0
    Total = 0 

    print("ENter number of elements that you want to enter")
    Length = int(input())

    Arr=list()

    print("Enter the elements :")
    for iCnt in range(Length):
        value = int(input())
        Arr.append(value)

    print("Elements from list are : ")
    for iCnt in range(Length):
        print(Arr[iCnt])

    for iCnt in range(Length):
        Total += Arr[iCnt]
        print(Total)


if __name__ =="__main__":
    main() 