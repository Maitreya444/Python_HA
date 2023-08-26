def main():
    Length = 0
    value = 0
    search_element = 0
    found = False  
    print("Enter number of elements that you want to enter:")
    Length = int(input())

    Arr = list()

    print("Enter the elements:")
    for iCnt in range(Length):
        value = int(input())
        Arr.append(value)

    print("Enter the element you want to search for:")
    search_element = int(input())

    for iCnt in range(Length):
        if Arr[iCnt] == search_element:
            found = True
            break  
    if found:
        print(f"{search_element} found in the list.")
    else:
        print(f"{search_element} not found in the list.")

if __name__ == "__main__":
    main()
