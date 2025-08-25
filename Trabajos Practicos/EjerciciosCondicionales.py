#Se le solita al usuario la fecha con el formato solicitado
fecha_solicitada = input('Ingrese la fecha actual con el siguiente formato "dia, DD/MM" donde dia es el dia actual, DD el numero del dia y MM es el mes: ')

#Variables constantes
DIAS_POSIBLES = ["lunes","martes","miercoles","jueves","viernes"]
DIAS_POSIBLES_CON_EXAMENES = ["lunes","martes","miercoles"]
DD_POSIBLES = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
MM_POSIBLES= ["01","02","03","04","05","06","07","08","09","10","11","12"]
#Se separa la fecha con un split con el formato solicitado para su proceso
fecha_formato= fecha_solicitada.split(', ')
#Se declaran las variables con el formato a utilizar
dia= fecha_formato[0].lower()
dd= int(fecha_formato[1].split('/')[0])
mm= fecha_formato[1].split('/')[1]
#Se valida por las fechas estan dentro del rango posibles
if(dia in DIAS_POSIBLES and dd in DD_POSIBLES and mm in MM_POSIBLES):
    #Se valida si el dia se encuentra en los posibles con examenes
    if(dia in DIAS_POSIBLES_CON_EXAMENES):
        #Se pregunta si hubo examenes
        respuesta = input(f"Hubo examenes el dia {dia} responde SI o NO, segun corresponda: ").upper()
        #Se valida si hubo examens
        if(respuesta == "SI"):
            #En el caso de q si hubo se pregunta la cantidad de alumnos aprobados y desaprobados y se imprime el porcentaje
            alumnos_aprobados = float(input("Cuantos alumnos aprobraron el examen: "))
            alumnos_desaprobados = float(input("Y cuantos alumnos desaprobaron el examen: "))
            total_alumnos = alumnos_aprobados + alumnos_desaprobados
            print("El porcentaje de almunos aprobados fue del: ", round((alumnos_aprobados / total_alumnos)*100,2), "%")
        elif(respuesta == "NO"):
            #No hubo examenes esta dia
            print("No hubo examenes el dia: ", dia)
        else:
            #Respuesta por default si no ingresa una valida
            print("Respuesta no valida")
    elif(dia == "jueves"):
        #Se pide el porcentaje de alumnos presentes si el dia es jueves para comprobar si asistieron la mayoria
        porcentaje_alumnos_presentes = int(input("Ingrese el porcentaje de alumnos presentes: "))
        if(porcentaje_alumnos_presentes < 50):
            print("No asistio la mayoria de alumnos")
        else:
            print("Asistio la mayoria de alumnos")
    elif(dia == "viernes"):
        #Si el dia es el primero del mes 01 o del 07 se imprime el comiendo de un nuevo ciclo y se calcula el total de ingreso de dinero
        if(dd == 1 and (mm == "01" or mm == "07")):
            print("Comienzo de nuevo ciclo")
            total_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel = int(input("Ingrese el arancel por cada alumno en $: "))
            print("El ingreso total es de: ", total_alumnos * arancel)
        else:
            print("Clase de Ingles para Viajeros")
else:
    print("Inserte una fecha valida con el formato dia, DD/MM")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    