from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from .models import Familiar

def familia(self):
    dp=datetime.date(1987,7,2)
    dm=datetime.date(1987,12,10)
    da=datetime.date(2019,3,22)
    do=datetime.date(2021,10,2)
    padre=Familiar(puesto="El Padre", nombre="Nicolas",apellido="Finetti",dni=32804357,fechaNacimiento=dp)
    madre=Familiar(puesto="La Madre", nombre="Lujan",apellido="Fernandez",dni=33046288,fechaNacimiento=dm)
    hija=Familiar(puesto="La Hija", nombre="Justina",apellido="Finetti Fernandez",dni=57511551,fechaNacimiento=da)
    hijo=Familiar(puesto="El Hijo", nombre="Pedro",apellido="Finetti Fernandez",dni=59061554,fechaNacimiento=do)
    familia=[padre,madre,hija,hijo]
    for n in familia:
        n.save()

    diccionario = {"padre" : padre, "madre" : madre, "hija": hija, "hijo":hijo, "familia":familia}
    plantilla=loader.get_template("template2.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)


