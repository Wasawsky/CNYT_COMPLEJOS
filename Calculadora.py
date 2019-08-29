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
    """Recibo 2 vectores complejos  y sumo -> vector complejo
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
    """Recibo 1 vector complejo y un escalar y hago la multiplicacion escalar de vector -> vector complejo
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
    """Recibo una matriz compleja y un escalar y hago la multiplicacion escalar de matriz -> matriz compleja
    """
    for j in range(len(m1)):
        m1[j]=multiplicacionEscalarVector(m1[j],c)
    return m1
def transpuesta(m1):
    """Recibo una matriz compleja y determino su transpuesta -> matriz compleja
    """
    m2=[[(0,0) for x in m1] for x in m1[0]]
    for j in range(len(m1[0])):
        for k in range(len(m1)):
            m2[j][k]=m1[k][j]
    return m2
def matrizConjugada(m1):
    """Recibo una matriz compleja y determino la matriz conjugada -> matriz compleja
    """
    for j in range(len(m1)):
        for k in range(len(m1[0])):
            m1[j][k]=conjugado(m1[j][k])
    return m1
def matrizAdjunta(m1):
    """Recibo una matriz compleja y determino matriz adjunta -> matriz compleja
    """
    return matrizConjugada(transpuesta(m1))
def multiplicacionMatrizMatriz(m1,m2):
    """Recibo 2 matrices complejas y hallo la multiplicacion de matrices -> matriz compleja
       se debe cumplr a:m*n, b:n*p
    """
    m3=[[(0,0) for x in m2[0]] for x in m1]
    for j in range(len(m1)):
        for k in range(len(m2[0])):
            resultado=(0,0)
            for h in range(len(m2)):
                resultado=suma(multiplicacion(m1[j][h],m2[h][k]),resultado)
            m3[j][k]=resultado
    return m3
def accion(m1,v1):
    """ Recibo 1 matriz compleja de n*n y 1 vector de n*1
            y hallo la accion de la matriz sobre el vector   -> vector complejo
    """
    return multiplicacionMatrizMatriz(m1,transpuesta([v1]))
def productoInternoVector(v1,v2):
    """ Recibo 2 vectores de n*1 y calculo el producto interno -> numero complejo
    """
    return multiplicacionMatrizMatriz(matrizConjugada([v1]),transpuesta([v2]))[0][0]
def sumaDiagonal(m1):
    """ Recibo una matriz de n*n y calculo la suma de los elementos diagonales -> numero complejo
    """
    sumaD=(0,0)
    for j in range(len(m1)):
        sumaD=suma(m1[j][j],sumaD)
    return sumaD
def productoInternoMatriz(m1,m2):
    """ Recibo 2 matrices complejas y calculo el producto interno -> numero complejo
    """
    return sumaDiagonal(multiplicacionMatrizMatriz(matrizAdjunta(m1),m2))
def normaVector(v1):
    """ Recibo 1 vector de n*1 y hallo su norma -> numero real
    """
    print(productoInternoVector(v1,v1)[0])
    return math.sqrt(productoInternoVector(v1,v1)[0])
def normaMatriz(m1):
    """ Recibo 1 matriz de n*m y hallo su norma -> numero real
    """
    return math.sqrt(productoInternoMatriz(m1,m1)[0])
def distanciaVectorVector(v1,v2):
    """ Recibo 2 vectores y determino su distancia -> numero real
    """
    print(sumaVectores(v1,inversa(v2)))
    return normaVector(sumaVectores(v1,inversa(v2)))
def distanciaMatrizMatriz(m1,m2):
    """ Recibo 2 matrices y determino su distancia -> numero real
    """
    return normaMatriz(sumaMatrices(m1,inversaMatriz(m2)))
def matrizIdentidad(n):
    """ Recibo un entero y determino la matriz identidad n*n -> matriz 
    """
    ident=[[(0,0) for x in range(n)] for x in range(n)]
    for j in range(n):
        ident[j][j]=(1,0)
    return ident
def matrizUnitaria(m1):
    """ Determino si una matriz es unitaria -> boolean
    """
    ident=matrizIdentidad(len(m1))
    m1=multiplicacionMatrizMatriz(matrizAdjunta(m1),m1)
    esUnitaria=True
    for j in range(len(m1)):
        for k in range(len(m1)):
            if (m1[j][k]!=ident[j][k]):
                esUnitaria=False
                break
    return esUnitaria
def matrizHermitian(m1):
    """ Determino si una matriz es hermitian -> boolean
    """
    esHermitian=True
    m2=matrizAdjunta(m1)
    for j in range(len(m1)):
        for k in range(len(m1)):
            if (resta(m1[j][k],m2[j][k])!=(0,0)):
                esHermitian=False
                break
    return esHermitian
    
#[[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]]


#v1=[tuple(map(float, x.split(","))) for x in (input().split(" "))]
#v2=[tuple(map(float, x.split(","))) for x in (input().split(" "))]
"""""""""

"""""""""


"""""""""
m1=[]
m2=[]
for i in range(2):
    vf=[tuple(map(float, x.split(","))) for x in (input().split(" "))]
    m1.append(vf)
for i in range(2):
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
#print(matrizConjugada(m1))
#print(matrizAdjunta(m1))
#print(multiplicacionMatrizMatriz(m1,m2))
#print(accion(m1,v1))
#print(productoInternoVector(v1,v2))
#print(sumaDiagonal(m1))
#print(productoInternoMatriz(m1,m2))
#print(normaVector(v1))
#print(normaMatriz(m1))
#print(distanciaVectorVector(v1,v2))
#print(distanciaMatrizMatriz(m1,m2))
#print(matrizUnitaria(m1))
#print(matrizHermitian(m1))
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


"""
###ANOTACIONES

FORMA DE VECTOR SENCILLA 1*N

V = [V1,V2,V3,...VN]

FORMA DE VECTOR N*1 EN MATRIZ

M = [[V1],[V2],[V3],....,[VN]]

FORMA DE VECTOR 1*N EN MATRIZ

M = [[V1,V2,V3,...VN]]

FORMA DE MATRIZ M*N

MA=[MA1[MA11, MA12, MA13, .....MA1N],
    MA2[MA21, MA22, MA23, .....MA1N],
    MA3[MA31, MA32, MA33, .....MA1N],
    ......,
    MAM[MAM1, MAM2, MAM3,.....,MAMN]]

"""
