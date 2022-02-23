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


def normalize():
    total = 0
    for i in fitness:
        total += i

    for j in range(0, len(fitness)):
        fitness[j] = j / total


def setPts(numPts):
    global numCities
    numCities = numPts


def distance(pt1, pt2):
    return np.sqrt((pt2[0]-pt1[0]) ** 2 + (pt2[1]-pt1[1]) ** 2)


def swap(pts, pt1, pt2):
    pts[pt1], pts[pt2] = pts[pt2], pts[pt1]


def shuffle(pts, num):
    for i in range(0, num):
        ind1 = np.random.randint(0, len(pts))
        ind2 = np.random.randint(0, len(pts))
        swap(pts, ind1, ind2)
        return pts


def distTotal(points, ptOrder):
    total = 0
    for i in range(0, numCities-1):
        total += distance(points[ptOrder[i]], points[ptOrder[i+1]])

    return total


def pick(pts, prob):
    ind = 0
    r = np.random.random(1)

    while r > 0:
        r = r - prob[ind]
        ind += 1

    ind -= 1
    if 0 < ind < 10:
        return list.copy(pts[ind])
    else:
        return pick(pts, prob)


def mutate(pts):
    ind1 = np.random.randint(0, len(pts))
    ind2 = np.random.randint(0, len(pts))
    swap(pts, ind1, ind2)


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

    for i in range(100):
        population.append(shuffle(list.copy(order), 100))


def solve(points, pop):
    print(points)
    print(population)
    del fitness[:]
    bestDist = 0
    ind = 0
    for i in pop:
        d = distTotal(cities, i)
        fitness.append(1/d+1)
        if fitness[ind] > bestDist:
            bestDist = fitness[ind]
            bestOrder = i

        ind += 1

    normalize()

    print(bestOrder)
    print(distTotal(cities, bestOrder))
    for i in range(numCities-1):
        x1 = points[bestOrder[i]][0]
        y1 = points[bestOrder[i]][1]
        x2 = points[bestOrder[i+1]][0]
        y2 = points[bestOrder[i+1]][1]
        lines.append(w.create_line(x1, y1, x2, y2))


def nextGen(pop):
    for i in lines:
        w.delete(i)

    newPop = []
    for i in range(0, len(pop)):
        newOrd = pick(pop, fitness)
        mutate(newOrd)
        newPop.append(newOrd)

    for i in range(0, len(pop)):
        pop[i] = newPop[i]

    solve(cities, pop)


w = Canvas(root, width=600, height=600)
topFrame = Frame(root)
bottomFrame = Frame(root)
topFrame.pack()
bottomFrame.pack(side=BOTTOM)
w.pack(side=BOTTOM)
genBtn = Button(topFrame, text="Generate", command=lambda: generate(numCities))
solveBtn = Button(topFrame, text="Solve", command=lambda: solve(cities, population))
numLabel = Label(topFrame, text="Number of Points")
e1 = Entry(topFrame)
applyBtn = Button(topFrame, text="Apply", command=lambda: setPts(int(e1.get())))
nextBtn = Button(topFrame, text="Next Gen", command=lambda: nextGen(population))
numLabel.pack()
e1.pack()
applyBtn.pack()
genBtn.pack()
solveBtn.pack()
nextBtn.pack()
root.mainloop()
