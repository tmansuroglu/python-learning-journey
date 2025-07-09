class Point1:
    __match_args__ = ("x", "y")  # defines which attributes to match positionally. Without this you cant match the class

    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point1(3, 4)

match p1:
    case Point1(3, 4): 
        print("First match")

class Point2:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
p2 = Point2(1,2)

match p2:
    case Point2(1, 2):  # ❌ This will raise a TypeError!
        print("Second match")