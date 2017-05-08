def multi(n,m):
    if m == 1:
        return n
    return n + multi(n,m-1)

print(multi(8,5))
