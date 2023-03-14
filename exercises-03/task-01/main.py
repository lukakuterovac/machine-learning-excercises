import pandas as pd

data = pd.read_csv("data_C02_emission.csv")

print(len(data))

print(data.info())

data.dropna(axis=0)
data.drop_duplicates()
data = data.reset_index(drop=True)
print(len(data))

for col in data:
    if type(col) == object:
        data[col] = data[col].astype("Category")

data_new = pd.DataFrame(
    data, columns=["Make", "Model", "Fuel Consumption City (L/100km)"]
).sort_values("Fuel Consumption City (L/100km)", ascending=False)
print(data_new.head(3))
print(data_new.tail(3))

engine_25_35_data = data[
    (data["Engine Size (L)"] >= 2.5) & (data["Engine Size (L)"] <= 3.5)
]
print(len(engine_25_35_data))
print("CO2: ", engine_25_35_data.loc[:, "CO2 Emissions (g/km)"].mean())

audi_data = data[(data["Make"] == "Audi")]
print(len(audi_data))
audi_4cyl = audi_data[(audi_data["Cylinders"] == 4)]
print("CO2: ", audi_4cyl.loc[:, "CO2 Emissions (g/km)"].mean())

cyl_data = data[data["Cylinders"] % 2 == 0]
print(len(cyl_data))
print("CO2: ", cyl_data.loc[:, "CO2 Emissions (g/km)"].mean())

diesel_data = data[data["Fuel Type"] == "D"]
gasoline_data = data[(data["Fuel Type"] == "X") | (data["Fuel Type"] == "Z")]
print("D", diesel_data.loc[:, "Fuel Consumption City (L/100km)"].mean())
print("B", gasoline_data.loc[:, "Fuel Consumption City (L/100km)"].mean())
print("D", diesel_data.loc[:, "Fuel Consumption City (L/100km)"].median())
print("B", gasoline_data.loc[:, "Fuel Consumption City (L/100km)"].median())

diesel_4cyl_data = diesel_data[diesel_data["Cylinders"] == 4].sort_values(
    "Fuel Consumption City (L/100km)", ascending=False
)
print(diesel_4cyl_data.head(1))

manual_data = data[data["Transmission"].str.startswith("M")]
print(len(manual_data))

print(data.corr(numeric_only=True))
