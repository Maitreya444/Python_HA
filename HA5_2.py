class Circle:
    def __init__(self,Radius,Area,Circumferance):
        print("Inisde Constructor")
        self. No1 = Radius
        self. No2 = Area
        self. No3 = Circumferance

    def Radius(self):
        pi = 3.14
        Ans = self.No3 / 2 * pi
        return Ans
    
    def Area(self):
        pi = 3.14
        Ans = pi * self.No1 * self.No1  
        return Ans
    
    def Circumferance(self):
        pi = 3.14
        Ans = 2 * pi * self.No1
        return Ans
    
def main():
    Ret = 0
    obj1 = Circle(16,16,16)
    obj2 = Circle(24,24,24)

    Ret = obj1.Radius()
    print("Radius is ", Ret)
    Ret = obj1.Area()
    print("Area is ", Ret)
    Ret = obj1.Circumferance()
    print("Circumferance is ", Ret)  

    Ret = obj2.Radius()
    print("Radius is ", Ret)
    Ret = obj2.Area()
    print("Area is ", Ret)
    Ret = obj2.Circumferance()
    print("Circumferance is ", Ret)  

if __name__ =="__main__":
    main()