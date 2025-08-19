"""
1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
del rectángulo.
"""

class rectangulo:
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h

#ejemplo
r = rectangulo(5, 3)
print(r.area())


"""
2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.
"""

class Mate:
    def __init__(self, n):
        self.max_ceb = n
        self.ceb_rest = n
        self.lleno = False

    def cebar(self):
        if self.lleno:
            raise Exception("cuidado! te quemaste!")
        self.lleno = True

    def beber(self):
        if not self.lleno:
            raise Exception("el mate esta vacio")
        self.lleno = False
        if self.ceb_rest > 0:
            self.ceb_rest -= 1
        else:
            print("el mate se lavo")


"""
3) Botella y Sacacorchos3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho.
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho.
"""


class Botella:
    def __init__(self, bodega):
        self.bodega = bodega
        self.tapa = True  # true = tapada

class Sacacorchos:
    def __init__(self):
        self.corcho = None

    def destapar(self, botella):
        if not botella.tapa:
            raise Exception("botella ya destapada")
        if self.corcho:
            raise Exception("sacacorchos esta ocupado")
        self.corcho = botella
        botella.tapa = False

    def limpiar(self):
        if not self.corcho:
            raise Exception("no hay nada que limpiar")
        self.corcho = None

"""
4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
al método. 
"""

class Rest:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def info(self):
        print(f"{self.nombre} - {self.tipo}")

    def abrir(self):
        print(f"{self.nombre} abierto!")

class Helad(Rest):
    def __init__(self, nombre, tipo, sabores):
        super().__init__(nombre, tipo)
        self.sabores = sabores

    def mostrar_sabores(self):
        print("Sabores:", ", ".join(self.sabores))

#ejemplo
h = Helad("Heladito", "helado", ["chocolate", "frutilla", "vainilla"])
h.mostrar_sabores()


"""
5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
devuelva la cantidad cosechada
"""

class Personaje:
    def __init__(self, vida, pos, vel):
        self.vida = vida
        self.pos = pos
        self.vel = vel

    def recibir(self, daño):
        self.vida -= daño
        if self.vida <= 0:
            raise Exception("Murió!")

    def mover(self, dir):
        if dir == "arriba": self.pos[1] += self.vel
        elif dir == "abajo": self.pos[1] -= self.vel
        elif dir == "izq": self.pos[0] -= self.vel
        elif dir == "der": self.pos[0] += self.vel

class Soldado(Personaje):
    def __init__(self, vida, pos, vel, atk):
        super().__init__(vida, pos, vel)
        self.atk = atk

    def atacar(self, otro):
        otro.recibir(self.atk)

class Campesino(Personaje):
    def __init__(self, vida, pos, vel, cosecha):
        super().__init__(vida, pos, vel)
        self.cosecha = cosecha

    def cosechar(self):
        return self.cosecha



"""
6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.
"""


class User:
    def __init__(self, nom, ape, edad, mail):
        self.nombre = nom
        self.ape = ape
        self.edad = edad
        self.mail = mail

    def info(self):
        print(f"{self.nombre} {self.ape} - {self.edad} años - {self.mail}")

    def saludar(self):
        print(f"Hola {self.nombre}!")



"""
7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.
"""

class Admin(User):
    def __init__(self, nombre, apellido, edad, mail, priv):
        super().__init__(nombre, apellido, edad, mail)
        self.priv = priv

    def mostrar_priv(self):
        print("Privilegios:", ", ".join(self.priv))



"""
8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
el método para mostrar privilegios
"""


class Priv:
    def __init__(self, lista):
        self.lista = lista

    def mostrar(self):
        print("Privilegios:", ", ".join(self.lista))

class Admin(User):
    def __init__(self, nombre, ape, edad, mail, priv):
        super().__init__(nombre, ape, edad, mail)
        self.priv_obj = Priv(priv)

#ejemplo
a = Admin("Luis", "M", 40, "l@mail.com", ["postear", "banear"])
a.priv_obj.mostrar()



"""
9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
funcionó.
"""

class Restaurante:
    def __init__(self, nombre, tipo_comida):
        self.nombre = nombre
        self.tipo_comida = tipo_comida

    def describir(self):
        print(f"{self.nombre} sirve comida {self.tipo_comida}.")

#

r = Restaurante("El Buen Sabor", "italiana")
r.describir()
