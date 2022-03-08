n = int (input("entrer un nombre"))

for i in range (1, n+1):
    if (n%2==0):
        n=n//2
    else:
        n=n*3+1
    print (n)
