class Pizza:
    # Atributos de clase:
    precio = 10000
    tamano = 'familiar'
    ingredientes_proteicos = ("Pollo", "Vacuno", "Carne vegetal")
    ingredientes_vegetales = ("Tomate", "Aceitunas", "Champiñones")
    tipos_masa= ("Tradicional", "Delgada")

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingrediente_vegetal_1 = None
        self.ingrediente_vegetal_2 = None
        self.tipo_masa = None
        self.es_valida = False

    # Métodos

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento.lower() in [valor.lower() for valor in valores_posibles]

    def realizar_pedido(self):
        # Solicitud de datos al usuario
        # Probablemente me quedo muy largo y repetitivo, pero no me da el tiempo para darle otra vuelta
        existe = False
        while existe == False:
            self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
            existe = Pizza.validar_elemento(self.ingrediente_proteico, Pizza.ingredientes_proteicos)
            print(f"El elemento '{self.ingrediente_proteico}' {'está' if existe else 'no está'} presente en la lista.")

        existe = False
        while existe == False:
            self.ingrediente_vegetal_1 = input("Ingrese el primer ingrediente vegetal: ")
            existe = Pizza.validar_elemento(self.ingrediente_vegetal_1, Pizza.ingredientes_vegetales)
            print(f"El elemento '{self.ingrediente_vegetal_1}' {'está' if existe else 'no está'} presente en la lista.")

        existe = False        
        while existe == False:
            self.ingrediente_vegetal_2 = input("Ingrese el segundo ingrediente vegetal: ")
            existe = Pizza.validar_elemento(self.ingrediente_vegetal_2, Pizza.ingredientes_vegetales)
            print(f"El elemento '{self.ingrediente_vegetal_2}' {'está' if existe else 'no está'} presente en la lista.")

        existe = False
        while existe == False:
            self.tipo_masa = input("Ingrese el tipo de masa (tradicional/delgada): ")
            existe = Pizza.validar_elemento(self.tipo_masa, Pizza.tipos_masa)
            print(f"El elemento '{self.tipos_masa}' {'está' if existe else 'no está'} presente en la lista.")


        # Validación de los datos
        es_proteico_valido = Pizza.validar_elemento(
            self.ingrediente_proteico, Pizza.ingredientes_proteicos
        )
        es_vegetal_1_valido = Pizza.validar_elemento(
            self.ingrediente_vegetal_1, Pizza.ingredientes_vegetales
        )
        es_vegetal_2_valido = Pizza.validar_elemento(
            self.ingrediente_vegetal_2, Pizza.ingredientes_vegetales
        )
        es_masa_valida = Pizza.validar_elemento(self.tipo_masa, Pizza.tipos_masa)

        # Asignación del valor de validez
        self.es_valida = (
            es_proteico_valido
            and es_vegetal_1_valido
            and es_vegetal_2_valido
            and es_masa_valida
        )

    def mostrar_informacion(self):
        if self.es_valida:
            print(f"**Pizza válida:**")
            print(f"Tamaño: {self.tamano}")
            print(f"Precio: ${self.precio}")
            print(f"Ingrediente proteico: {self.ingrediente_proteico}")
            print(f"Ingrediente vegetal 1: {self.ingrediente_vegetal_1}")
            print(f"Ingrediente vegetal 2: {self.ingrediente_vegetal_2}")
            print(f"Tipo de masa: {self.tipo_masa}")
        else:
            print("**Pizza no válida. Ingrese datos correctos.")