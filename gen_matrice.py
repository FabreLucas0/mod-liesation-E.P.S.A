import random as rd

# sortie matrice n² avec pour la somme de chaque ligne egale a x
def genMatricLineEqual(n,x):
    mat = []
    for i in range(n):
        ligne = []
        borne_sup=float(x)
        diff = 0.0
        for j in range(n):
            if j == n-1 :
                ligne.append(round(float(x)-diff,2))
            else :
                tmp = round(rd.uniform(0.0, borne_sup),2)
                ligne.append(tmp)
                borne_sup -= tmp 
                diff += tmp
        mat.append(ligne)

    return mat

# sortie matrice n² avec pour la somme de chaque colone egale a x
def genMatricColEqual(n,x):
    mat =[]
    diff = [0]*n
    borne_sup=[float(x)]*n

    for i in range(n):
        ligne = []
        for j in range(n):
            if i == n-1 :
                ligne.append(round(float(x)-diff[j],2))
            else :
                tmp = round(rd.uniform(0.0, borne_sup[j]),2)
                ligne.append(tmp)
                borne_sup[j] -= tmp 
                diff[j] += tmp
        mat.append(ligne)

    return mat



# sortie matrice n² avec pour la somme de la diagonale sera egale a x le 
# si le reste est a 0 alors la matrice sera remplie avec des 0
# sinon les chiffre seron random
def genMatricDiagEqual(n,x,reste):
    mat =[]
    diff = 0
    borne_sup=float(x)

    for i in range(n):
        ligne = []
        for j in range(n):
            if i == n-1 and j ==n-1 :
                ligne.append(round(float(x)-diff,2))
            elif i==j :
                tmp = round(rd.uniform(0.0, borne_sup),2)
                ligne.append(tmp)
                borne_sup -= tmp 
                diff += tmp
            elif reste == 0 :
                ligne.append(0.0)
            else :
                ligne.append(round(rd.uniform(0.0, float(x)),2))
        mat.append(ligne)

    return mat