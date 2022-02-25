# Relacion Grados sexagesimal y Radian
def main():

    import math

    PI = math.pi()

    def grados_Radianes(grados, radianes):
        GRADOS = (radianes * 360) / (2 * PI)
        return GRADOS

    
    GRADOS = 45
    RADIANES = 2

    resultado = round(grados_Radianes(GRADOS, RADIANES), 2)
    print(f'Tus radianes a grados son {resultado} grados')


if __name__ == '__main__':
    main()