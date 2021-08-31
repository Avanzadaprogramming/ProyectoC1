
from Empleado  import Empleado
from Disenador import Disenador
from Agencias import Agencia 
from Portafolio import Portafolio
from Modelo import Modelo
from Artistas import Artista
from Pabellones import Pabellon
from Desfiles import Desfile
from datetime import datetime
from Eventos import Evento
from Bandas import Banda

import random


def inicializacion():
    while True:
        print("-------------------Inicializacion Empresa---------------------")
        print("1. Generacion Automatica de Personal (Empleados,Diseñadores,Modelos,etc)")
        print("2. Ingresar Manualmente Personal (Empleados,Diseñadores,Modelos,etc)")
        respuesta = int(input("Ingrese la opcion: "))
        if respuesta == 1 or respuesta ==2:
            break
        else: print("Intentalo de nuevo")

    empleados = []
    empRasos = []
    empDirec = []
    disenadores = []
    agencias = []
    portafolios = []
    modelos = []
    artistas = []
    bandas = []

    if respuesta == 1: ##AUTOMATICO
        
        ##Empleados
        for i in range(0,random.randint(50,101)):
            empleados.append(Empleado(True,"None",len(empleados)))

        ##Clasificacion Empleados (Raso o Directivo)
        for i in empleados:
            if i.tipo == "directivo":
                empRasos.append(i)
            else:
                empDirec.append(i)
        
        ##Diseñadores
        for i in range(0, random.randint(10, 50)):
            disenadores.append(Disenador(True,"None",len(disenadores)))
        
        ##Agencias 
        for i in range(0,random.randint(10,50)):
            agencias.append(Agencia(True, len(agencias)))
        
        ##Portafolios
        for i in range(0,random.randint(10,150)):
            portafolios.append(Portafolio(len(portafolios)))

        ##Modelos
        for i in range(0,random.randint(50,200) ):
            modelos.append(Modelo(True, "None", len(modelos),random.choice(agencias),random.choice(portafolios)))

        ##Artistas 
        for i in range(0, random.randint(10, 50)):
            artistas.append(Artista(True,"None",len(artistas)))
        
        #Bandas
        for i in range(0,random.randint(3, 10)):
            bandas.append(Banda(True,"None",len(bandas)))



    else:    ##MANUAL 
        while True:
            print("-------------------------------------------------------------")
            try:
                print("IMPORTANTE:SE DEBE CREAR DE EMPLEADO UN RASO Y UN DIRECTIVO (MINIMO DOS EMPLEADOS) ")
                print("IMPORTANTE:SE DEBE CREAR UN DISEÑADOR,AGENCIAS,PORTAFOLIOS,MODELOS,ARTISTAS")
                numEmpleados= int(input("Cuantos Empleados Quieres Crear: "))
                numDisenadores= int(input("Cuantos Diseñadores Quieres Crear: "))
                numAgencias = int(input("Cuantas Agencias Quieres Crear: "))
                numPortafolios = int(input("Cuantos Portafolios De Modelos Quieres Crear: "))
                numModelos= int(input("Cuantos Modelos Quieres Crear: "))
                numArtistas = int(input("Cuantos Artistas Quieres Crear: "))
                numBandas = int(input("Cuatas Bandas Deseas Crear?: "))
                
                break
            except ValueError:
                print("##Error##")
                print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")


        ##Empleados
        for i in range(numEmpleados):
            empleados.append(Empleado(False,"None",len(empleados)))

        ##Clasificacion Empleados (Raso o Directivo)
        for i in empleados:
            if i.tipo == "raso":
                empRasos.append(i)
            else:
                empDirec.append(i)
        
        ##Diseñadores
        for i in range(0, numDisenadores):
            disenadores.append(Disenador(False,"None",len(disenadores)))
        
        ##Agencias 
        for i in range(numAgencias):
            agencias.append(Agencia(False, len(agencias)))
        
        ##Portafolios
        for i in range(numPortafolios):
            portafolios.append(Portafolio(len(portafolios)))

        ##Modelos
        for i in range(numModelos):
            modelos.append(Modelo(False, "None", len(modelos),random.choice(agencias),random.choice(portafolios)))
        ##Artistas 
        for i in range(numArtistas):
            artistas.append(Artista(False,"None",len(artistas)))

        ##Bandas
        for i in range(numBandas):
            bandas.append(Banda(False,"None",len(bandas)))
    print("--------------- !!Generacion De Datos Exitosa!! ----------------")

    return empleados,empRasos,empDirec,disenadores,agencias,portafolios,modelos,artistas,bandas



def mostrar(lista):
    for i in lista:
        print(i)
    print("----------------------------------------------------")




def main():
    nomEmpresa = input("Ingrese el nombre de la Empresa: ")
    empleados,empRasos,empDirec,disenadores,agencias,portafolios,modelos,artistas,bandas=inicializacion()

    print(f"Empleados: {len(empleados)}\nDirectivos: {len(empDirec)}\nRasos: {len(empRasos)}\
\nDiseñadores: {len(disenadores)}\nAgencias: {len(agencias)}\nModelos: {len(modelos)}\nArtistas: {len(artistas)}\nBandas: {len(bandas)}")
    
    pabellones= []
    desfiles = []
    eventos=[]
    while True:
        print(f"--------------------Bienvenido CEO de {nomEmpresa}--------------------------")
        print(f"1.Crear Evento")
        print(f"2.Ver Eventos")
        print(f"3.Ver Menu de Personal")
        print(f"4.Salir")


        while True:
            try:
                respuesta = int(input(f"¿Que desea hacer hoy?: "))
                break
            except ValueError:
                print("##Error##")
                print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")
        
        if respuesta  == 1:
            print("-------------------Crear Evento---------------------")
            print("¿Desea Crear El Evento Automaticamente?")
            print("1.Si")
            print("2.No")

            while True:
                try:
                    automatico = int(input(f"Respuesta: "))
                    break
                except ValueError:
                    print("##Error##")
                    print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

            if automatico == 1:
                print("-----Escogista Automatico-----")
                FechaInicio = input("Ingrese la fecha de INICIO del evento (dia/mes/año): ").strip().split("/")
                FechaFin= input("Ingrese la fecha de FIN del evento (dia/mes/año): ").strip().split("/")
                

                ##Pabellon
                pabellones.append(Pabellon(len(pabellones),random.choice(empleados),str(random.randint(1000000000,9999999999))))

                ##Desfiles
                inicio = datetime(int(FechaInicio[2]),int(FechaInicio[1]),int(FechaInicio[0]))
                final =  datetime(int(FechaFin[2]), int(FechaFin[1]), int(FechaFin[0]))
                for i in range(random.randint(1,10)):
                    fechaAletoria = inicio + (final - inicio) * random.random()
                    modelosDelDesfile= []

                    for k in range(random.randint(10,20)):
                        modelosDelDesfile.append(random.choice(modelos))

                    desfiles.append(Desfile(len(desfiles),f"Desfile{len(desfiles)}",fechaAletoria.date(),fechaAletoria.time(),random.choice(pabellones), random.choice(disenadores),modelosDelDesfile,random.choice(artistas)))
                
                #Evento
                admins = []
                rasos = []

                for i in range(random.randint(2,10)):
                    admins.append(random.choice(empDirec))
                    rasos.append(random.choice(empRasos))

                eventos.append(Evento(len(eventos),inicio,final,desfiles,admins,rasos,str(random.randint(800000,2000000)),str(random.randint(750000,1500000))))
                print("--------------Evento Creado--------------")
                print(eventos[len(eventos)-1])

            else:
                print("Escogista Manual")
                FechaInicio = input("Ingrese la fecha de INICIO del evento (dia/mes/año): ").strip().split("/")
                FechaFin= input("Ingrese la fecha de FIN del evento (dia/mes/año): ").strip().split("/")

                inicio = datetime(int(FechaInicio[2]),int(FechaInicio[1]),int(FechaInicio[0]))
                final =  datetime(int(FechaFin[2]), int(FechaFin[1]), int(FechaFin[0]))

                ##Pabellon
                print("---------------Creacion Pabellon---------------")
                while True:
                    try:
                        print("Si no sabe el ID ingrese -1")
                        numEmpleado = int(input(f"Que Empleado Desea Asigar al pabellon (Ingrese ID del Empleado): "))
                        if numEmpleado == -1:
                            mostrar(empleados)
                        if numEmpleado>=0:
                            break
                    except ValueError:
                            print("##Error##")
                            print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

                

                pabellones.append(Pabellon(len(pabellones),empleados[numEmpleado],str(random.randint(1000000000,9999999999))))

                print("-----------Pabellon Creado-----------")

                ##Desfiles
                print("---------------Creacion Desfiles---------------")
                while True: ##Numero De desfiles
                    try:
                        numDesfiles = int(input(f"Cuantos Desfiles Tiene el evento: "))
                        break
                    except ValueError:
                        print("##Error##")
                        print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")
                
                for i in range(numDesfiles):
                    nomDesfile = input("Ingrese el nombre del desfile: ")
                    Fecha = input("Ingrese la Fecha del desfile")
                    hora = input("Ingrese la hora del desfila")

                    while True: ##Diseñador
                        try:
                            print("Si no sabe el ID del diseñador ingrese -1")
                            numDisenador = int(input(f"Que Diseñador Desea Asigar al desfile (Ingrese ID del diseñador): "))
                            if numDisenador == -1:
                                mostrar(disenadores)
                            if numDisenador>=0:
                                break
                        except ValueError:
                                print("##Error##")
                                print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

                    while True: ##Numero de modelos
                        try:
                            numeroDeModelos = int(input(f"Ingrese la cantidad de modelos que desea "))
                            break
                        except ValueError:
                                print("##Error##")
                                print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")
                    
                    modelosDelDesfile= []

                    for i in range(numeroDeModelos):##Agregar lista de modelos
                        while True:
                            try:
                                print("Si no sabe el ID de la modelo ingrese -1")
                                numModelo = int(input(f"Que modelo Desea Asigar al desfile (Ingrese ID de la modelo): "))
                                if numModelo == -1:
                                    mostrar(modelos)
                                if numModelo>=0:
                                    break
                            except ValueError:
                                    print("##Error##")
                                    print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

                        modelosDelDesfile.append(modelos[numModelo])
                    
                    while True: #Artistas
                        try:
                            print("Si no sabe el ID del Artista ingrese -1")
                            numArtista = int(input(f"Que Artista Desea Asigar al desfile (Ingrese ID del Artista): "))
                            if numArtista == -1:
                                mostrar(artistas)
                            if numArtista>=0:
                                break
                        except ValueError:
                                print("##Error##")
                                print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")


                    desfiles.append(Desfile(len(desfiles),nomDesfile,Fecha,hora,pabellones[len(pabellones)-1],disenadores[numDisenador],modelosDelDesfile,artistas[numArtista]))



                ##Eventos
                rasos = []
                directivos = []
                while True: ##Numero de Directivos
                    try:
                        numeroDeDirectivos = int(input(f"Ingrese la cantidad de trabajadores Directivos que desea: "))
                        break
                    except ValueError:
                        print("##Error##")
                        print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

                        
                for i in range(numeroDeDirectivos):
                    while True: #Lista Directivo
                        try:
                            print("Si no sabe el ID del Trabajador Directivo ingrese -1")
                            numDirectivo = int(input(f"Que Trabajador Directivo desea Asignar al evento (Ingrese ID del Trabajador Directivo): "))
                            if numDirectivo == -1:
                                mostrar(empDirec)
                            if numDirectivo>=0:
                                break
                        except ValueError:
                                print("##Error##")
                                print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")
                    directivos.appen(empDirec[numDirectivo])
                

                while True: ##Numero de Rasos
                    try:
                        numeroDeRasos = int(input(f"Ingrese la cantidad de trabajadores Rasos que desea: "))
                        break
                    except ValueError:
                        print("##Error##")
                        print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero") 



                for i in range(numeroDeRasos):
                    while True: #Lista Directivo
                        try:
                            print("Si no sabe el ID del Trabajador Raso ingrese -1")
                            numRaso = int(input(f"Que Trabajador Raso desea Asignar al evento (Ingrese ID del Trabajador Raso): "))
                            if numRaso == -1:
                                mostrar(empRasos)
                            if numRaso>=0:
                                break
                        except ValueError:
                                print("##Error##")
                                print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")  
                    rasos.append(empRasos[numRaso])

                while True: ##Pago Directivos
                    try:
                        PagoDirectivos = int(input(f"Ingrese el pago de los Directivos: "))
                        break
                    except ValueError:
                        print("##Error##")
                        print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

                while True: ##Pago Rasos
                    try:
                        PagoRasos = int(input(f"Ingrese el pago de los Directivos: "))
                        break
                    except ValueError:
                        print("##Error##")
                        print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")
                
                eventos.append(Evento(len(eventos),inicio,final,desfiles,directivos,rasos,PagoDirectivos,PagoRasos))

        if respuesta == 2:
            mostrar(eventos)
            if len(eventos)== 0:
                print("--No Hay Eventos--")

        if respuesta == 3:
            while True:
                
                print("-------------------Menu De Personal----------------------")
                print(f"1.Ver Todos los Empleados")
                print(f"2.Ver Todos los Empleados Rasos")
                print(f"3.Ver Todos los Empleados Directivos")
                print(f"4.Ver Todos los Diseñadores")
                print(f"5.Ver Todas las Agencias")
                print(f"6.Ver Todas las Modelos")
                print(f"7.Ver Todos los Artistas")
                print(f"8.Ver Todos las Bandas")
                print(f"9.Agregar Empleados")
                print(f"10.Agregar Diseñador")
                print(f"11.Agregar Modelo")
                print(f"12.Agregar Artista")
                print(f"13.Agregar Banda")
                print(f"14.Salir a Menu Principal")
                print("---------------------------------------------------------")
                print("Si no ve ningun cambio en la pantalla mirar arriba del Menu")

                while True:
                    try:
                        respuesta2 = int(input(f"Que desea hacer: "))
                        break
                    except ValueError:
                        print("##Error##")
                        print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

                if respuesta2 == 1:
                    mostrar(empleados)
                elif respuesta2==2:
                    mostrar(empDirec)
                elif respuesta2 == 3:
                    mostrar(empRasos) 
                elif respuesta2 == 4:
                    mostrar(disenadores)
                elif respuesta2 == 5:
                    mostrar(agencias)
                elif respuesta2 == 6:
                    mostrar(modelos)
                elif respuesta2 == 7:
                    mostrar(artistas)
                elif respuesta2 == 8:## Mirar Error
                    mostrar(bandas)
                elif respuesta2 == 9:
                    print("-------------------Crear Empleado---------------------")
                    print("¿Desea Crear El Empleado Automaticamente?")
                    print("1.Si")
                    print("2.No")

                    while True:
                        try:
                            EmpleadoAutomatico = int(input(f"Respuesta: "))
                            break
                        except ValueError:
                            print("##Error##")
                            print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

                    if EmpleadoAutomatico == 1:
                        empleados.append(Empleado(True,"None",len(empleados)))
                        print("---Empleado Creado---")
                    elif EmpleadoAutomatico == 2:
                        empleados.append(Empleado(False,0,len(empleados)))
                        print("---Empleado Creado---")
                    else:
                        print("###Opcion Erronea###")
                elif respuesta2 == 10:
                    print("-------------------Agregar Diseñador---------------------")
                    print("¿Desea Crear El Diseñador Automaticamente?")
                    print("1.Si")
                    print("2.No")

                    while True:
                        try:
                            disenadorAutomatico = int(input(f"Respuesta: "))
                            break
                        except ValueError:
                            print("##Error##")
                            print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

                    if disenadorAutomatico == 1:
                        disenadores.append(Disenador(True,"None",len(disenadores)))
                        print("---Diseñador Creado---")
                    elif disenadorAutomatico == 2:
                        disenadores.append(Disenador(False,"None",len(disenadores)))
                        print("---Diseñador Creado---")
                    else:
                        print("###Opcion Erronea###")
                elif respuesta2 == 11:

                    print("-------------------Agregar Modelo---------------------")
                    print("¿Desea Crear El Evento Automaticamente?")
                    print("1.Si")
                    print("2.No")

                    while True:
                        try:
                            modeloAutomatico = int(input(f"Respuesta: "))
                            break
                        except ValueError:
                            print("##Error##")
                            print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

                    if modeloAutomatico == 1:
                        modelos.append(Modelo(True,"none",len(modelos),random.choice(agencias),random.choice(portafolios)))
                        print("---Modelo Creada---")
                    elif modeloAutomatico == 2:
                        modelos.append(Modelo(False,"none",len(modelos), random.choice(agencias),random.choice(portafolios)))
                        print("---Modelo Creada---")
                    else:
                        print("###Opcion Erronea###")   
                elif respuesta2 == 12:
                    print("-------------------Agregar Artista---------------------")
                    print("¿Desea Crear El Artista Automaticamente?")
                    print("1.Si")
                    print("2.No")

                    while True:
                        try:
                            artistaAutomatico = int(input(f"Respuesta: "))
                            break
                        except ValueError:
                            print("##Error##")
                            print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

                    if artistaAutomatico == 1:
                        artistas.append(Artista(True,"none",len(artistas)))
                        print("---Artista Creado---")
                    elif artistaAutomatico == 2:
                        artistas.append(Artista(False,"none",len(artistas)))
                        print("---Artista Creado---")
                    else:
                        print("###Opcion Erronea###") 
                elif respuesta2 == 13:
                    print("-------------------Agregar Banda---------------------")
                    print("¿Desea Crear La Banda Automaticamente?")
                    print("1.Si")
                    print("2.No")

                    while True:
                        try:
                            bandaAutomatico = int(input(f"Respuesta: "))
                            break
                        except ValueError:
                            print("##Error##")
                            print("Ingresaste un valor no valio, Prueba otra vez ingresando un numero entero")

                    if bandaAutomatico == 1:
                        
                        bandas.append(Banda(True,"none",len(bandas)))
                        print("---Banda Creado---")

                    elif bandaAutomatico == 2:

                        bandas.append(Banda(False,"None",len(bandas)))
                        print("---Banda Creado---")

                    else:
                        print("###Opcion Erronea###")                    
                elif respuesta2 == 14:
                    break           
                else:
                    print("###Opcion Erronea###")
        if respuesta == 4:
            print("AL FINNN TERMINEEEEEEE")
            print("HASTA LUEGO, GRACIAS POR PREFERIRNOS")
            break



                










main()
