
while True:
 try:  
     x=int(input("inserte un numero mayor a 10:"))
     if x>10:
          print("Verdadero")
          i=+1
     else:
          print("Falso")
     break
 except ValueError:
     print ("no valido")