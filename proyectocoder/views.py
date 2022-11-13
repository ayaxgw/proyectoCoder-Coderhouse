from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template, loader


def vistaSaludo(request):
    return HttpResponse("Hola Coders! :)")

def iniciarSesion(request):
    return HttpResponse("Ingresa username & password por Wsp")

def diaHoy(request, nombre):    
    hoy = datetime.now()
    respuesta = f"Hoy es {hoy} - Bienvenido {nombre}"
    return HttpResponse(respuesta)
    
def añoNacimiento(request, edad):

    edad = int(edad)

    añoNacimiento = datetime.now().year - edad

    return HttpResponse(f"Naciste en {añoNacimiento}")

def vistaPlantilla(request):

    # Abrimos el archivo
    archivo = open(r'proyectocoder\templates\plantilla_bonita.html')
    
    # Creamos el objeto "plantilla"
    plantilla = Template(archivo.read())
    
    #Cerramos archivo para liberar recursos
    archivo.close()
    
    # Diccionario con datos para la plantilla
    datos = {"nombre":"Ayax", "fecha": datetime.now(), "apellido":"Garcia Williner", "edad":"24 años"}
     
    # Creamos el contexto
    contexto = Context(datos)
    
    # Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)
    
    # Retornamos la respuesta
    return HttpResponse(documento)

def vista_listado_alumnos(request):

    # Abrimos el archivo
    archivo = open(r"proyectocoder\templates\listado_alumnos.html")

    # Creamos el template
    plantilla = Template(archivo.read())

    # Cerramos el archivo
    archivo.close()

    # Creamos el diccionario de datos
    listado_alumnos = ["Leonel Gareis", "Ayax Garcia Williner", "Cristian Garcia","Diego Ibarra", "Santiago Ortiz", "Barbara Vivante"]

    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    # Creamos el contexto
    contexto = Context(datos)
    
    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)

def vista_listado_alumnos2(request):

    # Creamos el diccionario de datos
    listado_alumnos = ["Leonel Gareis", "Ayax Garcia Williner", "Cristian Garcia","Diego Ibarra", "Santiago Ortiz", "Barbara Vivante"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template(r"listado_alumnos.html")
    documento = plantilla.render(datos)

    return HttpResponse(documento)