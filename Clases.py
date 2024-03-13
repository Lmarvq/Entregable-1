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

def AsignarTipoImplante(self):
        while True:
            try:
                Tipo_Im = input("Ingrese el tipo de implante a buscar: \n1-Marcapasos\n2-Stent coronario\n3-Implante dental\n4-Implante cadera\n5-Implante rodilla")
                if Tipo_Im == 1:
                    i = Marcapasos()
                    return i
                if Tipo_Im == 2:
                    i = Stent_Coronario()
                    return i
                if Tipo_Im == 3:
                    i = Implante_Dental()
                    return i
                if Tipo_Im == 4:
                    i = Implante_Cadera()
                    return i
                if Tipo_Im == 5:
                    i = Implante_Rodilla()
                    return i
                
            except: ValueError, TypeError
            print("Por favor ingrese uno de los valores numéricos asignados.")
            continue
def VerificarSerial():
    i = AsignarTipoImplante()
    while True: 
                        try :
                                s = input("Ingrese el serial del implante")
                                if s is int:
                                    serial = i.ObtenerS()

                                    if serial == s: 
                                        print("El serial ingresado corresponde a otro implante de la misma categoría, si pretende hacer un registro ingrese uno distinto.")
                                        op1 = int(input("¿Desea hacer un registro?\n 1-Si\n2-No."))
                                        if op1 == 1:
                                            continue
                                        if op1 == 2:
                                             existe = True
                                             return existe
                                    else:
                                        existe = False
                                        return existe
                        except: ValueError, TypeError
                        print("Ingrese únicamente valores numéricos, sin puntos o comas de por medio")
        

class Sistema():
    def __init__(self):
        self.__listaPAC ={}
        self.__IventarioImplantes = []
    
    def IngresarImplante(self):
            while True:
                try:
                    i = AsignarTipoImplante()
                    a = VerificarSerial()
                    if a == False:
                        t = input("Ingrese el tamaño del implante: \n")
                        m = input("Ingrese el material del implante: \n")
                        i.AsignarT(t)
                        i.AsignarM(m)
                        if i == 1:
                                ne = int(input("Ingrese el número de electrodos: \n"))
                                tipo = input("Ingrese el tipo del marcapasos: \n")
                                frecuencia = input("Ingrese la frecuencia de estimulación del marcapasos: \n")
                                i.AsignarNE(ne)
                                i.AsignarTipo(tipo)
                                i.AsignarF(frecuencia)
                                pass
                        if i ==2:
                                long = input("Ingrese la longitud del Stent coronario: \n")
                                diam = input("Ingrese el diámetro del Stent coronario: \n")
                                i.AsignarLongitud(long)
                                i.AsignarDiametro(diam)
                                pass
                        if i ==3:
                                sfij = input("Ingrese el sistema de fijación del implante dental: \n")
                                forma = input("Ingrese la forma del implante dental: \n")
                                i.AsignarSF(sfij)
                                i.AsignarForma(forma)
                                pass
                        if i == 4:
                                tfij = input("Ingrese el tipo de fijación de la prótesis de cadera: \n")
                                i.AsignarTF(tfij)
                                pass
                        if i == 5:
                                tfij = input("Ingrese el tipo de fijación de la prótesis de rodilla: \n")
                                i.AsignarTF(tfij)
                                pass
                    self.__IventarioImplantes.append(i)

                except: ValueError, TypeError
                print("Ingrese únicamente valores numéricos que no estén separados por puntos y/o comas")
                continue
                
    def EliminarImplante(self):
         while True:
            try:
                 i = AsignarTipoImplante()
                 a = VerificarSerial()

                 if a == True:
                    for i in self.__IventarioImplantes:
                         if i.ObtenerS == a:
                              del i
                              print(f"El implante con serial {i.ObtrenerS} y de tipo {i} ha sido eliminado del sistema")
            except:  ValueError, TypeError
        
    

 
     #eliminarlos, editar su información y visualizar el inventario completo.
