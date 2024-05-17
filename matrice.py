import numpy as np
#py -m pip install numpy

def ProduitMa(A,B):
 produit=[[0,0,0],[0,0,0],[0,0,0]]
 
 for i in range(len(A)):
      for j in range(len(B)):
       for k in range(len(A)):
         produit[i][j]=produit[i][j]+A[i][k]*B[k][j]

 print(A)
 print(B)
 print()
 
 for row in produit:
  print(row)
  


A=[[0,3,1],[3,1,2],[3,0,0]]
B=[[0,2,2],[0,1,1],[3,2,0]]

ProduitMa(A,B)

A=np.array([[0,3,1],[3,1,2],[3,0,0]])
B=np.array([[0,2,2],[0,1,1],[3,2,0]])

print("Multi :(np.dot(A,B) we can also do it for a list")
print(np.dot(A,B))
print("Transposé:A.T")
print(A.T)
print("Conjugéé: np.conj(A)")
print(np.conj(A))

print(np.size(A))
print(np.shape(A))




