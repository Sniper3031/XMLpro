# -*- coding: utf-8 -*-
from lxml import etree

doc=etree.parse('planets.xml')

raiz = doc.getroot()

seg1 = raw_input("Inicio del segmento:")
seg2 = raw_input("Fin del segmento:")

planets = raiz.findall('planet')
moons = raiz.findall('planet/moon')

if float(seg1) > float(seg2):
    print "Error, el inicio del segmento no puede ser mayor que el final."
else:
    for planet in planets:
        if float(planet.find("orbitalspeed").text) >= float(seg1) and float(planet.find("orbitalspeed").text) <= float(seg2):
            print planet.find("name").text
            print "* ", planet.find("orbitalspeed").text

    for moon in moons:
        if float(moon.find("orbitalspeed").text) >= float(seg1) and float(moon.find("orbitalspeed").text) <= float(seg2):
            print moon.find("name").text
            print "* ", moon.find("orbitalspeed").text