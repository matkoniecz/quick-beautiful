list_of_numbers = [28, -10, 7.6, 2828, 0, 13]
largest = list_of_numbers[0]
for element in list_of_numbers:
    if largest < element:
        largest = element
print(largest)
