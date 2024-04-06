"""
Quickhull Algorithm
"""
class Vector:
    """ Class to represent a point vector """

    def __init__(self, x, y):
        """ Class constructor

        Parameters
        ----------
        x : integer
        y : integer
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """ Helper function print vectors """
        return "(" + str(self.x) + ", "+ str(self.y) + ")"


def findMin(vectors):
    """ Returns the minimum x coordinate value from the vectors list

    Paramters
    ---------
    vectors : List of Vector objects
    """
    min = 0
    # for loop to find the min x value
    for i in range(len(vectors)-1):
        if (vectors[i+1].x < vectors[min].x):
            min = i+1
    return vectors[min]

def findMax(vectors):
    """ Returns the maximum x coordiante value from the vectors list

    Paramters
    ---------
    vectors : List of Vector objects
    """

    max = 0
    # for loop to find the max x value
    for i in range(len(vectors)-1):
        if (vectors[i+1].x > vectors[max].x):
            max = i+1
    return vectors[max]

def findVectorSide(v1, v2, v):
    """ Finds which side of the segment line (v1-v2) the query vector point (v) reside
    
    Paramters
    ---------
    v1 : Line start vector
    v2 : Line end vector
    v  : query vector
    """

    side = (v.y - v1.y) * (v2.x - v1.x) - (v2.y - v1.y) * (v.x  - v1.x)
    if side > 0:
        return 1
    if side < 0:
        return -1
    return 0



def findVectorDistance(v1, v2, v):
    """ Finds the distance of the query vector point(v) from the segment line (v1-v2)
    
    Paramters
    ---------
    v1 : Line start vector
    v2 : Line end vector
    v  : Query vector
    
    """
    value = (v.y - v1.y) * (v2.x - v1.x) - (v2.y -v1.y) * (v.x - v1.x)
    return abs(value)

def findHull(convexHull, vectors, v1, v2, side):
    """ Recursive function to find the furthest points and add them to the convex hull

    Paramters
    ---------
    convexHull : List of current convex hull vector points
    vectors    : List of vector objects
    v1         : Line start vector
    v2         : Line end vector
    side       : Sections either side of segment line
    
    """
    vectorLocationSide = [v for v in vectors if findVectorSide(v1, v2, v) == side]
    if len(vectorLocationSide) > 0:
        maxV = sorted(vectorLocationSide, key = lambda v: findVectorDistance(v1, v2, v))[-1]
        findHull(convexHull, vectors, maxV, v1, -findVectorSide(maxV, v1, v2))
        findHull(convexHull, vectors, maxV, v2, -findVectorSide(maxV, v2, v1))
    else:
        if v1 not in convexHull:
            convexHull.append(v1)
        if v2 not in convexHull:
            convexHull.append(v2)

def quickHull(vectors):
    """ Function to calcualte the convex hull from given list of vectors
    
    Paramters
    ---------
    vectors : List of vector objects
    """
    if len(vectors) <= 2:
        print("Requires more then 2 vectors to find convex hull")
        return

    v1 = findMin(vectors)
    v2 = findMax(vectors)
    convexHull = []
    findHull(convexHull, vectors, v1, v2, 1)
    findHull(convexHull, vectors, v1, v2, -1)
    print("Convex Hull: " + str(convexHull))

def readVectors():
    """ Read vectors from console"""
    vectors = []
    print("Enter vector list as \"x y\" pairs or press Enter to execute Quickhull method: ")
    # Adds vectors to the vector list
    while True:
        vectorList = input("")
        if vectorList != "":
            try:
                params = vectorList.split()
                vectors.append(Vector(int(params[0]), int(params[1])))
            except:
                print("Invalid Input")
        else:
            break
    print("vectors: " + str(vectors))
    return vectors

if __name__ == '__main__':

    # Start quickhull method
    quickHull(readVectors())