from lxml import etree

doc=etree.parse('planets.xml')

raiz = doc.getroot()

planets = raiz.findall('planet')


for planet in planets:
    print planet.find("name").text
    if planet.find("moon/name") == None :
        print "* Sin satelites"
    else:
        moons = planet.findall("moon/name")
        for moon in moons:
            print "*", moon.text