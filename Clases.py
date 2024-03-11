class Implante():
    def __init__(self):
        self.__tamaño = 0
        self.__material = ""
        self.__serial = int

    def AsignarT(self, t):
        self.__tamaño = t
    def AsignarM(self, m):
        self.__material = m
    def AsignarS(self, s):
        self.__serial = s

    def ObtenerT(self):
        return self.__tamaño
    def ObtenerM(self):
        return self.__material
    def ObtenerS(self):
        return self.__serial

class Marcapasos(Implante):
    def __init__(self):
        super(Implante).__init__()
        self.__NElectrodos = 0
        self.__tipo = ""
        self.__frecuencia = 0

    def AsignarNE(self, ne):
        self.__NElectrodos = ne
    def AsignarTipo(self, tipo):
        self.__tipo = tipo
    def AsignarF(self, f):
        self.__frecuencia = f

    def ObtenerNE(self):
        return self.__NElectrodos
    def ObtenerTipo(self):
        return self.__tipo
    def ObtenerF(self):
        return self.__frecuencia
    
class Stent_Coronario(Implante):
    def __init__(self):
        super(Implante).__init__()
        self.__longitud = 0
        self.__diametro = 0

    def AsignarLongitud(self, l):
        self.__longitud = l
    def AsignarDiametro(self, d):
        self.__diametro = d
        
    def ObtenerLong(self):
        return self.__longitud
    def ObtenerDiametro(self):
        return self.__diametro

class Implante_Dental(Implante):
    def __init__(self):
        super(Implante).__init__()
        self.__sistemafijacion = ""
        self.__forma = ""

    def AsignarSF(self, sf):
        self.__sistemafijacion = sf
    def AsignarForma(self, f):
        self.__forma = f
        
    def ObtenerForma(self):
        return self.__forma
    def ObtenerSF(self):
        return self.__sistemafijacion
    
class Implante_Cadera(Implante):
    def __init__(self):
        super(Implante).__init__()
        self.__tipofijacion = ""
    
    def AsignarTF(self, tf):
        self.__tipofijacion = tf
    def ObtenerTF(self):
        return self.__tipofijacion

class Implante_Rodilla(Implante):
    
    def __init__(self):
        super(Implante).__init__()
        self.__tipofijacion = ""
    
    def AsignarTF(self, tf):
        self.__tipofijacion = tf
    def ObtenerTF(self):
        return self.__tipofijacion
    
class Paciente():
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__implantes = []
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__implantes
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,i):
        self.__implantes.append(i)
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c
    





 #nuevos implantes, eliminarlos, editar su información y visualizar el inventario completo.

#Funciones
def VerificarSerial(self):
        while True:
            try:    
                    existe = True
                    Tipo_Im = input("Ingrese el tipo de implante a buscar: \n1-Marcapasos\n2-Stent coronario\n3-Implante dental\n4-Implante cadera\n5-Implante rodilla")
                    if Tipo_Im == 1:
                        i = Marcapasos()
                        pass
                        
                    if Tipo_Im == 2:
                        i = Stent_Coronario()
                        pass
                    if Tipo_Im == 3:
                        i = Implante_Dental()
                        pass
                    if Tipo_Im == 4:
                        i = Implante_Cadera()
                        pass
                    if Tipo_Im == 5:
                        i = Implante_Rodilla()
                        pass
                    
                    while True: 
                        try :
                                s = input("Ingrese el serial del implante")
                                if s is int:
                                    serial = i.ObtenerS()

                                    if serial == s: 
                                        print("El serial ingresado corresponde a otro implante de la misma categoría, ingrese uno distinto para el registro.")
                                        continue
                                    else:
                                        existe = False
                                        return s, existe
                                    
                        except: ValueError, TypeError
                        print("Ingrese únicamente valores numéricos")
                        continue
                
            except: ValueError, TypeError
            print("Por favor ingrese uno de los valores numéricos asignados.")
            continue


class Sistema():
    def __init__(self):
        self.__listaPAC ={}
        self.__IventarioImplantes = []

    def Ingresar_Implante():
        VerificarSerial()
        if VerificarSerial == False:
            pass #Añadir información al implante, considerando que ya tenemos serial y clase