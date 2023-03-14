import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data_C02_emission.csv")

plt.figure()
data["CO2 Emissions (g/km)"].plot(kind="hist", bins=100)
plt.show()

data["Fuel Color"] = data["Fuel Type"].map(
    {
        "X": "Red",
        "Z": "Blue",
        "D": "Green",
        "E": "Purple",
        "N": "Yellow",
    }
)
data.plot.scatter(
    x="Fuel Consumption City (L/100km)",
    y="CO2 Emissions (g/km)",
    c="Fuel Color",
)
plt.show()

data.boxplot(column=["Fuel Consumption Hwy (L/100km)"], by="Fuel Type")
plt.show()

new_data = data.groupby("Fuel Type")["Cylinders"].count().plot(kind="bar")

data.groupby("Cylinders")["CO2 Emissions (g/km)"].mean().plot(kind="bar", ax=new_data)
plt.show()
