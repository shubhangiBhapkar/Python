import math

class Assignment:

    def find_maximum(self, a, b, c):
        if a > b and a > c:
            return a
        elif b > c:
            return b
        else:
            return c
    
    def find_largest(self, numbers):
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        return largest

    def linear_search(self, arr, target):
        for i in arr:
            if i == target:
                print(f"{target} is found in the array {arr}")
                return
        print(f"{target} is not found in the array {arr}")

    def factorial(self, n):
        if n < 0:
            return "Factorial is not defined for negative numbers."
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def prime(self, n):
        if n < 2:
            print(f"{n} is not a prime number")
            return
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                print(f"{n} is not a prime number")
                return
        print(f"{n} is a prime number")

# Create an object of the class
obj = Assignment()

# Find the largest number among three
print("Largest number among three:")
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print(f"Largest number: {obj.find_maximum(a, b, c)}")

# Find the largest number in a list
numbers = [12, 7, 54, 3, 87, 1]
print(f"The largest number in the list {numbers} is: {obj.find_largest(numbers)}")

# Perform linear search
target = 50
arr = [10, 20, 30, 40, 50]
obj.linear_search(arr, target)

# Calculate factorial
n = int(input("Enter a number to calculate factorial: "))
print(f"The factorial of {n} is {obj.factorial(n)}")

# Check if a number is prime
num = int(input("Enter a number to check if it is prime: "))
obj.prime(num)
