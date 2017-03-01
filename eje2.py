# -*- coding: utf-8 -*-
from lxml import etree

doc=etree.parse('planets.xml')

raiz = doc.getroot()

seg1 = raw_input("Inicio del segmento:")
seg2 = raw_input("Fin del segmento:")

planets = raiz.findall('planet')

cont = 0
for planet in planets:
    if float(planet.find("inclination").text) >= float(seg1) and float(planet.find("inclination").text) <= float(seg2):
        cont = cont+1

print "Numero de planetas con eje de inclinacion entre" , seg1, "y" , seg2 ,":" , cont
