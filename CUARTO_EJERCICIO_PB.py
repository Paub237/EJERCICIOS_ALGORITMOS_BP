#Vamos a crear un código que realice por pantalla un cálculo de variables, que nos permita sumar, 
#restar y hacer operaciones para mostrar al final un resulatdo de cada operación y a su vez crear una tabla de
#la verdad y cada una de las operaciones usando "bool" o usando "and y or"

a = input ("Ingrese un numero en pantalla ")
b = input ("Ingrese un numero mayor que el anterior")

a = int(a)
b = int (b) 

print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (a % b)


print (bool(a==a))
print (bool (a==b))


print ("Tabla de la verdad, todo lo relacinado con And o Y" "v DISYUNCIÓN")
print ((str(a==a)) + "and" + str (a==a) + "--->" + str (a==a))
print ((str(a==a)) + "and" + str (a==b) + "--->" + str (a==b))
print ((str(a==b)) + "and" + str (b==b) + "--->" + str (a==b))
print ((str(a==b)) + "and" + str (a==b) + "--->" + str (a==b))

print ("Tabla de la verdad, todo lo relacionado con Or u O" "^ CONJUNCIÓN")
print ((str(a==a)) + "and" + str (a==a) + "-->" + str (a==a))
print ((str(a==a)) + "and" + str (a==b) + "-->" + str (a==a))
print ((str(a==b)) + "and" + str (b==b) + "-->" + str (a==a))
print ((str(a==b)) + "and" + str (a==b) + "-->" + str (a==b))


