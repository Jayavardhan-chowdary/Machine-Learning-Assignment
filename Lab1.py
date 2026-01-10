#P . Jayavardhan Chowdary
#BL.SC.U4AIE24064
#1)
# Program to count vowels and consonants in a string

text = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():        # check only letters
        if ch in 'aeiouAEIOU':
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

#2)
# Program to multiply two matrices A and B

# input matrix A
r1 = int(input("Enter number of rows of Matrix A: "))
c1 = int(input("Enter number of columns of Matrix A: "))

A = []
print("Enter elements of Matrix A:")
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    A.append(row)

# input matrix B
r2 = int(input("Enter number of rows of Matrix B: "))
c2 = int(input("Enter number of columns of Matrix B: "))

B = []
print("Enter elements of Matrix B:")
for i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input()))
    B.append(row)

# check if multiplication is possible
if c1 != r2:
    print("Error: Matrix multiplication not possible")
else:
    # result matrix
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            row.append(0)
        result.append(row)

    # matrix multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Product of Matrix A and B:")
    for row in result:
        print(row)

#3)
# Program to count common elements between two lists

list1 = []
list2 = []

n1 = int(input("Enter number of elements in first list: "))
print("Enter elements of first list:")
for i in range(n1):
    list1.append(int(input()))

n2 = int(input("Enter number of elements in second list: "))
print("Enter elements of second list:")
for i in range(n2):
    list2.append(int(input()))

count = 0

for i in list1:
    for j in list2:
        if i == j:
            count += 1
            break   # avoids counting same element again

print("Number of common elements:", count)

#4)
# Program to find transpose of a matrix

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter elements of the matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

print("Original Matrix:")
for row in matrix:
    print(row)

# transpose matrix
transpose = []
for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)

print("Transpose of the Matrix:")
for row in transpose:
    print(row)
#5)
# Program to generate 100 random numbers and find mean, median and mode

import random

numbers = []

# generate 100 random numbers between 100 and 150
for i in range(100):
    numbers.append(random.randint(100, 150))

print("Generated Numbers:")
print(numbers)

# find mean
total = 0
for num in numbers:
    total += num
mean = total / 100

# find median
numbers.sort()
if len(numbers) % 2 == 0:
    mid1 = numbers[49]
    mid2 = numbers[50]
    median = (mid1 + mid2) / 2
else:
    median = numbers[len(numbers)//2]

# find mode
max_count = 0
mode = numbers[0]

for i in numbers:
    count = 0
    for j in numbers:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        mode = i

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
