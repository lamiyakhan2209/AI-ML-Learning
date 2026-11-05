numbers = [56, 77, 84, 91, 35, 40, 98, 22, 17, 16, 34, 18, 49, 62]

even_number = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers in the list are: ", even_number)