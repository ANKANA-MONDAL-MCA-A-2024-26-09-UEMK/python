radius = 10
area = 3.14 * radius ** 2
result = "The area of a circle with radius "

for char in str(radius):
    result += char

result += " is "

for char in str(int(area)):
    result += char

result += " meters square."
print(result)
