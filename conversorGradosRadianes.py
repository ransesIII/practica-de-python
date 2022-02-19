# Relacion Grados sexagesimal y Radian

import math

PI = 3.1415
GRADOS = 45
RADIANES = 67

def grados_Radianes(grados, radianes):
    GRADOS = (radianes * 360) // (2 * PI)
    return GRADOS 

print(grados_Radianes(0, RADIANES))