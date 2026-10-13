#2013. Detect Squares
"""You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
 

Example 1:


Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points
 

Constraints:

point.length == 2
0 <= x, y <= 1000
At most 3000 calls in total will be made to add and count."""


#answer:
class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.ptsCount[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        for y2 in self.ptsCount[x1]:
            side = y2 - y1
            if side == 0:
                continue

            x3, x4 = x1 + side, x1 - side
            res += (self.ptsCount[x1][y2] * self.ptsCount[x3][y1] *
                    self.ptsCount[x3][y2])

            res += (self.ptsCount[x1][y2] * self.ptsCount[x4][y1] *
                    self.ptsCount[x4][y2])
        return res


#example:
detectSquares = CountSquares()
print(detectSquares.add([3, 10]))  # Output: None
print(detectSquares.add([11, 2]))  # Output: None
print(detectSquares.count([11, 10]))  # Output: 1


"""Walkthrough:

1. We need to design a data structure that supports adding points to a 2D plane and counting how many axis-aligned squares can be formed using a given point as one of the corners.
2. In the constructor, `self.ptsCount = defaultdict(lambda: defaultdict(int))` creates a nested dictionary where `ptsCount[x][y]` stores the number of times the point `(x, y)` has been added.
3. The `add()` method receives a point `[x, y]` and increments `self.ptsCount[x][y]` by one, allowing duplicate points to be counted correctly.
4. The `count()` method receives a query point `[x1, y1]` and initializes `res = 0` to store the total number of squares that can be formed using this point as a corner.
5. We iterate through every existing y-coordinate `y2` stored in the same vertical column `x1`, treating `(x1, y2)` as a potential second corner of a square.
6. We calculate `side = y2 - y1`, which represents the vertical distance between the query point and the potential second corner.
7. If `side == 0`, we skip that point because two points with the same coordinates cannot form a square with a nonzero side length.
8. We calculate two possible x-coordinates for the opposite vertical side of the square: `x3 = x1 + side` and `x4 = x1 - side`. These represent squares extending to the right and left of the query point.
9. For the square extending to the right, the other two required corners are `(x3, y1)` and `(x3, y2)`. We multiply the frequencies of all three required points other than the query point: `ptsCount[x1][y2] * ptsCount[x3][y1] * ptsCount[x3][y2]`.
10. This multiplication counts every possible combination of duplicate points that can form a square on the right side.
11. We perform the same calculation for the square extending to the left, using `(x4, y1)` and `(x4, y2)`, and add the result to `res`.
12. We repeat this process for every possible `y2`, considering every valid vertical side that could form a square with the query point.
13. Since both possible horizontal directions are checked, the algorithm counts squares extending either left or right, including all combinations created by duplicate points.
14. After examining all potential second corners, the `count()` method returns `res`, representing the total number of squares that can be formed with the query point as one corner.
15. The key idea is to fix the query point and another point sharing its x-coordinate, calculate the possible square side length, and check whether the other two corners exist.
16. If \\(P\\) is the number of distinct y-coordinates stored in the query point's column, the `count()` method takes \\(O(P)\\) time. The `add()` method takes \\(O(1)\\) average time, and the auxiliary space complexity is \\(O(N)\\) for storing the added points and their frequencies."""