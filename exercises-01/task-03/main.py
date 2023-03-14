def avg(arr):
    return sum(arr) / len(arr)


arr = []

while True:
    x = input()
    if x.isnumeric():
        arr.append(int(x))
    elif x.lower() == "done":
        break
    else:
        print("Enter a number")

print(f"Min: {min(arr)}")
print(f"Max: {max(arr)}")
print(f"Avg: {avg(arr)}")
arr.sort()
print(f"Sort: {arr}")
