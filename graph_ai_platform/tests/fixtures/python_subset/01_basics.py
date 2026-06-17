# 1. Simple function
def greet(name):
    return f"Hello, {name}!"

# 2. If/elif/else
def classify(x):
    if x > 0:
        return "positive"
    elif x == 0:
        return "zero"
    else:
        return "negative"

# 3. For loop
def sum_list(items):
    total = 0
    for item in items:
        total = total + item
    return total

# 4. While loop
def countdown(n):
    result = []
    while n > 0:
        result.append(n)
        n = n - 1
    return result

# 5. Class definition
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count = self.count + 1
    
    def get_count(self):
        return self.count

# 6. Import
import math
from os import path

# 7. Nested control flow
def factorial(n):
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return 1
    result = 1
    i = 1
    while i <= n:
        result = result * i
        i = i + 1
    return result

# 8. Break/Continue
def find_first(seq, target):
    for i in range(len(seq)):
        if seq[i] == target:
            break
        if seq[i] < 0:
            continue
        print(f"checking {seq[i]}")
    return i

# 9. Binary operation chains
def quadratic(a, b, c, x):
    return a * x * x + b * x + c

# 10. Simple assignment
x = 1
y = x + 1
z = y * 2
