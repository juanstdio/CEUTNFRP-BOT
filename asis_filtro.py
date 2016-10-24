# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup

def asistencia():
    respuesta = urllib.urlopen('http://www.frp.utn.edu.ar/asistenciaETC')
    html = respuesta.read()

    sopa = BeautifulSoup(html,'html.parser')

    puro = sopa.get_text()
    filtrado = puro.split('2016')
    filtrado = filtrado[1].split('Registro')
    filtrado = filtrado[0].split('\n')
     
    return filtrado
