# -*- coding: utf-8 -*-
from lxml import etree

doc = etree.parse('planets.xml')

raiz = doc.getroot()

lista1 = []
lista2 = []
lista3 = []

planets = raiz.findall('planet')
moons = raiz.findall('planet/moon')
planetsnames = raiz.findall('planet/name')

for planet in planets:
    lista2.append(planet.find("name").text)
for moon in moons:
    lista3.append(moon.find("name").text)

cad1 = raw_input("Nombre astro:")
while cad1 != "*":
        if cad1 in lista2:
            lista1.append(cad1)
            cad1 = raw_input("Nombre astro:")
        elif cad1 in lista3:
            lista1.append(cad1)
            cad1 = raw_input("Nombre astro:")
        else:
            print "Astro no existente"
            cad1 = raw_input("Nombre astro:")

cont = 0
for cadastro in lista1:
    for planet in planets:
        if cadastro == planet.find("name").text:
            cont = cont + float(planet.find("mass").text)
    for moon in moons:
        if cadastro == moon.find("name").text:
            cont = cont + float(moon.find("mass").text)

print cont





