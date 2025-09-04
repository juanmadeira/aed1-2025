def faz(n):
    print(f"oi {n}")
    if n > 998:
        return
    faz(n + 1)
    print(f"tchau {n}")

faz(1)
