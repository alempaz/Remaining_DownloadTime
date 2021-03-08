import sys

input_invalido = True


def start():
    gb1 = input('Tu archivo a descargar esta en Mb o Gb? Responde MB/GB: ')
    gb = gb1.lower()

    if gb == 'gb':
        gb_descargar = input('Ingresa el tamaño en Gb a descargar: ')
        mb_descargar = float(gb_descargar) * 1024
        velocidad_descarga = input('Ingresa la velocidad de descarga en Mb/s: ')
        tiempo_restseg = float(mb_descargar) / float(velocidad_descarga)
        tiempo_restmin = float(tiempo_restseg) * 60
        day = tiempo_restseg // (24 * 3600)
        tiempo_restseg = tiempo_restseg % (24 * 3600)
        hour = tiempo_restseg // 3600
        tiempo_restseg %= 3600
        minutes = tiempo_restseg // 60
        tiempo_restseg %= 60
        seconds = tiempo_restseg
        print('Tiempo restante de tu descarga es: Dias:%d -- Horas=:%d -- Minutos=%d -- Segundos=%d' % (
        day, hour, minutes, seconds))
        nuev = input('Desea hacer otro calculo? Si/No: ')
        nuevo = nuev.lower()
        if nuevo == 'si' or nuevo == 's':
            start()
        if nuevo == 'no' or nuevo == 'n':
            print('Ok. Adios!')
            exit()
        else:
            print('Mmmm, no se que quisiste decir, pero creo que no quieres hacer otro calculo. Adios!')
            exit()

    if gb == 'mb':
        mb_descargar = input('Ingresa el tamaño en Mb a descargar: ')
        velocidad_descarga = input('Ingresa la velocidad de descarga en Mb/s: ')
        tiempo_restseg = float(mb_descargar) / float(velocidad_descarga)
        tiempo_restmin = float(tiempo_restseg) * 60
        day = tiempo_restseg // (24 * 3600)
        tiempo_restseg = tiempo_restseg % (24 * 3600)
        hour = tiempo_restseg // 3600
        tiempo_restseg %= 3600
        minutes = tiempo_restseg // 60
        tiempo_restseg %= 60
        seconds = tiempo_restseg
        print('Tiempo restante de tu descarga es: Dias: %d -- Horas=: %d -- Minutos: %d -- Segundos: %d' % (
            day, hour, minutes, seconds))
        nuev = input('Desea hacer otro calculo? Responde Si o No: ')
        nuevo = nuev.lower()
        if nuevo == 'si' or nuevo == 's':
            start()
        if nuevo == 'no' or nuevo == 'n':
            print('Ok. Adios!')
            exit()
        else:
            print('Mmmm, no se que quisiste decir, prueba de nuevo')
            return

    else:
        print('Tu respuesta no fue Mb o Gb. Prueba de Nuevo.')


while input_invalido == True:
    start()