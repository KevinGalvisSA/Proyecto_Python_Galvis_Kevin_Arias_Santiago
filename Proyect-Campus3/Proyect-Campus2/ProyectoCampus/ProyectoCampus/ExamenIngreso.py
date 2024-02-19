import json
import RegresarCoordinacion

def NotasExamenIngreso():
    with open("Campers.json", "r") as Archivo:
        dato = json.load(Archivo)
        # Iterar sobre la lista de tuplas
    # Cargar el archivo JSON
    with open('ExamenIngreso.json', 'r') as archivo:
        data = json.load(archivo)
    Lista = [(clave, valor) for clave, valor in dato.items()]
    for clave, diccionario_interno in Lista:
        documento = input("Ingrese el documento del camper al cual se le asignara la nota: ")
        if clave == documento:
            print("Documento:", clave)
            print("Camper:", diccionario_interno)
            # Crear un nuevo diccionario con los datos del examen
            nombre = str(input("Ingrese el nombre del camper al cual se le asignara la nota: "))
            if diccionario_interno["nombre"] == nombre :
                print(f"Has decidio modificar las notas del camper -> {nombre}.")
                NotaTeorica = int(input("Ingrese el resultado de la nota del examen teorico: "))
                NotaPractica = int(input("Ingrese el resultado de la nota del examen practico: "))
                NotaSumadas = NotaPractica + NotaTeorica 
                NotaPromedio = NotaSumadas / 2
                if NotaPromedio < 60 :
                    print("|-EXAMEN REPROVADO-|")
                    print("El camper no puede ser aprovado.")
                    if diccionario_interno["estado"]=="Inscrito":
                        diccionario_interno["estado"]="Reprovado"
                        NuevoEstado = diccionario_interno["estado"]
                        print(f"El nuevo estado del camper es: {NuevoEstado}.")
                        NotaIngreso = NotaPromedio
                        Resultados = {
                            "Nombre": nombre,
                            "Nota": NotaIngreso
                        }
                        # Agregar el resultado la lista de resultados en el archivo JSON
                        data["Resultados"].append(Resultados)
                        # Guardar los datos actualizados en el archivo JSON
                        with open('ExamenIngreso.json', 'w') as archivo:
                            json.dump(data, archivo, indent=4)
                        with open('ExamenIngreso.json', 'r') as archivo:
                            LeerNotas = json.load(archivo)
                            print(LeerNotas)
                            break
                    else:
                        print("El estado del camper no es el correcto")
                elif NotaPromedio >= 60 :
                    print("|-EXAMEN APROVADO-|")
                    print("El camper califica para ingresar a ||-CAMPUSLAND-||")
                    if diccionario_interno["estado"]=="Inscrito":
                        diccionario_interno["estado"]="Aprovado"
                        NuevoEstado = diccionario_interno["estado"]
                        print(f"El nuevo estado del camper es: {NuevoEstado}.")
                        NotaIngreso = NotaPromedio
                        Resultados = {
                            "Nombre": nombre,
                            "Nota": NotaIngreso
                        }
                        # Agregar el resultado la lista de resultados en el archivo JSON
                        data["Resultados"].append(Resultados)
                    else:
                        print("El estado del camper no es el correcto")
                    # Guardar los datos actualizados en el archivo JSON
                    with open('ExamenIngreso.json', 'w') as archivo:
                        json.dump(data, archivo, indent=4)
                    with open('ExamenIngreso.json', 'r') as archivo:
                        LeerNotas = json.load(archivo)
                        print(LeerNotas)
                        break
            else:
                print(f"El camper que has igresado {nombre}. NO se encuentra registrado")
        else:
            print("El documento que ingresaste NO esta registrado")
    RegresarCoordinacion.regresarMenuC()






