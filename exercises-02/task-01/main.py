import matplotlib.pyplot as plt
import numpy as np

x = np.array([1.0, 3.0, 3.0, 2.0, 1.0], float)
y = np.array([1.0, 1.0, 2.0, 2.0, 1.0], float)

plt.plot(x, y, "r", linewidth=2, marker=".", markersize=10)
plt.axis([0.0, 4.0, 0.0, 4.0])
plt.xlabel("x os")
plt.ylabel("y os")
plt.title("Primjer")
plt.show()
