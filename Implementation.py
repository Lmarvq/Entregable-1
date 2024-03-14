from Clases import *

def main():
    while True:
        try:
            print("¡Bienvenido al Sistema X!\nEscoja la acción a ejecutar.")
            sis = Sistema()
            menu = int(input("1-Agregar implante\n2-Editar implante\n3-Eliminar implante\n4-Visualizar el inventario completo\n5-Salir\nUsted ingresó: "))
            if menu == 1:
                sis.IngresarImplante()
            if menu == 2:
                sis.EditarImplante()
            if menu ==3:
                sis.EliminarImplante()
            if menu == 4:
                sis.VisualizarInventario()
            if menu == 5:
                op1 = int(input("¿Está seguro que desea salir del sistema?\n1-Si\n2-No"))
                if op1 == 1:
                    break
                if op1 == 2:
                    continue
        except: (ValueError, TypeError)
        print("Por favor ingrese una de las opciones diseñadas")
        continue
        
main()