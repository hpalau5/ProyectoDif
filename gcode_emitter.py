#[(x,y,z),(x,y,z])
#si la coordenada z es mas alta que la actual, quiere decir que el gcode
#sera un g0
#sino de normal es un g1
velocidadExtrusion = 20
velocidadMovimiento = 1800

def emit_header():
    print("G21") #trabajar en milimetros
    print("G90") #usar posicionamiento absoluto
    print("G82") #colocar el extrusor en posicionamiento absoluto

    print("M104 S190 T0 ") #Iniciar el calentamiento del Extrusor T0 hasta 190 grados centígrados.
    print("M140 S50") # iniciar el calentamiento de la cama hasta 50 grados centígrados.
    print("G28 X0") #enviar todos los ejes a Home, mientras se calienta el Extrusor.
    print("M106 S255")# se ajusta el ventilador a la velocidad máxima.
    print("E2" + str(velocidadExtrusion) + " F" + str(velocidadMovimiento)) #extrusion y velocidad

def emit_gcode(arrayPuntos):

    ##si la z es diferente a la ultima, vamos a la z actual + 1mm, movemos a xy y bajamos la a z actual
    #se supone que solo con moverse a la xy sin imprimir no deberia hacer falta subir ni nada no?
    global up
    up = False
    def imprimirPunto(punto):
        global up
        if up:
            print("G0 X" + '{:.8f}'.format(punto[0]) + " Y" + '{:.8f}'.format(punto[1]) + " Z" + '{:.8f}'.format(actualZ+1))
            print("G0 X" + '{:.8f}'.format(punto[0]) + " Y" + '{:.8f}'.format(punto[1]) + " Z" + '{:.8f}'.format(punto[2]))
            up = False
        elif punto[2]==actualZ:
           print("G1" +" X" + '{:.8f}'.format(punto[0]) + " Y" + '{:.8f}'.format(punto[1]) + " Z" + '{:.8f}'.format(punto[2]))
        else:
            print("G0 Z" + '{:.8f}'.format(actualZ+1))
            up = True

    #con g0 vamos al primer punto y aplicamos ya el algoritmo de transformacion
    if len(arrayPuntos) != 0:
        actualZ = arrayPuntos[0][2]
        print("G0" +" X" + '{:.8f}'.format(arrayPuntos[0][0]) + " Y" + '{:.8f}'.format(arrayPuntos[0][1]) + " Z" + '{:.8f}'.format(actualZ+1))
        print("G0" + " Z" + '{:.8f}'.format(arrayPuntos[0][2]))


    for punto in arrayPuntos:
        imprimirPunto(punto)

    #para la siguiente capa seria repetir el bucle con los nuevos puntos y cambiando actualZ
