def sum(i):
    n = (i-1) // 2
    return (16*n**3 + 30*n**2 + 26*n + 3) // 3

i = int(input("Enter 501: "))
print (" The sum is ",sum(i))
