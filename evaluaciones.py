from pizza import Pizza
import os

# a. Imprimir valores de atributos de clase
os.system('cls' if os.name == 'nt' else 'clear') 
print("**Atributos de clase:**")
print(f"Tamaño: {Pizza.tamano}")
print(f"Precio: ${Pizza.precio}")
print(f"Ingredientes proteicos: {Pizza.ingredientes_proteicos}")
print(f"Ingredientes vegetales: {Pizza.ingredientes_vegetales}")
print(f"Tipos de masa: {Pizza.tipos_masa}")

# b. Validar elemento en una lista
print("\n**Validación de elemento en una lista:**")
elemento = "salsa de tomate"
lista_elementos = ["salsa de tomate", "salsa bbq"]
es_presente = Pizza.validar_elemento(elemento, lista_elementos)
print(f"El elemento '{elemento}' {'está' if es_presente else 'no está'} presente en la lista.")

# c. Crear una instancia y solicitar datos al usuario
print("\n**Solicitud de datos de pizza:**")
pizza = Pizza()
pizza.realizar_pedido()

# d. Mostrar información de la instancia
print("\n**Información de la pizza:**")
print(f"Ingredientes vegetales: {pizza.ingrediente_vegetal_1}, {pizza.ingrediente_vegetal_2}")
print(f"Ingrediente proteico: {pizza.ingrediente_proteico}")
print(f"Tipo de masa: {pizza.tipo_masa}")
print(f"Pizza válida: {'Sí' if pizza.es_valida else 'No'}")

# e. Mostrar si la clase Pizza es una pizza válida (error)
print("\n**Validación de la clase Pizza como pizza:**")
try:
    pizza_valida = pizza.es_valida
    print(f"La clase Pizza {'es' if pizza_valida else 'no es'} una pizza válida.")
except AttributeError as error:
    print(f"Error: {error}")
