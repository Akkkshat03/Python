def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n_terms = 7
series_sum = 0
for n in range(1, n_terms + 1):
    series_sum += n / factorial(n)
print(f"Sum of series: {series_sum}")
