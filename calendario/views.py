from django.shortcuts import render
from .models import Evento
from .forms import SimpleForm
from datetime import date, datetime, timedelta
import calendar

now = datetime.now()
form = SimpleForm
# Create your views here.


def atribuir_tareas(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        nota = request.POST['nota']
        hora_fecha = request.POST['hora_fecha']
        relevancia = request.POST['relevancia']
        evento = Evento.objects.create(nombre_e=nombre,nota_e=nota,hora_fecha_e=hora_fecha,valoracion_e=relevancia, finalizado_e=False)
        evento.save()

    return render(request,"atribuir_tareas.html",{"form":form, 'fecha':now})


def tareas_hoy(request):
    #recordar que al aplicar el filter debemos parsear la fecha solo a dia/mes/año ya que si no jamas va a coincidir con la hora establecida por el evento y la hora actual de la peticion
    tareas = Evento.objects.filter(hora_fecha_e__date=date.today()).order_by('hora_fecha_e')
    lista_vacia = tareas.exists()
    """ tarea_ordenada = tareas.order_by('hora_fecha_e') """

    return render(request,"tareas_hoy.html",{'tareas':tareas,'vacia_o_no':lista_vacia})

def tareas_week(request):
    #en la clase date, tenemos el metodo weekday, el cual nos va a devolver un numero entero indicando como si de una lista se tratase, el indice del dia de la semana, x ejemplo: Lunes=0 y Domingo=6}
    #se ingresan numeros enteros a los parametros, utilizamos el dia de hoy para reconocer la fecha actual accediendo a sus datos a travez de los atributos year(año),month(mes) y day(dia)
    numero_dia = date.today().weekday()
    #timedelta nos permite transformar numeros enteros en fechas, lo cual sirve para despues realizar operaciones algebraicas con los objetos de tipo fecha
    #los datos guardados en este caso son, el dia de la semana, las horas, minutos y segundos para luego usarlos en una resta
    delta = timedelta(days=numero_dia)
    #recorrer los dias con delta_sumar1
    delta_sumar1 = timedelta(days=1)
    #ahora suponiendo que el dia sea jueves(3), esos datos se usaran para restarlo y mover el puntero como referencia al dia dia 0 (lunes)

    dias=[]
    for i in range(0,7):
        sumar = timedelta(days=i)
        dia_x = date.today()-delta+sumar
        dias.append(dia_x)
    print(dias[0])

    """ almacenar en una lista externa al for los datos de cada dia, para obtener una lista """
    """ lista [] for dia in dias
    return el dia [0] --->> dia[1] --->> dia[2] """
    """ lunes = Evento.objects.filter(hora_fecha_e__date=date.today()-delta).order_by("hora_fecha_e") """
    lunes = Evento.objects.filter(hora_fecha_e__date=dias[0]).order_by("hora_fecha_e")
    martes = Evento.objects.filter(hora_fecha_e__date=dias[1]).order_by("hora_fecha_e")
    miercoles = Evento.objects.filter(hora_fecha_e__date=dias[2]).order_by("hora_fecha_e")
    jueves = Evento.objects.filter(hora_fecha_e__date=dias[3]).order_by("hora_fecha_e")
    viernes = Evento.objects.filter(hora_fecha_e__date=dias[4]).order_by("hora_fecha_e")
    sabado = Evento.objects.filter(hora_fecha_e__date=dias[5]).order_by("hora_fecha_e")
    domingo = Evento.objects.filter(hora_fecha_e__date=dias[6]).order_by("hora_fecha_e")
    #con delta_sumar1 vamos a ir recorriendo los dias de uno en uno

    
    return render(request, "tareas_week.html",{"lunes":lunes,"martes":martes,"miercoles":miercoles,"jueves":jueves,"viernes":viernes,"sabado":sabado,"domingo":domingo})

def tareas_month(request):
    anio = date.today().year
    mes = date.today().month
    calendario = calendar.TextCalendar(calendar.SUNDAY)
    dias_tareas = []
    dias_tareas_mes = {"dias_tareas":dias_tareas}

    for cal_dia in calendario.itermonthdays(anio, mes):
        if(cal_dia):
            fecha = date(anio, mes, cal_dia)
            tarea = Evento.objects.filter(hora_fecha_e__date=date(anio, mes, cal_dia)).order_by("hora_fecha_e")
            dias_tareas.append([fecha, tarea])
            
        else:
            dias_tareas.append([None,None])

    return render(request, "tareas_month.html", dias_tareas_mes)
