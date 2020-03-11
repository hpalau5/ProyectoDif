#[(x,y,z),(x,y,z])
#si la coordenada z es mas alta que la actua, quiere decir que el gcode
#sera un g0
#sino de normal es un g1

#con g1 vamos al primer punto y aplicamos ya el algoritmo de transformacion
gcode = ""
gcode+="G21" #trabajar en milimetros
gcode+="G90" #usar posicionamiento absoluto
gcode+="G82" #colocar el extrusor en posicionamiento absoluto

gcode+="G1" f x y z


for each(punto in puntosPerimetro)
    gcode+=imprimirPunto(punto)


imprimirPunto((x,y,z))
    return "G0 + " +"X" + x + "Y" + y + "Z" + "z\n"

    if z>
    subes
    mueves a xy
    bajas la z