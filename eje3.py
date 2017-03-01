# -*- coding: utf-8 -*-
from lxml import etree

doc=etree.parse('planets.xml')

raiz = doc.getroot()

planets = raiz.findall('planet')
moons = raiz.findall('planet/moon')

cad1 = raw_input("Nombre astro:")

for planet in planets:
    if cad1 == planet.find("name").text:
        print "Diametro:", planet.find("diameter").text
        print "Masa:", planet.find("mass").text

for moon in moons:
    if cad1 == moon.find("name").text:
        print "Diametro:", moon.find("diameter").text
        print "Masa:", moon.find("mass").text