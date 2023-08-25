#Input : 5
#           *   *   *   *   *
#           *   *   *   *
#           *   *   *
#           *   *
#           *
def print_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("* ", end="")
        print()

def main():
    n = int(input("Enter a number: "))
    print_pattern(n)

if __name__ == "__main__":
    main()
