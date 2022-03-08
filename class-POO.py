class Syracuse():
    def get_N(N):
        f=open("Syracuse.txt", "w")
        f.write("%d " %N)

        for i in range(1, n+1):
            if N%2==0:
                N=N//2
            else:
                N=3*N+1
            f.write("%d " %N)
        f.close()

N= int(input("Entrer le nombre entier N= "))
n= int(input("Le numéro de la suite que vous souhaitez n= "))
Syracuse.get_N(N)