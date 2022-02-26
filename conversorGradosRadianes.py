# Relacion Grados sexagesimal y Radian
def main():

    PI = 3.1415

    def DeRadianes_Grados(radianes):
        GRADOS = (radianes * 360) / (2 * PI)
        return GRADOS
    
    def DeGrados_Radianes(grados):
        RADIANES = ((2 * PI) * grados) / 360
        return RADIANES

    
    INTRO = 'Convertidor de Grados/Radianes'
    print(INTRO)

    OPCIONES = input('Elige una opcion de convercion; g para Radianes a Grados, o, r para Grados a Radianes: ')
    print(OPCIONES)


    if OPCIONES == 'g':
        radianes = int(input('Escribe los Radianes: '))
        resultadoGrados = round(DeRadianes_Grados(radianes), 2)
        print(f'{resultadoGrados} Grados')
    elif OPCIONES == 'r':
        grados = int(input('Escribe los Grados: '))
        resultadoRadianes = round(DeGrados_Radianes(grados), 2)
        print(f'{resultadoRadianes} Radianes')
    
    
    # resultado = round(grados_Radianes(), 2)
    # print(f'Tus radianes a grados son {resultado} grados')


if __name__ == '__main__':
    main()