def total_euro(hours, euro_per_hour):
    return hours * euro_per_hour


hours = int(input("Working hours: "))
euro_per_hour = float(input("Euro per hour: "))

total = total_euro(hours, euro_per_hour)

print(f"Ukupno: {total} eura")
