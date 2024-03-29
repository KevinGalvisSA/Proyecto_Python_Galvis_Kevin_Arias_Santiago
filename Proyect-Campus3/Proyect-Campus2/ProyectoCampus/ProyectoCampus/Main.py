import Main
import Trainers
import Campers
import Coordinacion
import Reportes
import time

def MenuOpciones(Opciones):
    #Calcular longitud maxima de las opciones
    LongitudMaxima = max(len(Opcion) for Opcion in Opciones)
    
    #Longitud del borde
    LongitudBorde = LongitudMaxima + 2
    
    print("╔" + "═" * LongitudBorde  + "╗")
    
    #Imprimir opciones
    for Opcion in Opciones:
        espaciosFaltantes = LongitudMaxima - len(Opcion)
        print("║ " + Opcion + " " * espaciosFaltantes + " ║")
    
    print("╚" + "═" * LongitudBorde + "╝")


OpcionEscogida = ["                  *Bienvenido al Menu Principal*",
    "═════════════════════════════════════════════════════════════════════",
    "A continuacion, se le presentan las siguientes opciones:",
    "",
    "1. Acceder al menu *Campers*(|Registro-Eliminacion-Muestra|)",
    "",
    "2. Acceder al menu *Trainers*(|Registro-MuestraRutas-Asignacion|)",
    "",
    "3. Acceder al menu *Coordinacion*(|EstadoCamper-AsignacionTrainer|)",
    "",
    "4. Salir"
]

def TerminarMenuPrincipal():
    print("Has decidido salir del menu 'Principal'")
    print("")
    print("Saliendo...")
    time.sleep(3)
    print("Hecho. Ingresando al menu reportes y finalizacion del sistema.")
    time.sleep(3)
    Reportes.menuReportes()

def MenuPrincipal():
    global opc
    while (True):
        
        MenuOpciones(OpcionEscogida)
        
        print("")
        
        opc = int(input("Ingresa el identificador de la opción deseada: "))
        
        Main.MenuPrincipal2()

def MenuPrincipal2():
    global opc
    while (True):
        try:
            if opc  == 1:
                time.sleep(1)
                Campers.MenuCamper()
                
            elif opc  == 2:
                time.sleep(1)
                Trainers.MenuTrainer()
                
            elif opc  == 3:
                time.sleep(1)
                Coordinacion.MenuCoordinacion()
                
            elif opc  == 4:
                time.sleep(1)
                TerminarMenuPrincipal()
                
            else:
                print("No has ingresado uno de los identirficadores disponibles")
        except ValueError as e:
            print("Ha ocurrido un error al ingresar la opcion deseada -->", e)
            print("")
            print("Asegurate de ingresar la opcion correcta tomando en cuenta el identificador ('1', '2', '3' o '4').")

MenuPrincipal()

