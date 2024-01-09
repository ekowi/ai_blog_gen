def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y


# Example usage:
num1 = 252
num2 = 198

gcd_result, x, y = extended_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}")
print(f"Bézout coefficients (x, y): ({x}, {y})")
