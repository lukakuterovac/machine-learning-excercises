import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("data.csv", delimiter=",", skip_header=1)

# a)
print(f"Broj osoba: {len(data)}")

# b)
plt.scatter(data[:, 1], data[:, 2])
plt.show()

# c)
plt.scatter(data[::50, 1], data[::50, 2])
plt.show()

# d)
min_height = np.min(data[:, 1])
max_height = np.max(data[:, 1])
mean_height = np.mean(data[:, 1])
print(f"Min: {min_height}\nMax: {max_height}\nAvg: {mean_height}")

# e)
m_ind = data[:, 0] == 1
m_data = data[m_ind]
m_min_height = np.min(m_data[:, 1])
m_max_height = np.max(m_data[:, 1])
m_mean_height = np.mean(m_data[:, 1])
print(f"Male\nMin: {m_min_height}\nMax: {m_max_height}\nAvg: {m_mean_height}")
f_ind = data[:, 0] == 0
f_data = data[f_ind]
f_min_height = np.min(f_data[:, 1])
f_max_height = np.max(f_data[:, 1])
f_mean_height = np.mean(f_data[:, 1])
print(f"Female\nMin: {f_min_height}\nMax: {f_max_height}\nAvg: {f_mean_height}")
