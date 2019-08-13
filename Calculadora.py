#Numeros complejos
#MICHAEL BALLESTEROS
#2019-2

import math

#---------------------------------------------------------------------

def suma(c1,c2):
    """Recibo 2 complejos y los suma -> complejo
    """
    a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
    return (a1+a2,b1+b2)
def resta(c1,c2):
    """Recibo 2 complejos y los resta -> complejo
    """
    a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
    return (a1-a2,b1-b2)
def multiplicacion(c1,c2):
    """Recibo 2 complejos y los multiplica -> complejo
    """
    a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
    return (a1*a2-b1*b2,a1*b2+a2*b1)
def division(c1,c2):
    """Recibo 2 complejos y los divido -> complejo
    """
    a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
    x = float("{0:.1f}".format((a1*a2+b1*b2)/(a2**2+b2**2)))
    y = float("{0:.1f}".format((a2*b1-a1*b2)/(a2**2+b2**2)))
    return (x,y)
def modulo(c1):
    """Complejo y hallo modulo -> entero
    """
    a1,b1=c1[0],c1[1]
    return float("{0:.2f}".format((a1**2+b1**2)**(1/2)))
def conjugado(c1):
    """Recibo complejos y lo conjuga -> complejo
    """
    a1,b1=c1[0],c1[1]
    return (a1,b1*-1)
def fase(c):
    """Recibo complejo hallo fase en grados -> entero
    """
    a,b=c[0],c[1]
    return float("{0:.2f}".format(((math.atan2(b,a))*180)/math.pi))
def convpolaracartesiano(c):
    """Recibo polar (angulo en grados)y doy cartesiano -> Cartesiano
    """
    p,ang=c[0],(c[1]*math.pi)/180
    x=float("{0:.2f}".format(p*math.cos(ang)))
    y=float("{0:.2f}".format(p*math.sin(ang)))
    return (x,y)
def convcartesianoapolar(c):
    """Recibo cartesiano y doy polar -> Polar
    """
    a,b = c[0],c[1]
    p = modulo(c)
    ang = fase(c)
    return (p,ang)

#---------------------------------------------------------------------


def sumaVectores(v1,v2):
    """Recibo 2 vectores complejos y sumo -> vector complejo
    """
    for j in range(len(v1)):
        v1[j]=suma(v1[j],v2[j])
    return v1
def inversa(v1):
    """Recibo 1 vector complejo y hallo inverso aditivo -> vector complejo
    """
    for j in range(len(v1)):
        v1[j]=multiplicacion((-1,0),v1[j])

    return v1
def multiplicacionEscalarVector(v1,c):
    """ Recibo un vector complejo y un escalar y hago la multiplicacion escalar de vector -> vector complejo
    """
    for j in range(len(v1)):
        v1[j]=multiplicacion(v1[j],c)

    return v1
def sumaMatrices(m1,m2):
    """Recibo 2 matrices complejas y las sumo -> matriz compleja
    """
    for j in range(len(m1)):
        m1[j]=sumaVectores(m1[j],m2[j])

    return m1
def inversaMatriz(m1):
    """Recibo matriz compleja y hallo inverso aditivo -> matriz compleja
    """
    for j in range(len(m1)):
        m1[j]=inversa(m1[j])

    return m1
def multiplicacionEscalarMatriz(m1,c):
    """ Recibo una matriz compleja y un escalar y hago la multiplicacion escalar de matriz -> matriz compleja
    """
    for j in range(len(m1)):
        m1[j]=multiplicacionEscalarVector(m1[j],c)
    return m1
def transpuesta(m1):
    m2=[[(0,0) for x in m1] for x in m1[0]]

    for j in range(len(m1[0])):
        for k in range(len(m1)):
            m2[j][k]=m1[k][j]
    return m2

#[[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]]
"""""""""
v1=[]
v2=[]
for i in range(4):
    c = tuple(map(float, input().split(",")))
    v1.append(c)

for i in range(4):
    c = tuple(map(float, input().split(",")))
    v2.append(c)
"""""""""
"""""""""
m1=[]
m2=[]
for i in range(3):
    vf=[tuple(map(float, x.split(","))) for x in (input().split(" "))]
    m1.append(vf)

for i in range(4):
    vf=[tuple(map(float, x.split(","))) for x in (input().split(" "))]
    m2.append(vf)
"""""""""
#c = tuple(map(float,input().split(",")))
#print(v1)
#print(v2)
#print(sumaVectores(v1,v2))
#print(inversa(v1))
#print(multiplicacionEscalarVector(v1,c))
#print(sumaMatrices(m1,m2))
#print(inversaMatriz(m1))
#print(multiplicacionEscalarMatriz(m1,c))
#print(transpuesta(m1))

################################
#c = tuple(map(float,input().split(",")))
#c1 = tuple(map(int,input().split(",")))
#c2 = tuple(map(int,input().split(",")))


#print(suma(c1,c2))
#print(resta(c1,c2))
#print(multiplicacion(c1,c2))
#print(division(c1,c2))
#print(modulo(c))
#print(conjugado(c))
#print(convpolaracartesiano(c))
#print(convcartesianoapolar(c))
#print(fase(c))
################################