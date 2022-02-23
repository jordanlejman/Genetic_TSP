import numpy as np
from tkinter import *

cities = []
numCities = 10
root = Tk()
root.title("TSP")
order = []
fitness = []
population = []
lines = []
w = Canvas(root, width=600, height=600)


def setPts(numPts):
    global numCities
    numCities = numPts


def distance(pt1, pt2):
    return np.sqrt((pt2[0]-pt1[0]) ** 2 + (pt2[1]-pt1[1]) ** 2)


def distTotal(points):
    total = 0
    for i in range(0, numCities-1):
        total += distance(points[i], points[i+1])

    return total


def swap(pt1, pt2):
    pt1[0], pt2[0] = pt2[0], pt1[0]
    pt1[1], pt2[1] = pt2[1], pt1[1]


def recurseSolve(pts, num):
    for i in range(num - 1):
        recurseSolve(pts, num - 1)
        if num % 2 == 0:
            swap(pts[i], pts[num - 1])
        else:
            swap(pts[0], pts[num - 1])


def generate(pts):
    for i in range(0, pts):
        cities.append([])
        for j in range(0, 2):
            cities[i].append(np.random.randint(50, 550))

    for i in range(0, pts):
        order.append(i)

    for i in range(pts):
        x1 = cities[i][0]-3
        y1 = cities[i][1]-3
        x2 = cities[i][0]+3
        y2 = cities[i][1]+3
        w.create_oval(x1, y1, x2, y2, fill="black")


def solve(pts):
    bestDist = distTotal(pts)
    bestOrder = pts
    print(bestDist)
    for i in range(numCities):
        for j in range(numCities):
            swap(pts[i], pts[j])
            if distTotal(pts) < bestDist:
                bestDist = distTotal(pts)
                bestOrder = pts

    for k in range(numCities - 1):
        x1 = bestOrder[k][0]
        y1 = bestOrder[k][1]
        x2 = bestOrder[k + 1][0]
        y2 = bestOrder[k + 1][1]
        w.create_line(x1, y1, x2, y2)


topFrame = Frame(root)
bottomFrame = Frame(root)
topFrame.pack()
bottomFrame.pack(side=BOTTOM)
w.pack(side=BOTTOM)
genBtn = Button(topFrame, text="Generate", command=lambda: generate(numCities))
solveBtn = Button(topFrame, text="Solve", command=lambda: solve(cities))
numLabel = Label(topFrame, text="Number of Points")
e1 = Entry(topFrame)
applyBtn = Button(topFrame, text="Apply", command=lambda: setPts(int(e1.get())))
numLabel.pack()
e1.pack()
applyBtn.pack()
genBtn.pack()
solveBtn.pack()
root.mainloop()
