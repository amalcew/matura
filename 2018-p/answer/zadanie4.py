#Podciąg rosnący

def PodciągRosnący(lista):
  lista_rosnąca=[1 for i in range(len(lista))]           
  for i in range(len(lista)):
    for j in range(i-1,-1,-1):
      if lista[j] < lista[i] and lista_rosnąca[j] >= lista_rosnąca[i]:
        lista_rosnąca[i]=lista_rosnąca[j]+1
  k=max(lista_rosnąca)
  g.write(str(k) +'\n')

f=open('ciagi.txt','r')
g=open('podciagi.txt','r+')

n=int(f.readline())
for i in range(n):
  lista=[]
  for val in f.readline().split():
    lista.append(int(val))
  del lista[0] 
  PodciągRosnący(lista)
f.close()
for val in g.readline():
  print(int(val))
g.close()

