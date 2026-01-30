def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def euler_phi(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count
n = int(input("Enter the value of n: "))
print("Phi(", n, ") :", euler_phi(n))