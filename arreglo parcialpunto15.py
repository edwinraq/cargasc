import math
cargaTNT = int(input("Digite la carga de TNT en kg: "))
aux = input("Digite coordenada de la bomba: ")
aux = aux.split(",")
coorTNTx = int(aux[0])
coorTNTy = int(aux[1])
aux2 = input("Digite coordenada de la poblacion: ")
aux2 = aux2.split(",")
coorPoblacionx = int(aux2[0]) 
coorPoblaciony = int(aux2[1])
d = math.sqrt((math.pow((coorTNTx - coorPoblacionx),2) + math.pow((coorTNTy - coorPoblaciony),2)))
bandera = False
printfinal = ""

if(d>=0 and d<(cargaTNT*3)):
  printfinal = "TOTAL"
  bandera = True
  
if (d>=(cargaTNT*3) and d<(cargaTNT*7)):
  printfinal = "MORTAL"
  bandera = True
  
if (d>=(cargaTNT*7) and d<(cargaTNT*10)):
  printfinal = "GRAVE"
  bandera = True
  
if (d>=(cargaTNT*10) and d<(cargaTNT*15)):
  printfinal = "LEVE"
  bandera = True
  
if(bandera == False):
  print("La poblacion esta a salvo")
else:
  print("\nDaño a la poblacion:",printfinal)
