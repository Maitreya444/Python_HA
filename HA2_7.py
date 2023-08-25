#Input : 5
#   1   2   3   4   5   
#   1   2   3   4   5
#   1   2   3   4   5   
#   1   2   3   4   5   
#   1   2   3   4   5

def print_pattern(n):
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end="   ")
        print()

def main():
    n = int(input("Enter a number: "))
    print_pattern(n)

if __name__ == "__main__":
    main()
