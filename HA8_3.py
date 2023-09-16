import sys
    
i = 5

def Display(no):
    global i

    if(i >= no):
        print(i)
        i = i -1
        Display(no)

def main():
    Display(1)
    
if __name__ =="__main__":
    main()