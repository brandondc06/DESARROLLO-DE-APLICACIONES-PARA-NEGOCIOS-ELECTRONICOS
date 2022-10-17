#Listas en python



print("Lista 4 numeros: ")
a=[57,45,7,13,5,8]
print(a)

print("Lista de 3 String: ")
b=["Hola","Chau","buen dia","Hi","Bye","Sayonara"]
print(b)

print("Longitud de la lista: ")
n=len(a)
print(n)


# para acceder a sus elementos se debe 
# utilizar el []
# los indices comienzan con 0

print("Elemento con indice 0 de la lista: ")
print(b[0])
print("Elemento con indice 1 de la lista: ")
print(b[1])
print("Elemento con indice 2 de la lista: ")
print(b[2])
# ***********************************************

vaciar=[]
print("lista vacia: ")
print(vaciar)
# crear sublista
print("Elemento del indice 0 al 1 (2-1): ")
print(a[0:2])
print("Elementos del indice 1 al 3 (4-1): ")
print(a[1:4])



# ********************************************

# agregar un elemento a la lista 
print("una lista con 3 string: ")
a=['una','lista','de']
print(a)

print("La misma lista luego de agregar un String ")
a.append('string')
a.append('ratona')
a.append('malvada')
print(a)

# ************************************************
# TUPLAS son como las listas, pero no
# se pueden modificar, son listas de solo lectura 

a=(1,2,57,4)
print("una tupla de 4 elementos: ")
print(a)
print("el elemento con indice 2: ")
print(a[2])
print("Los elementos entre los indices 0 y 2: ")
print(a[0:2])

# ***********************************************
# sentencias if
edad=17
print("la persona es: ")
if edad < 18:
    # identacion
    print("menor")
else:
    print("Mayor")

print("de edad")

# ***************************************
# usando el metodo for
subjects=["matematias","español","quimica","ingles"]
scores=[]
for subjects in subjects:
    scores= input("que nota has sacado" + subjects + "?")
    scores.append(scores)
for i in range (len(subjects)):
    print("en" + subjects[i] + "has sacado" + scores[i])


