def http_error(status):
    match status:
        case 400 | 404:
            return 'bad request'
        case _:
            return 'default case'
        
def match_point(tupleParam):
    match tupleParam:
        case (0,0):
            print(0,0)
        case (x ,0):
            print(f"X={x}")
        case (0 , y):
            print(f"Y={y}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
        
match_point((0,1))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
            
where_is(Point(0,0))