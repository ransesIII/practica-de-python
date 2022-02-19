# Relacion Grados sexagesimal y Radian

import math

PI = math.pi()
GRADOS = 45
RADIANES = 67

def grados_Radianes(grados, radianes):
    GRADOS = (radianes * 360) // (2 * PI)
    return GRADOS 