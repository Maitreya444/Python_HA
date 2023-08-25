#Write a program which display one number and display below pattern
#Input : 5
#Output:        *   *   *   *   *
#               *   *   *   *   *
#               *   *   *   *   *
#               *   *   *   *   *
#               *   *   *   *   *

def Pattern(iNo):
    i = 0
    j = 0
    while(i < iNo):
        j = 0
        while(j < iNo):
            print("* ", end="")
            j = j + 1
        print(" ")
        i = i + 1
            

def main():
    iValue = 0
    print("Enter a number")
    iValue = int(input())
    Pattern(iValue)

if __name__=="__main__":
    main()