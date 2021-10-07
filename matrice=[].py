matrice=[]
n=int(input('dati dim matricei de la 2 pina la 10:'))
if n<=10 and n>=2:
  for i in range(0, n):
    m=int(input('dati elementele:'))
    for k in range(0,n):
        matrice.append(m[i][k])
print(matrice)
#diag princ
diagonalaprincipala=[]
for i in range(len(matrice)):
    for k in range(len(matrice[0])) :
        if i==k :
            diagonalaprincipala.append(matrice[i][k])
print('suma diagonalei principale:',sum(diagonalaprincipala))
#diag sec
diagonalasecundara=[] 
for i in range(len(matrice)):
    for k in range(len(matrice[0])) :
        if i+k==n-1:
            diagonalasecundara.append(matrice[i][k])
print('suma diagonalei secundare:',sum(diagonalasecundara)) 
#suma mai sus de diag princ
sumamaisusdediagonalaprincipala=[]
for i in range(len(matrice)):
    for k in range(len(matrice[0])) :
        if i-k<0:
            sumamaisusdediagonalaprincipala.append(matrice[i][k])
print('suma mai sus de diagonala principala:',sum(sumamaisusdediagonalaprincipala))
#suma mai jos de diag princ
sumamaijosdediagonalaprincipala=[]
for i in range(len(matrice)):
    for k in range(len(matrice[0])) :
        if i-k>0 :
            sumamaijosdediagonalaprincipala.append(matrice[i][k])
print('suma mai jos de diagonala principala:',sum(sumamaijosdediagonalaprincipala))
#suma mai sus de diag sec
sumamaisusdediagonalasecundara=[]
for i in range(len(matrice)):
    for k in range(len(matrice[0])):
        if i+k<n-1:
            sumamaisusdediagonalasecundara.append(matrice[i][k])
print('suma mai sus de diagonala secundara:',sum(sumamaisusdediagonalasecundara))
#suma mai jos de diag sec
sumamaijosdediagonalasecundara=[]
for i in range(len(matrice)):
    for k in range(len(matrice[0])):
        if i+k>n-1:
            sumamaijosdediagonalasecundara.append(matrice[i][k])
print('suma mai jos de diagonala secundara:',sum(sumamaijosdediagonalasecundara)) 