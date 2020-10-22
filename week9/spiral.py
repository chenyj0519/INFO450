def sum(i):
    n = (i-1) // 2
    return 1+2*n*(8*n*n+15*n+13)/3

i = int(input("Enter the number: "))
print (" The sum is ",sum(i))
