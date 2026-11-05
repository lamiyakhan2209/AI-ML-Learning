numbers = [10, 20, 30, 40, 10, 30, 50]
unique_number = []

for num in numbers:
    if num not in unique_number:
        unique_number.append(num)
print("unique number list:", unique_number)