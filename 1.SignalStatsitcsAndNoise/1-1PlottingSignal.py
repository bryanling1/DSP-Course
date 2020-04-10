from matplotlib import pyplot
from matplotlib import style

x = [1, 2, 3, 4, 5, 6]
y = [7, 5, 6, 7, 8, 9]

x2 = [1, 2, 3, 4, 5, 6]
y2 = [7, 2, 9, 7, 8, 5]

style.use("dark_background")
pyplot.plot(x, y, label="line1")
pyplot.plot(x2, y2, label="line2")
pyplot.xlabel("X axis")
pyplot.ylabel("Y axis")
pyplot.legend()
pyplot.show()