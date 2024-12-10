for _ in range(10):
    p = float(input("Enter principal (p): "))
    r = float(input("Enter annual rate (r): "))
    n = int(input("Enter years (n): "))
    q = int(input("Enter times compounding per year (q): "))
    a = p * ((1 + (r / (100 * q))) ** (n * q))
    print(f"Compound amount: {a}")
