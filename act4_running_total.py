# Running Total
count = 0
total = 0.0

while True:
    price = float(input("Price (0 to stop): "))
    if price == 0:
        break
    count = count + 1
    total = total + price

if count > 0:
    average = total / count
else:
    average = 0.0

print(f"Items: {count} Total: {total:.2f}")
print(f"Average: {average:.2f}")