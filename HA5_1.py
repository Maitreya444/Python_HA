class Demo:
    def __init__(self, Value1, Value2):
        self.no1 = Value1
        self.no2 = Value2

    Value = 0

    def Fun(self):
        print("Nos from obj1 are : ", self.no1, self.no2)
    def Gun(self):
        print("Nos from obj2 are : ", self.no1, self.no2)

def main():
    
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)
    
    obj1.Fun()
    obj2.Gun()

if __name__=="__main__":
    main()