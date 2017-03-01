from lxml import etree

doc=etree.parse('planets.xml')

raiz = doc.getroot()

planets = raiz.findall('planet')

print len(planets)
print raiz.find("name").text

for planet in planets:
    print planet.find("name").text