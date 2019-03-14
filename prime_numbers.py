import matplotlib.pyplot as plt
import math

def is_prime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

def check_palindrome(x):
    new_x = list(map(int, str(x)) )
    palindrome = False
    if (new_x) == (new_x)[::-1]:
        palindrome = True
    return palindrome

palindromes = []
x_coords = []
x = 0
for i in range(1,10000):
    if is_prime(i):
        x += 1
        x_coords.append(x)
        palindromes.append(i)

print(palindromes)

plt.scatter(x_coords,palindromes,s=5)
plt.show()
