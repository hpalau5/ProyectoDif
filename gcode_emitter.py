#[(x,y,z),(x,y,z])
#si la coordenada z es mas alta que la actual, quiere decir que el gcode
#sera un g0
#sino de normal es un g1
velocidadExtrusion = 20
velocidadMovimiento = 1800

def generarGcode(arrayPuntos):

    ##si la z es diferente a la ultima, vamos a la z actual + 1mm, movemos a xy y bajamos la a z actual
    #se supone que solo con moverse a la xy sin imprimir no deberia hacer falta subir ni nada no?
    def imprimirPunto(puntos):
        if puntos[2]==actualZ:
           print("G1" +" X" + str(puntos[0]) + " Y" + str(puntos[1]) + " Z" + str(puntos[2]))
        else:
            print("G0 Z" + str(actualZ+1))
            print("G0 X" + str(puntos[0]) + " Y" + str(puntos[1]))
            print("G0 Z" + str(actualZ))

    arrayPuntos = [(1,1,2),(2,2,2),(1,5,4),(1,5,2),(1,2,2)]

    print("G21") #trabajar en milimetros
    print("G90") #usar posicionamiento absoluto
    print("G82") #colocar el extrusor en posicionamiento absoluto

    print("M104 S190 T0 ") #Iniciar el calentamiento del Extrusor T0 hasta 190 grados centígrados.
    print("M140 S50") # iniciar el calentamiento de la cama hasta 50 grados centígrados.
    print("G28 X0") #enviar todos los ejes a Home, mientras se calienta el Extrusor.
    print("M106 S255")# se ajusta el ventilador a la velocidad máxima.
    print("E2" + str(velocidadExtrusion) + " F" + str(velocidadMovimiento)) #extrusion y velocidad

    #con g0 vamos al primer punto y aplicamos ya el algoritmo de transformacion
    print("G0" +" X" + str(arrayPuntos[0][0]) + " Y" + str(arrayPuntos[0][1]) + " Z" + str(arrayPuntos[0][2]))
    actualZ=arrayPuntos[0][2]
    arrayPuntos.pop(0)

    for punto in arrayPuntos:
        imprimirPunto(punto)

    #para la siguiente capa seria repetir el bucle con los nuevos puntos y cambiando actualZ
arrayPuntos = [(1,1,2),(2,2,2),(1,5,4),(1,5,2),(1,2,2)]
generarGcode(arrayPuntos)
